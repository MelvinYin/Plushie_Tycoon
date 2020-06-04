package plushie_tycoon.serverService.gs.inventory;
import java.util.HashMap;

import plushie_tycoon.serverService.config.baseObjects.BaseObjects;
import plushie_tycoon.serverService.config.Defaults;

public class GlobalInventory {
    private HashMap<BaseObjects, Integer> inventory;
    private HashMap<BaseObjects, Integer> movements;

    public GlobalInventory(HashMap<BaseObjects, Integer> inventory){
        this.inventory = inventory;
        this.movements = new HashMap<>();
    }

    public GlobalInventory(){
        this.inventory = new HashMap<>();
        this.movements = new HashMap<>();
    }

    public int getTotalMoveCost() {
        int costs = 0;
        for (HashMap.Entry<BaseObjects, Integer> entry : this.movements.entrySet()) {
            if (entry.getValue() > 0){
                costs += InventoryCalculator.getMoveInCost(entry.getKey()) * entry.getValue();
            } else {
                costs += InventoryCalculator.getMoveOutCost(entry.getKey()) * entry.getValue();
            }
        }
        return costs;
    }

    public HashMap<BaseObjects, Integer> getMoveCostSplit() {
        HashMap<BaseObjects, Integer> costs = new HashMap<>();
        for (HashMap.Entry<BaseObjects, Integer> entry : this.movements.entrySet()) {
            if (entry.getValue() > 0){
                costs.put(entry.getKey(), InventoryCalculator.getMoveInCost(entry.getKey()) * entry.getValue());
            } else {
                costs.put(entry.getKey(), InventoryCalculator.getMoveOutCost(entry.getKey()) * entry.getValue());
            }
        }
        return costs;
    }

    public HashMap<BaseObjects, Integer> getStorageCostSplit() {
        HashMap<BaseObjects, Integer> costs = new HashMap<>();
        for (HashMap.Entry<BaseObjects, Integer> entry : this.inventory.entrySet()) {
            costs.put(entry.getKey(), InventoryCalculator.getStorageCost(entry.getKey()) * entry.getValue());
        }
        return costs;
    }

    public int getTotalStorageCost() {
        int costs = 0;
        for (HashMap.Entry<BaseObjects, Integer> entry : this.inventory.entrySet()) {
            costs += InventoryCalculator.getStorageCost(entry.getKey()) * entry.getValue();
        }
        return costs;
    }

    public int getTotalWeight() {
        int weight = 0;
        for (HashMap.Entry<BaseObjects, Integer> entry : this.inventory.entrySet()) {
            weight += Defaults.getWeight(entry.getKey()) * entry.getValue();
        }
        return weight;
    }

    public int getTotalVolume() {
        int volume = 0;
        for (HashMap.Entry<BaseObjects, Integer> entry : this.inventory.entrySet()) {
            volume += Defaults.getVolume(entry.getKey()) * entry.getValue();
        }
        return volume;
    }

    public void resetMovement() {
        this.movements = new HashMap<>();
    }

    public HashMap<BaseObjects, Integer> getInventory() {
        return this.inventory;
    }

    public HashMap<BaseObjects, Integer> getMovements() {
        return this.movements;
    }

    public int getMoveInCost(BaseObjects item) {
        return InventoryCalculator.getMoveInCost(item);
    }

    public int getMoveOutCost(BaseObjects item) {
        return InventoryCalculator.getMoveOutCost(item);
    }

    public void add(BaseObjects item, int quantity){
        if (this.inventory.containsKey(item)){
            inventory.put(item, inventory.get(item) + quantity);
        } else {
            inventory.put(item, quantity);
        }
    }

    public void sub(BaseObjects item, int quantity){
        if (this.inventory.containsKey(item)){
            inventory.put(item, inventory.get(item) - quantity);
        } else {
            inventory.put(item, -quantity);
        }
    }

    public void replace(BaseObjects item, int quantity){
        inventory.put(item, quantity);
    }

    public int get(BaseObjects item){
        return inventory.get(item);
    }

}

