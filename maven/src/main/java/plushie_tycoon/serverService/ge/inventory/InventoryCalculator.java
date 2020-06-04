package plushie_tycoon.serverService.ge.inventory;

import plushie_tycoon.serverService.config.baseObjects.BaseObjects;
import plushie_tycoon.serverService.config.Defaults;
import plushie_tycoon.serverService.config.stats.MoveInCost;
import plushie_tycoon.serverService.config.stats.MoveOutCost;
import plushie_tycoon.serverService.config.stats.StoreCost;


public class InventoryCalculator {
    int tier = 0; // unimplemented for now

    public static int getStorageCost(BaseObjects item) {
        int cost = 0;
        cost += StoreCost.getWeight() * Defaults.getWeight(item);
        cost += StoreCost.getVolume() * Defaults.getVolume(item);
        assert cost >= 0;
        return cost;
    }

    public static int getMoveInCost(BaseObjects item) {
        int cost = 0;
        cost += MoveInCost.getWeight() * Defaults.getWeight(item);
        cost += MoveInCost.getVolume() * Defaults.getVolume(item);
        assert cost >= 0;
        return cost;
    }
    public static int getMoveOutCost(BaseObjects item) {
        int cost = 0;
        cost += MoveOutCost.getWeight() * Defaults.getWeight(item);
        cost += MoveOutCost.getVolume() * Defaults.getVolume(item);
        assert cost >= 0;
        return cost;
    }
}
