package plushie_tycoon.serverService.ge;
import plushie_tycoon.serverService.config.baseObjects.BaseObjects;
import plushie_tycoon.serverService.config.baseObjects.Products;
import plushie_tycoon.serverService.config.baseObjects.Resources;

import java.util.HashMap;
import java.util.ArrayList;
import plushie_tycoon.serverService.config.Defaults;
import plushie_tycoon.serverService.config.Initials;
import plushie_tycoon.serverService.ge.inventory.GlobalInventory;
import plushie_tycoon.serverService.ge.market.GlobalMarket;
import plushie_tycoon.Grpc.*;
import plushie_tycoon.serverService.utils.BaseStringConverter;

//todo: add data retrieval method for UI to update after every call
//todo: convert it to sql eventually? For GS



public class GE {
    private StateHistory history;
    private int budget;
    private GlobalMarket market;
    private GlobalInventory inventory;
    private int time;

    public GE(){
        history = new StateHistory();
        market = new GlobalMarket();
        budget = Initials.budget;
        inventory = new GlobalInventory(Initials.quantities);
        time = Initials.time;
    }

    public int getMoveInCost(BaseObjects object, int quantity){
        return inventory.getMoveInCost(object) * quantity;
    }
    public int getMoveOutCost(BaseObjects object, int quantity){
        return inventory.getMoveOutCost(object) * quantity;
    }
    public int getStorageCost(){
        return inventory.getTotalStorageCost();
    }

    public void add(BaseObjects object, int quantity){
        inventory.add(object, quantity);
    }
    public void addBudget(int quantity){
        budget += quantity;
    }
    public void addTime(){
        time++;
    }
    public void sub(BaseObjects object, int quantity){
        inventory.sub(object, quantity);
    }
    public void subBudget(int quantity){
        budget -= quantity;
    }

    public void commit(){
        history.addBudget(budget);
        history.addTime(time);
        history.addInventory(inventory);
        history.addMarket(market);
        time++;
    }

    public boolean canReverseCall(){
        return !history.isEmpty();
    }
    public void reverseCall(){
        budget = history.getBudget();
        time = history.getTime();
        inventory = history.getInventory();
        market = history.getMarket();
        history.pop();
    }

    public Snapshot buy(BaseObjects object, int quantity){
        int price = market.get(object) * quantity;
        System.out.println("Buying " + object.toString() + " " + quantity + " price " + price +" budget " + budget);
        if (price > budget){
            String errorMsg = "Cannot buy <" + quantity + "> of <" + object + "> as it costs <" + price +
                    "> and budget is <" + budget + ">.";
            return getNullReturn(errorMsg);
        }
        inventory.add(object, quantity);
        budget -= price;
        return getUpdateReturn();
    }
    public Snapshot sell(BaseObjects object, int quantity){
        if (inventory.get(object) < quantity){
            String errorMsg = "Cannot sell <" + quantity + "> of <" + object + "> as you only have <"
                    + inventory.get(object) + ">.";
            return getNullReturn(errorMsg);
        }
        inventory.sub(object, quantity);
        int price = market.get(object) * quantity;
        budget += price;
        return getUpdateReturn();
    }

    public boolean canMake(Products product, int quantity){
        for (Resources resource: Resources.values()){
            if (Defaults.getResourceRatio(product, resource) * quantity > inventory.get(resource)){
                return false;
            }
        }
        return true;
    }

    public Snapshot make(BaseObjects object, int quantity){
        Products product = (Products) object;
        if (!canMake(product, quantity)){
            String errorMsg = "Cannot make <" + quantity + "> of <" + product + "> as you only have <"
                    + inventory.get(product) + ">.";
            return getNullReturn(errorMsg);
        }
        inventory.add(product, quantity);
        for (Resources resource: Resources.values()){
            inventory.sub(resource, quantity * Defaults.getResourceRatio(product, resource));
        }
        return getUpdateReturn();
    }
    public Snapshot next(){
        budget -= inventory.getTotalMoveCost();
        budget -= inventory.getTotalStorageCost();
        inventory.resetMovement();
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


    private Snapshot getUpdateReturnnew(){
        Snapshot.Builder snapshot = Snapshot.newBuilder();
//        prices
        for (Products base: Products.values()){
            String baseString = BaseStringConverter.convert(base);
            snapshot.putPrices(baseString, market.get(base));
            snapshot.putQuantities(baseString, inventory.get(base));
            snapshot.putWeights(baseString, Defaults.getWeight(base));
            snapshot.putVolumes(baseString, Defaults.getVolume(base));

            mItemCost.Builder itemcost = mItemCost.newBuilder();
            itemcost.setMovein(inventory.getMoveInCost(base));
            itemcost.setMoveout(inventory.getMoveOutCost(base));
            itemcost.setStorage(inventory.getStorageCost(base));
            snapshot.putItemCost(baseString, itemcost.build());
        }

        for (Resources base: Resources.values()){
            String baseString = BaseStringConverter.convert(base);
            snapshot.putPrices(baseString, market.get(base));
            snapshot.putQuantities(baseString, inventory.get(base));
            snapshot.putWeights(baseString, Defaults.getWeight(base));
            snapshot.putVolumes(baseString, Defaults.getVolume(base));

            mItemCost.Builder itemcost = mItemCost.newBuilder();
            itemcost.setMovein(inventory.getMoveInCost(base));
            itemcost.setMoveout(inventory.getMoveOutCost(base));
            itemcost.setStorage(inventory.getStorageCost(base));
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

    private Snapshot getUpdateReturn(){
        int addition = 1;

        String[] resources = {"cloth", "stuffing", "accessories", "packaging"};
        String[] products = {"aisha", "beta", "chama"};
        String[] bases = new String[resources.length + products.length];
        System.arraycopy(resources, 0, bases, 0, resources.length);
        System.arraycopy(products, 0, bases, resources.length, products.length);

        Snapshot.Builder snapshot = Snapshot.newBuilder();
//        prices
        int count = 0;
        for (String base: bases){
            snapshot.putPrices(base, 10+count+addition);
            count++;
        }

//        quantities
        count = 0;
        for (String base: bases){
            snapshot.putQuantities(base, 20+count+addition);
            count++;
        }

        //        weights
        count = 0;
        for (String base: bases){
            snapshot.putWeights(base, 0.1+count*0.01+addition*0.01);
            count++;
        }

        //        volumes
        count = 0;
        for (String base: bases){
            snapshot.putVolumes(base, 0.2+count*0.01+addition*0.01);
            count++;
        }

        //        item_cost
        count = 0;
        for (String base: bases){
            mItemCost.Builder itemcost = mItemCost.newBuilder();
            itemcost.setMovein(0.3+count*0.01+addition*0.01);
            itemcost.setMoveout(0.4+count*0.01+addition*0.01);
            itemcost.setStorage(0.5+count*0.01+addition*0.01);
            snapshot.putItemCost(base, itemcost.build());
            count++;
        }

        //        resource_ratio
        count = 0;

        for (String product: products){
            mRatioPerProduct.Builder ratioPerProduct = mRatioPerProduct.newBuilder();
            for (String resource: resources){
                ratioPerProduct.putRatio(resource, 1+count);
                count++;
            }
            snapshot.putResourceRatio(product, ratioPerProduct.build());
        }

        snapshot.setTime(1);
        snapshot.setAction("update");
        snapshot.setBudget(100000 + addition);
        snapshot.setConsoleOutput("console_");
        return snapshot.build();
    }
}


/*
*
class GE:
    def __init__(self):
        GS_dataclass = GSConstructor()
        GS_dataclass.load_init()
        assert GS_dataclass.is_complete()
        self.GS = GSM(GS_dataclass)
        self.GS.commit(call=dict(command=Func.start))
        self.callback = self._default_callback
        self.func_map = self.get_func_map()
        self.text = ""

    def return_data(self):
        return self.GS.return_data()

    def return_data_for_ui(self):
        return self.GS.return_data_for_ui()

    def _default_callback(self, call):
        func_signal = call['command']
        func = self.func_map[func_signal]
        try:
            return_value = func(call)
        except InsufficientQuantityError:
            self.GS.reverse_call()
            log("InsufficientQuantityError\n\n", inspect.currentframe())
            raise RepeatUIAction
        GS_update = self.GS.return_data_for_ui()
        # log("GE Call: {}\n Return: {}".format(call, GS_update),
        #     inspect.currentframe())
        return GS_update, return_value

    def buy(self, call):
        self.GS.commit(call=call)
        category = call['category']
        quantity = call['quantity']
        self.text += f"Buy: {category} x {quantity}\n"
        self.GS.buy('inventory', category, quantity)
        movein_cost = self.GS.movein_cost(category, quantity)
        price = self.GS.get('market', category)
        total_cost = price * quantity + movein_cost
        self.GS.sub('budget', 'budget', total_cost)
        return 'update'

    def sell(self, call):
        self.GS.commit(call=call)
        category = call['category']
        quantity = call['quantity']
        self.GS.sell('inventory', category, quantity)
        moveout_cost = self.GS.moveout_cost(category, quantity)
        price = self.GS.get('market', category)
        total_cost = price * quantity - moveout_cost
        self.GS.add('budget', 'budget', total_cost)
        return 'update'

    def make(self, call):
        self.GS.commit(call=call)
        category = call['category']
        quantity = call['quantity']
        cost = 0
        production_cost, materials = self.GS.get('production', category)
        cost += production_cost * quantity
        for _category, material in materials.items():
            self.GS.sub('inventory', _category, material * quantity)
            moveout_cost = self.GS.moveout_cost(_category, material * quantity)
            cost += moveout_cost
        movein_cost = self.GS.movein_cost(category, quantity)
        cost += movein_cost
        self.GS.sub('budget', 'budget', cost)
        self.GS.make('inventory', category, quantity)
        return 'update'

    def quit(self, call):
        sys.exit()

    def get_func_map(self):
        mapping = dict()
        mapping[Func.buy] = self.buy
        mapping[Func.sell] = self.sell
        mapping[Func.quit] = self.quit
        mapping[Func.make] = self.make
        mapping[Func.save] = self.save
        mapping[Func.load] = self.load
        mapping[Func.next] = self.next_turn
        mapping[Func.back] = self.back
        return mapping

    def next_turn(self, call):
        storage_cost = self.GS.storage_cost()
        self.GS.sub('budget', 'budget', storage_cost)
        ret_value = self.GS.next_turn()
        self.GS.commit(call=call)
        return ret_value

    def back(self, call):
        ret_value = self.GS.reverse_call()
        if not ret_value:
            log("No previous action logged.", inspect.currentframe())
            return 'pause'
        return 'update'

    def copy(self):
        return copy.deepcopy(self)

    def save(self, call):
        self.GS.commit(call)
        GS_dataclass = self.GS.return_data()
        with open(save_folder + save_file_name, "wb") as file:
            pickle.dump(GS_dataclass, file, -1)
        return 'pause'

    def load(self, call):
        with open(save_folder + save_file_name, "rb") as file:
            GS_dataclass = pickle.load(file)
        self.GS = GSM(GS_dataclass)
        self.GS.commit(call)
        return 'update'


* */