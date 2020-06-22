package plushie_tycoon.client.clientEngine.clientInventory;

import plushie_tycoon.config.baseObjects.BaseObjects;
import plushie_tycoon.config.Defaults;
import plushie_tycoon.config.stats.MoveInCost;
import plushie_tycoon.config.stats.MoveOutCost;
import plushie_tycoon.config.stats.StoreCost;


public class InventoryCalculator {
    int tier = 0; // unimplemented for now

    public static double getStorageCost(BaseObjects item) {
        double cost = 0;
        cost += StoreCost.getWeight() * Defaults.getWeight(item);
        cost += StoreCost.getVolume() * Defaults.getVolume(item);
        assert cost >= 0;
        return cost;
    }

    public static double getMoveInCost(BaseObjects item) {
        double cost = 0;
        cost += MoveInCost.getWeight() * Defaults.getWeight(item);
        cost += MoveInCost.getVolume() * Defaults.getVolume(item);
        assert cost >= 0;
        return cost;
    }
    public static double getMoveOutCost(BaseObjects item) {
        double cost = 0;
        cost += MoveOutCost.getWeight() * Defaults.getWeight(item);
        cost += MoveOutCost.getVolume() * Defaults.getVolume(item);
        assert cost >= 0;
        return cost;
    }
}
