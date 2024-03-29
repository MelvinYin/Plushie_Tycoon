package plushie_tycoon.host.hostEngine.hostMarket;

import plushie_tycoon.Grpc;
import plushie_tycoon.config.baseObjects.BaseObjects;
import plushie_tycoon.config.Initials;
import plushie_tycoon.config.baseObjects.Products;
import plushie_tycoon.config.baseObjects.Resources;
import plushie_tycoon.utils.FillBaseHashMap;

import java.util.HashMap;

/** Does not have external setting capabilities unless value explicitly called. */
public class HostMarket {
    HashMap<BaseObjects, IndividualMarket> indMarkets;
    HashMap<BaseObjects, HashMap<String, Integer>> orders;
    public HashMap<String, HashMap<BaseObjects, Integer>> processedOrders;
    HashMap<String, Double> budgetChanges;

    public HostMarket(HashMap<BaseObjects, Double> market_values){
        indMarkets = this.spawnMarkets(market_values);
        orders = FillBaseHashMap.with(new HashMap<>());
        processedOrders = new HashMap<>();
        budgetChanges = new HashMap<>();
    }

    public HostMarket(){
        this(Initials.prices);
    }

    public void sendOrder(String userid, BaseObjects base, int quantity){
        orders.get(base).put(userid, quantity);
    }

    public void clearMarket() {
        HashMap<BaseObjects, Double> originalPrices = new HashMap<>();
        HashMap<BaseObjects, Double> prices = new HashMap<>();
        BaseObjects base;
        for (HashMap.Entry<BaseObjects, IndividualMarket> indMarketEntry : indMarkets.entrySet()) {
            base = indMarketEntry.getKey();
            IndividualMarket market = indMarketEntry.getValue();
            originalPrices.put(base, market.get());
            for (HashMap.Entry<String, Integer> entry : orders.get(base).entrySet()) {
                if (entry.getValue() > 0) {
                    market.addBuyer(entry.getKey(), entry.getValue());
                } else if (entry.getValue() < 0) {
                    market.addSeller(entry.getKey(), entry.getValue());
                }
            }
            prices.put(base, market.clearMarket());
        }

        for (HashMap.Entry<BaseObjects, HashMap<String, Integer>> orderEntry : orders.entrySet()) {
            base = orderEntry.getKey();
            for (HashMap.Entry<String, Integer> entry : orderEntry.getValue().entrySet()) {
                String userid = entry.getKey();
                int quantity = entry.getValue();
                double previous = budgetChanges.getOrDefault(userid, 0.);
                if ((quantity > 0) & (originalPrices.get(base) > prices.get(base))) {
                    double originalBudget = quantity * originalPrices.get(base);
                    quantity = (int) (originalBudget / prices.get(base));
                }
                budgetChanges.put(userid, previous - quantity * prices.get(base));
                if (!processedOrders.containsKey(userid)){
                    processedOrders.put(userid, FillBaseHashMap.with(0));
                }
                processedOrders.get(userid).put(base, quantity);
            }
        }
    }

    public HashMap<String, Double> getBudgetChanges(){
        return budgetChanges;
    }

    public double getBudgetChanges(String userid){
        return budgetChanges.get(userid);
    }

    public HashMap<String, HashMap<BaseObjects, Integer>> getProcessedOrders(){
        return processedOrders;
    }


    public HashMap<BaseObjects, Integer> getProcessedOrders(String userid){
        if (!processedOrders.containsKey(userid)){
            processedOrders.put(userid, FillBaseHashMap.with(0));
        }
        return processedOrders.get(userid);
    }

    public HashMap<BaseObjects, IndividualMarket> spawnMarkets(HashMap<BaseObjects, Double> values) {
        HashMap<BaseObjects, IndividualMarket> ind_markets = new HashMap<>();
        for (HashMap.Entry<BaseObjects, Double> entry: values.entrySet()) {
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

    public HashMap<BaseObjects, Double> returnValues(){
        HashMap<BaseObjects, Double> output = new HashMap<>();
        for (HashMap.Entry<BaseObjects, IndividualMarket> entry: this.indMarkets.entrySet()) {
            output.put(entry.getKey(), entry.getValue().get());
        }
        return output;
    }

    public double get(BaseObjects key){
        return indMarkets.get(key).get();
    }

}
