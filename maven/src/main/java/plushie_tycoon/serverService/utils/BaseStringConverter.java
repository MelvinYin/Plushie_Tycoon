package plushie_tycoon.serverService.utils;

import plushie_tycoon.serverService.config.baseObjects.BaseObjects;
import plushie_tycoon.serverService.config.baseObjects.Products;
import plushie_tycoon.serverService.config.baseObjects.Resources;

import java.util.HashMap;
import java.util.Map;

public class BaseStringConverter {
    static HashMap<String, BaseObjects> strToBase;
    static HashMap<BaseObjects, String> baseToString;
    static {
        strToBase = new HashMap<>();
        strToBase.put("stuffing", Resources.STUFFING);
        strToBase.put("accessory", Resources.ACCESSORY);
        strToBase.put("packaging", Resources.PACKAGING);
        strToBase.put("cloth", Resources.CLOTH);
        strToBase.put("aisha", Products.AISHA);
        strToBase.put("beta", Products.BETA);
        strToBase.put("chama", Products.CHAMA);

        baseToString = new HashMap<>();
        for (Map.Entry<String, BaseObjects> entry: strToBase.entrySet()){
            baseToString.put(entry.getValue(), entry.getKey());
        }
    }

    public static String convert(BaseObjects base){
        return baseToString.get(base);
    }

    public static BaseObjects convert(String base){
        return strToBase.get(base);
    }
}
