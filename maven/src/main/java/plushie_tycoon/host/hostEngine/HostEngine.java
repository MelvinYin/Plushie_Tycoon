package plushie_tycoon.host.hostEngine;

import io.grpc.Server;
import io.grpc.ServerBuilder;
import plushie_tycoon.Grpc;
import plushie_tycoon.config.Defaults;
import plushie_tycoon.config.baseObjects.BaseObjects;
import plushie_tycoon.config.baseObjects.Resources;
import plushie_tycoon.config.baseObjects.Products;
import plushie_tycoon.host.hostEngine.hostServices.AdminPageService;
import plushie_tycoon.host.hostEngine.hostServices.ClientToHostService;
import plushie_tycoon.host.hostEngine.hostMarket.HostMarket;
import plushie_tycoon.host.hostEngine.production.Production;
import plushie_tycoon.utils.BaseStringConverter;
import plushie_tycoon.host.hostEngine.inventory.InventoryCalculator;
import plushie_tycoon.Grpc.ProposedChanges;

import java.util.concurrent.Executors;
import java.util.concurrent.locks.ReentrantLock;
import java.io.IOException;
import java.util.HashMap;
import java.util.Stack;

//todo: concern about nextTurn getting called but orderStack is not empty...? Maybe add a check and a warning if
// this is so, when nextTurn is called.

public class HostEngine {
    int time = 0;
    final HashMap<String, UserData> userDatas;
    final HashMap<String, Boolean> hasUpdated;
    final HashMap<BaseObjects, HashMap<String, Integer>> buySellOrders;
    final HashMap<Products, HashMap<String, Integer>> makeOrders;
    final UserDataCalculator userDataCalculator;
    final HostMarket market;
    final Production production;
    final AdminPageService adminService;
    final ClientToHostService serverService;
    final int portno;
    final ReentrantLock lockOrderStack;
    final Stack<ProposedChanges> orderStack;

    public HostEngine(int portno){
        userDatas = new HashMap<>();
        hasUpdated = new HashMap<>();
        buySellOrders = new HashMap<>();
        makeOrders = new HashMap<>();
        market = new HostMarket();
        userDataCalculator = new UserDataCalculator();
        production = new Production();
        serverService = new ClientToHostService(this);
        adminService = new AdminPageService(this);
        this.portno = portno;
        orderStack = new Stack<>();
        lockOrderStack = new ReentrantLock(true);

        for (Resources resource: Resources.values()){
            buySellOrders.put(resource, new HashMap<>());
        }
        for (Products product: Products.values()){
            buySellOrders.put(product, new HashMap<>());
            makeOrders.put(product, new HashMap<>());
        }
    }

    public void runServices()  throws IOException, InterruptedException {
        ServerBuilder builder = ServerBuilder.forPort(portno).executor(Executors.newFixedThreadPool(4));
        builder.addService(serverService).addService(adminService);
        Server server = builder.build();
        server.start();
        server.awaitTermination();
    }

    public void lockOrderStack(){
        lockOrderStack.tryLock();
    }

    public void unlockOrderStack(){
        lockOrderStack.unlock();
    }

    public int nextTurn(){
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
        for (HashMap.Entry<Products, HashMap<String, Integer>> perItem: makeOrders.entrySet()){
            for (HashMap.Entry<String, Integer> entry: perItem.getValue().entrySet()){
                production.make(perItem.getKey(), entry.getValue(), userDatas.get(entry.getKey()));
            }
        }
        market.clearMarket();
        System.out.println(market);
        System.out.println(market.processedOrders);
        for (HashMap.Entry<String, UserData> perUser: userDatas.entrySet()){
            String userid = perUser.getKey();
            userDataCalculator.updateUserData(
                    perUser.getValue(), market.getProcessedOrders(userid), market.getBudgetChanges(userid));
        }
        orderStack.clear();
        return time;
    }

    public Grpc.ReturnCode addCall(String userid, HashMap<BaseObjects, Integer> buySellOrder,
                                   HashMap<Products, Integer> makeOrder){
        lockOrderStack.tryLock();
        lockOrderStack.unlock();
        for (HashMap.Entry<BaseObjects, Integer> entry: buySellOrder.entrySet()){
            buySellOrders.get(entry.getKey()).put(userid, entry.getValue());
        }
        for (HashMap.Entry<Products, Integer> entry: makeOrder.entrySet()){
            makeOrders.get(entry.getKey()).put(userid, entry.getValue());
        }
        Grpc.ReturnCode output = Grpc.ReturnCode.newBuilder().build();
        hasUpdated.put(userid, true);
        orderStack.push(formatChanges(userid, buySellOrder, makeOrder));
        return output;
    }

    public ProposedChanges getCall(){
        if (orderStack.empty()){
            return ProposedChanges.newBuilder().setUserid("").build();
        }
        return orderStack.pop();
    }

    ProposedChanges formatChanges(String userid, HashMap<BaseObjects, Integer> buySellOrder,
                                          HashMap<Products, Integer> makeOrder){
        Grpc.ProposedChanges.Builder changes = ProposedChanges.newBuilder();
        changes.setUserid(userid);
        for (HashMap.Entry<BaseObjects, Integer> entry: buySellOrder.entrySet()){
            String baseString = entry.getKey().toString();
            changes.putBuySell(baseString, entry.getValue());
        }
        for (HashMap.Entry<Products, Integer> entry: makeOrder.entrySet()){
            String baseString = entry.getKey().toString();
            changes.putMake(baseString, entry.getValue());
        }
        return changes.build();
    }

    public int getTime(){
        return this.time;
    }

    public boolean orderStackIsEmpty() {
        return orderStack.empty();
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

    public boolean hasUpdated(String userid){
        return hasUpdated.get(userid);
    }

    Grpc.Snapshot buildSnapshot(String userid){
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

