package plushie_tycoon.serverService.geLocal.market;

import plushie_tycoon.config.baseObjects.BaseObjects;
import plushie_tycoon.config.Initials;

import java.util.HashMap;

/** Does not have external setting capabilities unless value explicitly called. */
public class LocalMarket {
    HashMap<BaseObjects, Double> indMarkets;

    public LocalMarket(HashMap<BaseObjects, Double> market_values){
        this.indMarkets = market_values;
    }

    public LocalMarket(){
        this.indMarkets = Initials.prices;
    }

    public void set(BaseObjects key, double price){
        indMarkets.put(key, price);
    }

    public HashMap<BaseObjects, Double> returnValues(){
        return indMarkets;
    }

    public double get(BaseObjects key){
        return indMarkets.get(key);
    }
}
