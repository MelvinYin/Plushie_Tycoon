package plushie_tycoon.serverService.geGlobal;

import com.sun.org.apache.xpath.internal.operations.Bool;
import plushie_tycoon.Grpc;
import plushie_tycoon.serverService.config.Defaults;
import plushie_tycoon.serverService.config.baseObjects.BaseObjects;
import plushie_tycoon.serverService.config.baseObjects.Resources;
import plushie_tycoon.serverService.config.baseObjects.Products;
import plushie_tycoon.serverService.geGlobal.market.GlobalMarket;
import plushie_tycoon.serverService.geGlobal.production.Production;
import plushie_tycoon.serverService.utils.BaseStringConverter;
import plushie_tycoon.serverService.geLocal.inventory.InventoryCalculator;

import java.util.HashMap;

public class GEGlobal {
    int time = 0;
    public HashMap<String, UserData> userDatas;
    public HashMap<String, Boolean> hasUpdated;
    public HashMap<BaseObjects, HashMap<String, Integer>> buySellOrders;
    public HashMap<BaseObjects, HashMap<String, Integer>> makeOrders;
    private UserDataCalculator userDataCalculator;
    private GlobalMarket market;
    private Production production;
    GEGlobal(){
        userDatas = new HashMap<>();
        hasUpdated = new HashMap<>();
        buySellOrders = new HashMap<>();
        makeOrders = new HashMap<>();
        market = new GlobalMarket();
        userDataCalculator = new UserDataCalculator();
        production = new Production();

        for (Resources resource: Resources.values()){
            buySellOrders.put(resource, new HashMap<>());
            makeOrders.put(resource, new HashMap<>());
        }
        for (Products product: Products.values()){
            buySellOrders.put(product, new HashMap<>());
            makeOrders.put(product, new HashMap<>());
        }
    }

    public void nextTurn(){
        hasUpdated.replaceAll((k, v) -> false);
        time++;
//        supposed to put in your movement_cost, etc here to update.
        userDataCalculator.updateParameters();
        for (HashMap.Entry<BaseObjects, HashMap<String, Integer>> perItem: buySellOrders.entrySet()){
            BaseObjects base = perItem.getKey();
            for (HashMap.Entry<String, Integer> entry: perItem.getValue().entrySet()){
                market.sendOrder(entry.getKey(), base, entry.getValue());
            }
        }
        for (HashMap.Entry<BaseObjects, HashMap<String, Integer>> perItem: makeOrders.entrySet()){
            Products base = (Products) perItem.getKey();
            for (HashMap.Entry<String, Integer> entry: perItem.getValue().entrySet()){
                production.make(base, entry.getValue(), userDatas.get(entry.getKey()));
            }
        }
        market.clearMarket();
        for (HashMap.Entry<String, UserData> perUser: userDatas.entrySet()){
            String userid = perUser.getKey();
            userDataCalculator.updateUserData(
                    perUser.getValue(), market.getProcessedOrders(userid), market.getBudgetChanges(userid));
        }
    }

    public Grpc.ReturnCode addCall(String userid, HashMap<BaseObjects, Integer> buySellOrder,
                                   HashMap<BaseObjects, Integer> makeOrder){
        for (HashMap.Entry<BaseObjects, Integer> entry: buySellOrder.entrySet()){
            buySellOrders.get(entry.getKey()).put(userid, entry.getValue());
        }
        for (HashMap.Entry<BaseObjects, Integer> entry: makeOrder.entrySet()){
            makeOrders.get(entry.getKey()).put(userid, entry.getValue());
        }
        Grpc.ReturnCode output = Grpc.ReturnCode.newBuilder().build();
        hasUpdated.put(userid, true);
        return output;
    }

    public int getTime(){
        return this.time;
    }

    public Grpc.Snapshot query(String userid){
        return buildSnapshot(userid);
    }

    public Grpc.Snapshot register(String userid){
        userDatas.put(userid, new UserData());
        hasUpdated.put(userid, false);
        return buildSnapshot(userid);
    }

    public boolean isRegistered(String userid){
        return userDatas.containsKey(userid);
    }

    public boolean hasUpdate(String userid){
        return hasUpdated.get(userid);
    }

    private Grpc.Snapshot buildSnapshot(String userid){
        Grpc.Snapshot.Builder snapshot = Grpc.Snapshot.newBuilder();

//        User-specific information
        UserData thisUser = userDatas.get(userid);

        for (Products base: Products.values()) {
            snapshot.putQuantities(BaseStringConverter.convert(base), thisUser.inventory.get(base));
        }
        for (Resources base: Resources.values()) {
            snapshot.putQuantities(BaseStringConverter.convert(base), thisUser.inventory.get(base));
        }
        snapshot.setBudget(thisUser.budget);

        //        Generic Information

        for (Products base: Products.values()){
            String baseString = BaseStringConverter.convert(base);
            snapshot.putPrices(baseString, market.get(base));
            snapshot.putWeights(baseString, Defaults.getWeight(base));
            snapshot.putVolumes(baseString, Defaults.getVolume(base));

            Grpc.mItemCost.Builder itemcost = Grpc.mItemCost.newBuilder();
            itemcost.setMovein(InventoryCalculator.getMoveInCost(base));
            itemcost.setMoveout(InventoryCalculator.getMoveOutCost(base));
            itemcost.setStorage(InventoryCalculator.getStorageCost(base));
            snapshot.putItemCost(baseString, itemcost.build());
        }

        for (Resources base: Resources.values()){
            String baseString = BaseStringConverter.convert(base);
            snapshot.putPrices(baseString, market.get(base));
            snapshot.putWeights(baseString, Defaults.getWeight(base));
            snapshot.putVolumes(baseString, Defaults.getVolume(base));

            Grpc.mItemCost.Builder itemcost = Grpc.mItemCost.newBuilder();
            itemcost.setMovein(InventoryCalculator.getMoveInCost(base));
            itemcost.setMoveout(InventoryCalculator.getMoveOutCost(base));
            itemcost.setStorage(InventoryCalculator.getStorageCost(base));
            snapshot.putItemCost(baseString, itemcost.build());
        }

        for (Products product: Products.values()){
            String productString = BaseStringConverter.convert(product);
            Grpc.mRatioPerProduct.Builder ratioPerProduct = Grpc.mRatioPerProduct.newBuilder();
            for (Resources resource: Resources.values()){
                String resourceString = BaseStringConverter.convert(resource);
                ratioPerProduct.putRatio(resourceString, Defaults.getResourceRatio(product, resource));
            }
            snapshot.putResourceRatio(productString, ratioPerProduct.build());
        }
        snapshot.setTime(time);
        return snapshot.build();
    }
}

