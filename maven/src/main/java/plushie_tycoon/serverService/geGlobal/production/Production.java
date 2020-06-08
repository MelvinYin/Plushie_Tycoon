package plushie_tycoon.serverService.geGlobal.production;

import org.graalvm.compiler.lir.LIRInstruction;
import plushie_tycoon.serverService.config.Defaults;
import plushie_tycoon.serverService.geGlobal.UserData;
import plushie_tycoon.serverService.config.baseObjects.BaseObjects;
import plushie_tycoon.serverService.config.baseObjects.Products;
import plushie_tycoon.serverService.config.baseObjects.Resources;

import java.util.HashMap;

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
