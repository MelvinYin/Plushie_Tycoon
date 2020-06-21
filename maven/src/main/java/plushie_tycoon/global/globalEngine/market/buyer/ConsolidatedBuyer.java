package plushie_tycoon.global.globalEngine.market.buyer;

import java.util.ArrayList;
import java.util.Map;
import java.util.List;

public class ConsolidatedBuyer extends BuyerBase{
    List<BuyerBase> buyers;
    public ConsolidatedBuyer(List<BuyerBase> buyers){
        this.buyers = buyers;
    }
    public ConsolidatedBuyer(Map<String, BuyerBase> buyerMap){
        buyers = new ArrayList<>();
        for (Map.Entry<String, BuyerBase> entry: buyerMap.entrySet()){
            buyers.add(entry.getValue());
        }
    }
    public int buy(double price){
        int quantity = 0;
        for (BuyerBase buyer: this.buyers){
            quantity += buyer.buy(price);
        }
        return quantity;
    }
}
