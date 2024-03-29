package plushie_tycoon.host.hostEngine.production;

import plushie_tycoon.config.Defaults;
import plushie_tycoon.host.hostEngine.UserData;
import plushie_tycoon.config.baseObjects.Products;
import plushie_tycoon.config.baseObjects.Resources;

public class Production {
    public void make(Products product, int quantity, UserData userdata){
        for (Resources resource: Resources.values()){
            int resourceQ = Defaults.getResourceRatio(product, resource) * quantity;
            userdata.inventory.put(resource, userdata.inventory.get(resource) -resourceQ);
        }
        userdata.inventory.put(product, userdata.inventory.get(product) -quantity);
        double cost = Defaults.getProductionHours(product) * quantity * Defaults.costPerHour;
        userdata.budget -= cost;
    }
}
