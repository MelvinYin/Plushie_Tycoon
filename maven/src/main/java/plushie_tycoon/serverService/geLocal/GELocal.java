package plushie_tycoon.serverService.geLocal;
import plushie_tycoon.config.baseObjects.BaseObjects;
import plushie_tycoon.config.baseObjects.Products;
import plushie_tycoon.config.baseObjects.Resources;

import plushie_tycoon.config.Defaults;
import plushie_tycoon.config.Initials;
import plushie_tycoon.serverService.geLocal.inventory.LocalInventory;
import plushie_tycoon.serverService.geLocal.market.LocalMarket;
import plushie_tycoon.Grpc.*;
import plushie_tycoon.serverService.utils.BaseStringConverter;
import java.util.Random;

import java.util.HashMap;

public class GELocal {
    private StateHistory history;
    private double budget;
    private LocalMarket market;
    private LocalInventory localInventory;
    public String userid;
    private int time;
    public HashMap<BaseObjects, Integer> buySellTracker;
    public HashMap<BaseObjects, Integer> makeTracker;
    int clientPortno;
//    CallStack(){
//
//    }
//
//    public void buy(BaseObjects category, Integer quantity){
//        buySell.put(category, buySell.getOrDefault(category, 0) + quantity);
//    }
//    public void sell(BaseObjects category, Integer quantity){
//        buySell.put(category, buySell.getOrDefault(category, 0) - quantity);
//    }
//    public void make(BaseObjects category, Integer quantity){
//        make.put(category, make.getOrDefault(category, 0) + quantity);
//    }

    public GELocal(int clientPortno){
        history = new StateHistory();
        market = new LocalMarket();
        budget = Initials.budget;
        localInventory = new LocalInventory(Initials.quantities);
        time = Initials.time;
        buySellTracker = new HashMap<>();
        makeTracker = new HashMap<>();
        Random random = new Random();
        userid = String.valueOf(random.nextInt());
        this.clientPortno = clientPortno;
        LocalServer.register(clientPortno, userid);
    }

    public void commit(){
        history.addBudget(budget);
        history.addTime(time);
        history.addInventory(localInventory);
        history.addMarket(market);
    }

    public boolean canReverseCall(){
        return !history.isEmpty();
    }

    public void reverseCall(){
        budget = history.getBudget();
        time = history.getTime();
        localInventory = history.getLocalInventory();
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
        localInventory.add(object, quantity);
        budget -= price;
        commit();
        buySellTracker.put(object, buySellTracker.getOrDefault(object, 0) + quantity);
        return getUpdateReturn();
    }
    public Snapshot sell(BaseObjects object, int quantity){
        if (localInventory.get(object) < quantity){
            String errorMsg = "Cannot sell <" + quantity + "> of <" + object + "> as you only have <"
                    + localInventory.get(object) + ">.";
            return getNullReturn(errorMsg);
        }
        localInventory.sub(object, quantity);
        budget += market.get(object) * quantity;
        commit();
        buySellTracker.put(object, buySellTracker.getOrDefault(object, 0) - quantity);
        return getUpdateReturn();
    }

    public boolean canMake(Products product, int quantity){
        for (Resources resource: Resources.values()){
            if (Defaults.getResourceRatio(product, resource) * quantity > localInventory.get(resource)){
                return false;
            }
        }
        return true;
    }

    public Snapshot make(BaseObjects object, int quantity){
        Products product = (Products) object;
        if (!canMake(product, quantity)){
            String errorMsg = "Cannot make <" + quantity + "> of <" + product + "> as you only have <"
                    + localInventory.get(product) + ">.";
            return getNullReturn(errorMsg);
        }
        localInventory.add(product, quantity);
        for (Resources resource: Resources.values()){
            localInventory.sub(resource, quantity * Defaults.getResourceRatio(product, resource));
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
        LocalServer.send(clientPortno, changes.build());
        budget -= localInventory.getTotalMoveCost();
        budget -= localInventory.getTotalStorageCost();
        localInventory.resetMovement();
        time++;
//        commit();
        return getUpdateReturn();
    }

    public boolean checkIfNextTurn(){
        int serverTime = LocalServer.getTime(clientPortno);
        if (serverTime == time){
            return false;
        }
        Snapshot newData = LocalServer.query(clientPortno, userid);
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
            localInventory.set(base, snapshot.getQuantitiesOrThrow(baseString));
        }
        for (Products base: Products.values()){
            String baseString = BaseStringConverter.convert(base);
            market.set(base, snapshot.getPricesOrThrow(baseString));
            localInventory.set(base, snapshot.getQuantitiesOrThrow(baseString));
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
            snapshot.putQuantities(baseString, localInventory.get(base));
            snapshot.putWeights(baseString, Defaults.getWeight(base));
            snapshot.putVolumes(baseString, Defaults.getVolume(base));

            mItemCost.Builder itemcost = mItemCost.newBuilder();
            itemcost.setMovein(localInventory.getMoveInCost(base));
            itemcost.setMoveout(localInventory.getMoveOutCost(base));
            itemcost.setStorage(localInventory.getStorageCost(base));
            snapshot.putItemCost(baseString, itemcost.build());
        }

        for (Resources base: Resources.values()){
            String baseString = BaseStringConverter.convert(base);
            snapshot.putPrices(baseString, market.get(base));
            snapshot.putQuantities(baseString, localInventory.get(base));
            snapshot.putWeights(baseString, Defaults.getWeight(base));
            snapshot.putVolumes(baseString, Defaults.getVolume(base));

            mItemCost.Builder itemcost = mItemCost.newBuilder();
            itemcost.setMovein(localInventory.getMoveInCost(base));
            itemcost.setMoveout(localInventory.getMoveOutCost(base));
            itemcost.setStorage(localInventory.getStorageCost(base));
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