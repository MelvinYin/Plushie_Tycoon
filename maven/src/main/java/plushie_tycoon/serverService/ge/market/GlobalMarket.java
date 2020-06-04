package plushie_tycoon.serverService.ge.market;

import plushie_tycoon.serverService.config.baseObjects.BaseObjects;
import plushie_tycoon.serverService.config.Initials;

import java.util.HashMap;

/** Does not have external setting capabilities unless value explicitly called. */
public class GlobalMarket {
    HashMap<BaseObjects, IndividualMarket> indMarkets;
    public GlobalMarket(HashMap<BaseObjects, Integer> market_values){
        this.indMarkets = this.spawnMarkets(market_values);
    }
    public GlobalMarket(){
        this.indMarkets = this.spawnMarkets(Initials.prices);
    }
    public HashMap<BaseObjects, IndividualMarket> spawnMarkets(HashMap<BaseObjects, Integer> values) {
        HashMap<BaseObjects, IndividualMarket> ind_markets = new HashMap<>();
        for (HashMap.Entry<BaseObjects, Integer> entry: values.entrySet()) {
            IndividualMarket ind_market = new IndividualMarket(entry.getValue());
            ind_markets.put(entry.getKey(), ind_market);
        }
        return ind_markets;
    }
    public void setValues(HashMap<BaseObjects, Integer> values){
        for (HashMap.Entry<BaseObjects, Integer> entry: values.entrySet()) {
            this.indMarkets.get(entry.getKey()).set(entry.getValue());
        }
    }
    public HashMap<BaseObjects, Integer> returnValues(){
        HashMap<BaseObjects, Integer> output = new HashMap<>();
        for (HashMap.Entry<BaseObjects, IndividualMarket> entry: this.indMarkets.entrySet()) {
            output.put(entry.getKey(), entry.getValue().get());
        }
        return output;
    }

    public int get(BaseObjects key){
        return indMarkets.get(key).get();
    }

    /** assumed callstack already collapsed. this should be organised by category => action => quantity */
    public void clearMarket(HashMap<BaseObjects, HashMap<String, Integer>> callstack){
        for (HashMap.Entry<BaseObjects, HashMap<String, Integer>> entry: callstack.entrySet()) {
            BaseObjects category = entry.getKey();
            HashMap<String, Integer> remainder = entry.getValue();
            int buy_q = remainder.get("buy");
            int sell_q = remainder.get("sell");
            this.indMarkets.get(category).clearMarket(buy_q, sell_q);
        }
    }
}
