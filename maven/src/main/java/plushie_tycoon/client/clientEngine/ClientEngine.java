package plushie_tycoon.client.clientEngine;
import plushie_tycoon.config.baseObjects.BaseObjects;
import plushie_tycoon.config.baseObjects.Products;
import plushie_tycoon.config.baseObjects.Resources;

import plushie_tycoon.config.Defaults;
import plushie_tycoon.config.Initials;
import plushie_tycoon.client.ClientPageService;
import plushie_tycoon.client.clientEngine.clientInventory.ClientInventory;
import plushie_tycoon.client.clientEngine.clientMarket.ClientMarket;
import plushie_tycoon.Grpc.*;
import plushie_tycoon.utils.BaseStringConverter;

import java.util.Random;

import java.util.HashMap;
import io.grpc.Server;
import io.grpc.ServerBuilder;

import java.io.IOException;

public class ClientEngine {
    private StateHistory history;
    private double budget;
    private ClientMarket market;
    private ClientInventory ClientInventory;
    public String userid;
    private int time;
    public HashMap<BaseObjects, Integer> buySellTracker;
    public HashMap<BaseObjects, Integer> makeTracker;
    int serverPortno;
    int webPagePortno;
    ClientPageService clientPageService;
    ToHost toHost;
    boolean needUpdate;

    public ClientEngine(int webPagePortno, int serverPortno){
        history = new StateHistory();
        market = new ClientMarket(Initials.prices);
        budget = Initials.budget;
        ClientInventory = new ClientInventory(Initials.quantities);
        time = Initials.time;
        buySellTracker = new HashMap<>();
        makeTracker = new HashMap<>();
        Random random = new Random();
        userid = String.valueOf(random.nextInt());
        toHost = new ToHost(serverPortno);
        this.serverPortno = serverPortno;
        this.webPagePortno = webPagePortno;
        clientPageService = new ClientPageService(this);
        needUpdate = false;
    }

    public void initFromGlobalServer(){
        toHost.waitForReady(10);
        Snapshot initSnapshot = toHost.register(userid);
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
        history.addInventory(ClientInventory);
        history.addMarket(market);
    }

    public boolean canReverseCall(){
        return !history.isEmpty();
    }

    public void reverseCall(){
        budget = history.getBudget();
        time = history.getTime();
        ClientInventory = history.getClientInventory();
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
        ClientInventory.add(object, quantity);
        budget -= price;
        commit();
        buySellTracker.put(object, buySellTracker.getOrDefault(object, 0) + quantity);
        return getUpdateReturn();
    }
    public Snapshot sell(BaseObjects object, int quantity){
        if (ClientInventory.get(object) < quantity){
            String errorMsg = "Cannot sell <" + quantity + "> of <" + object + "> as you only have <"
                    + ClientInventory.get(object) + ">.";
            return getNullReturn(errorMsg);
        }
        ClientInventory.sub(object, quantity);
        budget += market.get(object) * quantity;
        commit();
        buySellTracker.put(object, buySellTracker.getOrDefault(object, 0) - quantity);
        return getUpdateReturn();
    }

    public boolean canMake(Products product, int quantity){
        for (Resources resource: Resources.values()){
            if (Defaults.getResourceRatio(product, resource) * quantity > ClientInventory.get(resource)){
                return false;
            }
        }
        return true;
    }

    public Snapshot make(BaseObjects object, int quantity){
        Products product = (Products) object;
        if (!canMake(product, quantity)){
            String errorMsg = "Cannot make <" + quantity + "> of <" + product + "> as you only have <"
                    + ClientInventory.get(product) + ">.";
            return getNullReturn(errorMsg);
        }
        ClientInventory.add(product, quantity);
        for (Resources resource: Resources.values()){
            ClientInventory.sub(resource, quantity * Defaults.getResourceRatio(product, resource));
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
        }
        for (Products product: Products.values()){
            changes.putBuySell(BaseStringConverter.convert(product), buySellTracker.getOrDefault(product, 0));
            changes.putMake(BaseStringConverter.convert(product), makeTracker.getOrDefault(product, 0));
        }
        toHost.send(changes.build());
        budget -= ClientInventory.getTotalMoveCost();
        budget -= ClientInventory.getTotalStorageCost();
        ClientInventory.resetMovement();
        time++;
        needUpdate = true;
        return getUpdateReturn();
    }

    public Snapshot updateFromHost() {
        if (needUpdate){
            needUpdate = false;
            return getUpdateReturn();
        } else {
            return Snapshot.newBuilder().build();
        }
    }

    public boolean checkIfNextTurn(){
        int serverTime = toHost.getTime();
        if (serverTime == time){
            return false;
        }
        Snapshot newData = toHost.query(userid);
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
            ClientInventory.set(base, snapshot.getQuantitiesOrThrow(baseString));
        }
        for (Products base: Products.values()){
            String baseString = BaseStringConverter.convert(base);
            market.set(base, snapshot.getPricesOrThrow(baseString));
            ClientInventory.set(base, snapshot.getQuantitiesOrThrow(baseString));
        }
        history.reset();
        buySellTracker.clear();
        makeTracker.clear();
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
            snapshot.putQuantities(baseString, ClientInventory.get(base));
            snapshot.putWeights(baseString, Defaults.getWeight(base));
            snapshot.putVolumes(baseString, Defaults.getVolume(base));

            mItemCost.Builder itemcost = mItemCost.newBuilder();
            itemcost.setMovein(ClientInventory.getMoveInCost(base));
            itemcost.setMoveout(ClientInventory.getMoveOutCost(base));
            itemcost.setStorage(ClientInventory.getStorageCost(base));
            snapshot.putItemCost(baseString, itemcost.build());
        }

        for (Resources base: Resources.values()){
            String baseString = BaseStringConverter.convert(base);
            snapshot.putPrices(baseString, market.get(base));
            snapshot.putQuantities(baseString, ClientInventory.get(base));
            snapshot.putWeights(baseString, Defaults.getWeight(base));
            snapshot.putVolumes(baseString, Defaults.getVolume(base));

            mItemCost.Builder itemcost = mItemCost.newBuilder();
            itemcost.setMovein(ClientInventory.getMoveInCost(base));
            itemcost.setMoveout(ClientInventory.getMoveOutCost(base));
            itemcost.setStorage(ClientInventory.getStorageCost(base));
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