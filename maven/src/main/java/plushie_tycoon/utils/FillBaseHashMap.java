package plushie_tycoon.utils;

import plushie_tycoon.config.baseObjects.BaseObjects;
import plushie_tycoon.config.baseObjects.Resources;
import plushie_tycoon.config.baseObjects.Products;

import java.util.HashMap;

public class FillBaseHashMap {
    public static < E > HashMap<BaseObjects, E> with(E element){
        HashMap<BaseObjects, E> hashmap = new HashMap<>();
        for (Resources base: Resources.values()){
            hashmap.put(base, element);
        }
        for (Products base: Products.values()){
            hashmap.put(base, element);
        }
        return hashmap;
    }
}
