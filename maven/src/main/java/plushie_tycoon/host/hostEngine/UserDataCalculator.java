package plushie_tycoon.host.hostEngine;

import plushie_tycoon.config.baseObjects.BaseObjects;
import plushie_tycoon.host.hostEngine.inventory.InventoryCalculator;

import java.util.HashMap;

public class UserDataCalculator {

    UserDataCalculator(){
    }

    public void updateParameters(){
    }

    public void updateUserData(UserData original, HashMap<BaseObjects, Integer> movements, double budgetChange){
        double movementCost = 0;
        double storageCost = 0;
        for (HashMap.Entry<BaseObjects, Integer> entry: movements.entrySet()){
            if (entry.getValue() > 0){
                movementCost += InventoryCalculator.getMoveInCost(entry.getKey()) * entry.getValue();
            } else {
                movementCost += InventoryCalculator.getMoveOutCost(entry.getKey()) * entry.getValue();
                original.inventory.put(entry.getKey(), original.inventory.get(entry.getKey()) - entry.getValue());
            }
        }
        for (HashMap.Entry<BaseObjects, Integer> entry: original.inventory.entrySet()){
            storageCost += InventoryCalculator.getStorageCost(entry.getKey()) * entry.getValue();
        }
        for (HashMap.Entry<BaseObjects, Integer> entry: movements.entrySet()) {
            if (entry.getValue() > 0) {
                original.inventory.put(entry.getKey(), original.inventory.get(entry.getKey()) + entry.getValue());
            }
            original.budget -= budgetChange;
            original.budget -= movementCost;
            original.budget -= storageCost;
        }
    }
}
