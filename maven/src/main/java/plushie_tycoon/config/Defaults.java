package plushie_tycoon.config;

import plushie_tycoon.config.baseObjects.BaseObjects;
import plushie_tycoon.config.baseObjects.Products;
import plushie_tycoon.config.baseObjects.Resources;

import java.util.HashMap;

public class Defaults {
    private static int numResources = Resources.values().length;
    public static HashMap<Integer, Integer> resourceRatio = new HashMap<>();
    public static HashMap<Products, Integer> productionHours = new HashMap<>();
    public static double costPerHour;
    public static HashMap<BaseObjects, Double> volumes = new HashMap<>();
    public static HashMap<BaseObjects, Double> weights = new HashMap<>();

    static {
        resourceRatio.put(getHashKey(Products.AISHA, Resources.CLOTH), 3);
        resourceRatio.put(getHashKey(Products.AISHA, Resources.STUFFING), 6);
        resourceRatio.put(getHashKey(Products.AISHA, Resources.ACCESSORY), 2);
        resourceRatio.put(getHashKey(Products.AISHA, Resources.PACKAGING), 1);

        resourceRatio.put(getHashKey(Products.BETA, Resources.CLOTH), 1);
        resourceRatio.put(getHashKey(Products.BETA, Resources.STUFFING), 4);
        resourceRatio.put(getHashKey(Products.BETA, Resources.ACCESSORY), 1);
        resourceRatio.put(getHashKey(Products.BETA, Resources.PACKAGING), 2);

        resourceRatio.put(getHashKey(Products.CHAMA, Resources.CLOTH), 2);
        resourceRatio.put(getHashKey(Products.CHAMA, Resources.STUFFING), 5);
        resourceRatio.put(getHashKey(Products.CHAMA, Resources.ACCESSORY), 1);
        resourceRatio.put(getHashKey(Products.CHAMA, Resources.PACKAGING), 4);

        productionHours.put(Products.AISHA, 30);
        productionHours.put(Products.BETA, 24);
        productionHours.put(Products.CHAMA, 36);

        costPerHour = 0.3;

        volumes.put(Resources.CLOTH, 0.5);
        volumes.put(Resources.STUFFING, 0.6);
        volumes.put(Resources.ACCESSORY, 0.7);
        volumes.put(Resources.PACKAGING, 0.8);
        volumes.put(Products.AISHA, 0.3);
        volumes.put(Products.BETA, 0.2);
        volumes.put(Products.CHAMA, 0.4);

        weights.put(Resources.CLOTH, 0.5);
        weights.put(Resources.STUFFING, 0.6);
        weights.put(Resources.ACCESSORY, 0.7);
        weights.put(Resources.PACKAGING, 0.8);
        weights.put(Products.AISHA, 0.3);
        weights.put(Products.BETA, 0.2);
        weights.put(Products.CHAMA, 0.4);
    }

    private static int getHashKey(Products product, Resources resource){
        return product.ordinal() * numResources + resource.ordinal();
    }

    public static int getResourceRatio(Products product, Resources resource){
        return resourceRatio.get(getHashKey(product, resource));
    }
    public static int getProductionHours(Products product){
        return productionHours.get(product);
    }
    public static double getVolume(BaseObjects baseObject){
        return volumes.get(baseObject);
    }
    public static double getWeight(BaseObjects baseObject){
        return weights.get(baseObject);
    }
}
