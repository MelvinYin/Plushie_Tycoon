package plushie_tycoon.local.localEngine.inventory;
import java.util.HashMap;

import plushie_tycoon.config.baseObjects.BaseObjects;
import plushie_tycoon.config.Defaults;

public class LocalInventory {
    private HashMap<BaseObjects, Integer> inventory;
    private HashMap<BaseObjects, Integer> movements;

    public LocalInventory(HashMap<BaseObjects, Integer> inventory){
        this.inventory = inventory;
        this.movements = new HashMap<>();
    }

    public LocalInventory(){
        this(new HashMap<>());
    }

    public double getTotalMoveCost() {
        double costs = 0;
        for (HashMap.Entry<BaseObjects, Integer> entry : this.movements.entrySet()) {
            if (entry.getValue() > 0){
                costs += InventoryCalculator.getMoveInCost(entry.getKey()) * entry.getValue();
            } else {
                costs += InventoryCalculator.getMoveOutCost(entry.getKey()) * entry.getValue();
            }
        }
        return costs;
    }

    public double getTotalStorageCost() {
        int costs = 0;
        for (HashMap.Entry<BaseObjects, Integer> entry : this.inventory.entrySet()) {
            costs += InventoryCalculator.getStorageCost(entry.getKey()) * entry.getValue();
        }
        return costs;
    }

    public double getTotalWeight() {
        int weight = 0;
        for (HashMap.Entry<BaseObjects, Integer> entry : this.inventory.entrySet()) {
            weight += Defaults.getWeight(entry.getKey()) * entry.getValue();
        }
        return weight;
    }

    public double getTotalVolume() {
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

    public double getMoveInCost(BaseObjects item) {
        return InventoryCalculator.getMoveInCost(item);
    }

    public double getMoveOutCost(BaseObjects item) {
        return InventoryCalculator.getMoveOutCost(item);
    }

    public double getStorageCost(BaseObjects item) {
        return InventoryCalculator.getStorageCost(item);
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

    public void set(BaseObjects item, int quantity){
        inventory.put(item, quantity);
    }

    public int get(BaseObjects item){
        return inventory.get(item);
    }

}

