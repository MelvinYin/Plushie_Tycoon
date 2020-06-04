package plushie_tycoon.serverService.config;

import plushie_tycoon.serverService.config.baseObjects.BaseObjects;
import plushie_tycoon.serverService.config.baseObjects.Products;
import plushie_tycoon.serverService.config.baseObjects.Resources;

import java.util.HashMap;

public class Defaults {
    private static int numResources = Resources.values().length;
    public static HashMap<Integer, Integer> resourceRatio = new HashMap<>();
    public static HashMap<Products, Integer> productionHours = new HashMap<>();
    public static int costPerHour;
    public static HashMap<BaseObjects, Integer> volumes = new HashMap<>();
    public static HashMap<BaseObjects, Integer> weights = new HashMap<>();

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

        costPerHour = 3;

        volumes.put(Resources.CLOTH, 5);
        volumes.put(Resources.STUFFING, 6);
        volumes.put(Resources.ACCESSORY, 7);
        volumes.put(Resources.PACKAGING, 8);
        volumes.put(Products.AISHA, 3);
        volumes.put(Products.BETA, 2);
        volumes.put(Products.CHAMA, 4);

        weights.put(Resources.CLOTH, 5);
        weights.put(Resources.STUFFING, 6);
        weights.put(Resources.ACCESSORY, 7);
        weights.put(Resources.PACKAGING, 8);
        weights.put(Products.AISHA, 3);
        weights.put(Products.BETA, 2);
        weights.put(Products.CHAMA, 4);
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
    public static int getVolume(BaseObjects baseObject){
        return volumes.get(baseObject);
    }
    public static int getWeight(BaseObjects baseObject){
        return weights.get(baseObject);
    }
}
