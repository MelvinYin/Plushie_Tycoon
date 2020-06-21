package plushie_tycoon.local.localEngine;
import plushie_tycoon.config.baseObjects.BaseObjects;
import plushie_tycoon.config.baseObjects.Products;
import plushie_tycoon.config.baseObjects.Resources;

import plushie_tycoon.config.Defaults;
import plushie_tycoon.config.Initials;
import plushie_tycoon.local.ClientPageService;
import plushie_tycoon.local.localEngine.inventory.LocalInventory;
import plushie_tycoon.local.localEngine.market.LocalMarket;
import plushie_tycoon.Grpc.*;
import plushie_tycoon.local.utils.BaseStringConverter;

import java.util.Random;

import java.util.HashMap;
import io.grpc.Server;
import io.grpc.ServerBuilder;

import javax.swing.plaf.basic.BasicBorders;
import java.io.IOException;

public class LocalEngine {
    private StateHistory history;
    private double budget;
    private LocalMarket market;
    private LocalInventory LocalInventory;
    public String userid;
    private int time;
    public HashMap<BaseObjects, Integer> buySellTracker;
    public HashMap<BaseObjects, Integer> makeTracker;
    int serverPortno;
    int webPagePortno;
    ClientPageService clientPageService;

    public LocalEngine(int webPagePortno, int serverPortno){
        history = new StateHistory();
        market = new LocalMarket();
        budget = Initials.budget;
        LocalInventory = new LocalInventory(Initials.quantities);
        time = Initials.time;
        buySellTracker = new HashMap<>();
        makeTracker = new HashMap<>();
        Random random = new Random();
        userid = String.valueOf(random.nextInt());
        this.serverPortno = serverPortno;
        this.webPagePortno = webPagePortno;
        clientPageService = new ClientPageService(this);
    }

    public void initFromGlobalServer(){
        ToGlobalServer.waitForReady(serverPortno);
        ToGlobalServer.ping(serverPortno);
        Snapshot initSnapshot = ToGlobalServer.register(serverPortno, userid);
        updateLocal(initSnapshot);
    }

    public void runServices() throws IOException, InterruptedException {
        Server server = ServerBuilder.forPort(webPagePortno).addService(clientPageService).build();
        server.start();
        server.awaitTermination();
    }

    public void commit(){
        history.addBudget(budget);
        history.addTime(time);
        history.addInventory(LocalInventory);
        history.addMarket(market);
    }

    public boolean canReverseCall(){
        return !history.isEmpty();
    }

    public void reverseCall(){
        budget = history.getBudget();
        time = history.getTime();
        LocalInventory = history.getLocalInventory();
        market = history.getMarket();
        history.pop();
    }

    public Snapshot buy(BaseObjects object, int quantity){
        double price = market.get(object) * quantity;
        System.out.println("Buying " + object.toString() + " " + quantity + " price " + price +" budget " + budget);
        if (price > budget){
            String errorMsg = "Cannot buy <" + quantity + "> of <" + object + "> as it costs <" + price +
                    "> and budget is <" + budget + ">.";
            return getNullReturn(errorMsg);
        }
        LocalInventory.add(object, quantity);
        budget -= price;
        commit();
        buySellTracker.put(object, buySellTracker.getOrDefault(object, 0) + quantity);
        return getUpdateReturn();
    }
    public Snapshot sell(BaseObjects object, int quantity){
        if (LocalInventory.get(object) < quantity){
            String errorMsg = "Cannot sell <" + quantity + "> of <" + object + "> as you only have <"
                    + LocalInventory.get(object) + ">.";
            return getNullReturn(errorMsg);
        }
        LocalInventory.sub(object, quantity);
        budget += market.get(object) * quantity;
        commit();
        buySellTracker.put(object, buySellTracker.getOrDefault(object, 0) - quantity);
        return getUpdateReturn();
    }

    public boolean canMake(Products product, int quantity){
        for (Resources resource: Resources.values()){
            if (Defaults.getResourceRatio(product, resource) * quantity > LocalInventory.get(resource)){
                return false;
            }
        }
        return true;
    }

    public Snapshot make(BaseObjects object, int quantity){
        Products product = (Products) object;
        if (!canMake(product, quantity)){
            String errorMsg = "Cannot make <" + quantity + "> of <" + product + "> as you only have <"
                    + LocalInventory.get(product) + ">.";
            return getNullReturn(errorMsg);
        }
        LocalInventory.add(product, quantity);
        for (Resources resource: Resources.values()){
            LocalInventory.sub(resource, quantity * Defaults.getResourceRatio(product, resource));
        }
        commit();
        makeTracker.put(object, makeTracker.getOrDefault(object, 0) + quantity);
        return getUpdateReturn();
    }

    public Snapshot next(){
        ProposedChanges.Builder changes = ProposedChanges.newBuilder();
        changes.setUserid(userid);
        for (Resources resource: Resources.values()){
            changes.putBuySell(BaseStringConverter.convert(resource), buySellTracker.getOrDefault(resource, 0));
            changes.putMake(BaseStringConverter.convert(resource), makeTracker.getOrDefault(resource, 0));
        }
        for (Products product: Products.values()){
            changes.putBuySell(BaseStringConverter.convert(product), buySellTracker.getOrDefault(product, 0));
            changes.putMake(BaseStringConverter.convert(product), makeTracker.getOrDefault(product, 0));
        }
        ToGlobalServer.send(serverPortno, changes.build());
        budget -= LocalInventory.getTotalMoveCost();
        budget -= LocalInventory.getTotalStorageCost();
        LocalInventory.resetMovement();
        time++;
        return getUpdateReturn();
    }

    public boolean checkIfNextTurn(){
        int serverTime = ToGlobalServer.getTime(serverPortno);
        if (serverTime == time){
            return false;
        }
        Snapshot newData = ToGlobalServer.query(serverPortno, userid);
        updateLocal(newData);
        return true;
    }

    public void updateLocal(Snapshot snapshot){
//        todo: later on, update everything from here so local doesn't require defaults or initials. Same with ui side.
        budget = snapshot.getBudget();
        time = snapshot.getTime();
        for (Resources base: Resources.values()){
            String baseString = BaseStringConverter.convert(base);
            market.set(base, snapshot.getPricesOrThrow(baseString));
            LocalInventory.set(base, snapshot.getQuantitiesOrThrow(baseString));
        }
        for (Products base: Products.values()){
            String baseString = BaseStringConverter.convert(base);
            market.set(base, snapshot.getPricesOrThrow(baseString));
            LocalInventory.set(base, snapshot.getQuantitiesOrThrow(baseString));
        }
        history.reset();
        buySellTracker.clear();
        makeTracker.clear();
    }

    public Snapshot getData(){
        return getUpdateReturn();
    }

    public Snapshot save(){
        return getUpdateReturn();
    }

    public Snapshot load(){
        return getUpdateReturn();
    }

    public Snapshot back(){
        if (!canReverseCall()){
            String errorMsg = "Cannot reverse call, callstack is empty.";
            return getNullReturn(errorMsg);
        }
        reverseCall();
        return getUpdateReturn();
    }

    public Snapshot quit(){
        return getUpdateReturn();
    }

    public Snapshot init(){
        return getUpdateReturn();
    }

    private Snapshot getNullReturn(String consoleOutput){
        return Snapshot.newBuilder().setAction("pause").setConsoleOutput(consoleOutput).build();
    }

    private Snapshot getUpdateReturn(){
        Snapshot.Builder snapshot = Snapshot.newBuilder();
//        prices
        for (Products base: Products.values()){
            String baseString = BaseStringConverter.convert(base);
            snapshot.putPrices(baseString, market.get(base));
            snapshot.putQuantities(baseString, LocalInventory.get(base));
            snapshot.putWeights(baseString, Defaults.getWeight(base));
            snapshot.putVolumes(baseString, Defaults.getVolume(base));

            mItemCost.Builder itemcost = mItemCost.newBuilder();
            itemcost.setMovein(LocalInventory.getMoveInCost(base));
            itemcost.setMoveout(LocalInventory.getMoveOutCost(base));
            itemcost.setStorage(LocalInventory.getStorageCost(base));
            snapshot.putItemCost(baseString, itemcost.build());
        }

        for (Resources base: Resources.values()){
            String baseString = BaseStringConverter.convert(base);
            snapshot.putPrices(baseString, market.get(base));
            snapshot.putQuantities(baseString, LocalInventory.get(base));
            snapshot.putWeights(baseString, Defaults.getWeight(base));
            snapshot.putVolumes(baseString, Defaults.getVolume(base));

            mItemCost.Builder itemcost = mItemCost.newBuilder();
            itemcost.setMovein(LocalInventory.getMoveInCost(base));
            itemcost.setMoveout(LocalInventory.getMoveOutCost(base));
            itemcost.setStorage(LocalInventory.getStorageCost(base));
            snapshot.putItemCost(baseString, itemcost.build());
        }

        for (Products product: Products.values()){
            String productString = BaseStringConverter.convert(product);
            mRatioPerProduct.Builder ratioPerProduct = mRatioPerProduct.newBuilder();
            for (Resources resource: Resources.values()){
                String resourceString = BaseStringConverter.convert(resource);
                ratioPerProduct.putRatio(resourceString, Defaults.getResourceRatio(product, resource));
            }
            snapshot.putResourceRatio(productString, ratioPerProduct.build());
        }

        snapshot.setTime(time);
        snapshot.setAction("update");
        snapshot.setBudget(budget);
        snapshot.setConsoleOutput("console_");
        return snapshot.build();
    }
}