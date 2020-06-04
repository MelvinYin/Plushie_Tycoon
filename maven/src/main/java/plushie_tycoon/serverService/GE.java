package plushie_tycoon.serverService;

import plushie_tycoon.serverService.config.baseObjects.BaseObjects;
import plushie_tycoon.serverService.config.baseObjects.Products;
import plushie_tycoon.serverService.gs.GS;
import plushie_tycoon.Grpc;

import java.util.ArrayList;
import plushie_tycoon.Grpc.Snapshot;

//todo: add data retrieval method for UI to update after every call
//todo: convert it to sql eventually? For GS



public class GE {
    private GS gs;
    private int curr_count;
    private int curr_sign;

    public GE(){
        gs = new GS();
        curr_count = 0;
        curr_sign = -1;
    }

    public Snapshot buy(BaseObjects object, int quantity){
        boolean returnCode = gs.buy(object, quantity);
        Snapshot output = Snapshot.newBuilder().build();
        if (!returnCode){
            return output;
        }
        return gs.returnData();
    }
    public Snapshot sell(BaseObjects object, int quantity){
        boolean returnCode = gs.sell(object, quantity);
        Snapshot output = Snapshot.newBuilder().build();
        if (!returnCode){
            return output;
        }
        return gs.returnData();
    }

    public Snapshot make(Products product, int quantity){
        boolean returnCode = gs.make(product, quantity);
        Snapshot output = Snapshot.newBuilder().build();
        if (!returnCode){
            return output;
        }
        return output;
    }
    public Snapshot next(Products product, int quantity){
        Snapshot output = Snapshot.newBuilder().build();
        return output;
    }
    public Snapshot save(Products product, int quantity){
        Snapshot output = Snapshot.newBuilder().build();
        return output;
    }

    public Snapshot load(Products product, int quantity){
        Snapshot output = Snapshot.newBuilder().build();
        return output;
    }

    public Snapshot back(Products product, int quantity){
        Snapshot output = Snapshot.newBuilder().build();
        return output;
    }
    public Snapshot quit(Products product, int quantity){
        Snapshot output = Snapshot.newBuilder().build();
        return output;
    }

    public Snapshot init(Products product, int quantity){
        Snapshot output = Snapshot.newBuilder().build();
        return output;
    }



    public ArrayList<String> returnData(){
        return gs.returnData();
    }

    private Grpc.Snapshot getReturn(String action){
        curr_count++;
        curr_sign *= -1;
        int addition = curr_count * curr_sign;

        String[] resources = {"cloth", "stuffing", "accessories", "packaging"};
        String[] products = {"aisha", "beta", "chama"};
        String[] bases = new String[resources.length + products.length];
        System.arraycopy(resources, 0, bases, 0, resources.length);
        System.arraycopy(products, 0, bases, resources.length, products.length);

        Grpc.Snapshot.Builder Snapshot = Grpc.Snapshot.newBuilder();
//        prices
        int count = 0;
        for (String base: bases){
            Snapshot.putPrices(base, 10+count+addition);
            count++;
        }

//        quantities
        count = 0;
        for (String base: bases){
            Snapshot.putQuantities(base, 20+count+addition);
            count++;
        }

        //        weights
        count = 0;
        for (String base: bases){
            Snapshot.putWeights(base, 0.1+count*0.01+addition*0.01);
            count++;
        }

        //        volumes
        count = 0;
        for (String base: bases){
            Snapshot.putVolumes(base, 0.2+count*0.01+addition*0.01);
            count++;
        }

        //        item_cost
        count = 0;
        for (String base: bases){
            Grpc.mItemCost.Builder itemcost = Grpc.mItemCost.newBuilder();
            itemcost.setMovein(0.3+count*0.01+addition*0.01);
            itemcost.setMoveout(0.4+count*0.01+addition*0.01);
            itemcost.setStorage(0.5+count*0.01+addition*0.01);
            Snapshot.putItemCost(base, itemcost.build());
            count++;
        }

        //        resource_ratio
        count = 0;

        for (String product: products){
            Grpc.mRatioPerProduct.Builder ratioPerProduct = Grpc.mRatioPerProduct.newBuilder();
            for (String resource: resources){
                ratioPerProduct.putRatio(resource, 1+count);
                count++;
            }
            Snapshot.putResourceRatio(product, ratioPerProduct.build());
        }

        Snapshot.setTime(1);
        Snapshot.setAction(action);
        Snapshot.setBudget(100000 + addition);
        Snapshot.setConsoleOutput("console_");
        return Snapshot.build();
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