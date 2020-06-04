package plushie_tycoon.serverService.gs;
import plushie_tycoon.serverService.config.baseObjects.BaseObjects;
import plushie_tycoon.serverService.config.baseObjects.Products;
import plushie_tycoon.serverService.config.baseObjects.Resources;

import java.util.HashMap;
import java.util.ArrayList;
import plushie_tycoon.serverService.config.Defaults;
import plushie_tycoon.serverService.config.Initials;
import plushie_tycoon.serverService.gs.inventory.GlobalInventory;
import plushie_tycoon.serverService.gs.market.GlobalMarket;


//todo: add market changes
public class GS {
    private GSHistory history;
    private int budget;
    private GlobalMarket market;
    private GlobalInventory inventory;
    private int time;

    public GS(){
        history = new GSHistory();
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

    public boolean buy(BaseObjects object, int quantity){
        int price = market.get(object) * quantity;
        System.out.println("Buying " + object.toString() + " " + quantity + " price " + price +" budget " + budget);
        if (price > budget){
            return false;
        }
        inventory.add(object, quantity);
        budget -= price;
        return true;
    }

    public boolean sell(BaseObjects object, int quantity){
        if (inventory.get(object) < quantity){
            return false;
        }
        inventory.sub(object, quantity);
        int price = market.get(object) * quantity;
        budget += price;
        return true;
    }

    public boolean canMake(Products product, int quantity){
        for (Resources resource: Resources.values()){
            if (Defaults.getResourceRatio(product, resource) * quantity > inventory.get(resource)){
                return false;
            }
        }
        return true;
    }

    public boolean make(Products product, int quantity){
        if (!canMake(product, quantity)){
            return false;
        }
        inventory.add(product, quantity);
        for (Resources resource: Resources.values()){
            inventory.sub(resource, quantity * Defaults.getResourceRatio(product, resource));
        }
        return true;
    }

    public void nextTurn(){
        budget -= inventory.getTotalMoveCost();
        budget -= inventory.getTotalStorageCost();
        inventory.resetMovement();
        commit();
    }

    public ArrayList<String> returnData(){
        ArrayList<String> output = new ArrayList<>();
        output.add("budget,"+budget);
        output.add("time,"+time);
        for (HashMap.Entry<BaseObjects, Integer> entry : inventory.getInventory().entrySet()){
            output.add(entry.getKey().toString() + "," + entry.getValue().toString());
        }
        for (HashMap.Entry<BaseObjects, Integer> entry : market.returnValues().entrySet()){
            output.add(entry.getKey().toString() + "_price,"+entry.getValue().toString());
        }
        return output;
    }
}

/*



 */