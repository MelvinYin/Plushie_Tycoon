package plushie_tycoon.serverService.geLocal;
import plushie_tycoon.serverService.config.baseObjects.BaseObjects;
import plushie_tycoon.serverService.config.baseObjects.Products;
import plushie_tycoon.serverService.config.baseObjects.Resources;

import plushie_tycoon.serverService.config.Defaults;
import plushie_tycoon.serverService.config.Initials;
import plushie_tycoon.serverService.geLocal.inventory.LocalInventory;
import plushie_tycoon.serverService.geLocal.market.LocalMarket;
import plushie_tycoon.Grpc.*;
import plushie_tycoon.serverService.utils.BaseStringConverter;

public class GELocal {
    private StateHistory history;
    private double budget;
    private LocalMarket market;
    private LocalInventory localInventory;
    private int time;

    public GELocal(){
        history = new StateHistory();
        market = new LocalMarket();
        budget = Initials.budget;
        localInventory = new LocalInventory(Initials.quantities);
        time = Initials.time;
    }

    public void commit(){
        history.addBudget(budget);
        history.addTime(time);
        history.addInventory(localInventory);
        history.addMarket(market);
        time++;
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
        return getUpdateReturn();
    }
    public Snapshot sell(BaseObjects object, int quantity){
        if (localInventory.get(object) < quantity){
            String errorMsg = "Cannot sell <" + quantity + "> of <" + object + "> as you only have <"
                    + localInventory.get(object) + ">.";
            return getNullReturn(errorMsg);
        }
        localInventory.sub(object, quantity);
        double price = market.get(object) * quantity;
        budget += price;
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
        return getUpdateReturn();
    }
    public Snapshot next(){
        budget -= localInventory.getTotalMoveCost();
        budget -= localInventory.getTotalStorageCost();
        localInventory.resetMovement();
        commit();
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