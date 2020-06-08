package plushie_tycoon.serverService.geGlobal.market.seller;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class ConsolidatedSeller extends SellerBase{
    List<SellerBase> sellers;
    public ConsolidatedSeller(List<SellerBase> sellers){
        this.sellers = sellers;
    }
    public ConsolidatedSeller(Map<String, SellerBase> buyerMap){
        sellers = new ArrayList<>();
        for (Map.Entry<String, SellerBase> entry: buyerMap.entrySet()){
            sellers.add(entry.getValue());
        }
    }

    public int sell(double price){
        int quantity = 0;
        for (SellerBase seller: this.sellers){
            quantity += seller.sell(price);
        }
        return quantity;
    }
}
