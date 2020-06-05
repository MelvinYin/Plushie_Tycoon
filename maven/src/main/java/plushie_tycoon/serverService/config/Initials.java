package plushie_tycoon.serverService.config;

import plushie_tycoon.serverService.config.baseObjects.BaseObjects;
import plushie_tycoon.serverService.config.baseObjects.Products;
import plushie_tycoon.serverService.config.baseObjects.Resources;

import java.util.HashMap;

public class Initials {
    private static int numResources = Resources.values().length;
    public static HashMap<BaseObjects, Integer> quantities = new HashMap<>();
    public static HashMap<BaseObjects, Double> prices = new HashMap<>();
    public static double budget;
    public static int time;

    static {
        quantities.put(Resources.CLOTH, 1001);
        quantities.put(Resources.STUFFING, 1002);
        quantities.put(Resources.ACCESSORY, 1003);
        quantities.put(Resources.PACKAGING, 1004);

        quantities.put(Products.AISHA, 10);
        quantities.put(Products.BETA, 11);
        quantities.put(Products.CHAMA, 12);

        prices.put(Resources.CLOTH, 10.);
        prices.put(Resources.STUFFING, 20.);
        prices.put(Resources.ACCESSORY, 18.);
        prices.put(Resources.PACKAGING, 12.);

        prices.put(Products.AISHA, 102.);
        prices.put(Products.BETA, 103.);
        prices.put(Products.CHAMA, 104.);
        budget = 1000002.;
        time = 12;
    }

    private static int getHashKey(Products product, Resources resource){
        return product.ordinal() * numResources + resource.ordinal();
    }
    public static int getQuantity(BaseObjects baseObject){
        return quantities.get(baseObject);
    }
    public static double getPrices(BaseObjects baseObject){
        return prices.get(baseObject);
    }
}
