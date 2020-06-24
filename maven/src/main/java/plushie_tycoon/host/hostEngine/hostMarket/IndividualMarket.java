package plushie_tycoon.host.hostEngine.hostMarket;
import plushie_tycoon.host.hostEngine.hostMarket.buyer.BuyerBase;
import plushie_tycoon.host.hostEngine.hostMarket.buyer.FixedBuyer;
import plushie_tycoon.host.hostEngine.hostMarket.buyer.LinearBuyer;
import plushie_tycoon.host.hostEngine.hostMarket.buyer.ConsolidatedBuyer;
import plushie_tycoon.host.hostEngine.hostMarket.seller.FixedSeller;
import plushie_tycoon.host.hostEngine.hostMarket.seller.LinearSeller;
import plushie_tycoon.host.hostEngine.hostMarket.seller.ConsolidatedSeller;
import plushie_tycoon.host.hostEngine.hostMarket.seller.SellerBase;

import java.util.HashMap;

//todo: Eventually we can have player buyers and sellers having different behaviour, for now they just send in
// quantity, and get current price out. So it's essentially a devoted budget.
public class IndividualMarket {
    double current_price;
    HashMap<String, Integer> playerBuyers;
    HashMap<String, Integer> playerSellers;

    public IndividualMarket(double price) {
        current_price = price;
        playerBuyers = new HashMap<>();
        playerSellers = new HashMap<>();
    }

    public double get() {
        return current_price;
    }

    public void addBuyer(String userid, int quantity){
        playerBuyers.put(userid, quantity);
    }

    public void addSeller(String userid, int quantity){
        playerSellers.put(userid, quantity);
    }

    public double clearMarket(){
        HashMap<String, BuyerBase> buyers = new HashMap<>();
        buyers.put("init", new LinearBuyer());
        for (HashMap.Entry<String, Integer> entry: playerBuyers.entrySet()){
            buyers.put(entry.getKey(), new FixedBuyer(entry.getValue()));
        }
        HashMap<String, SellerBase> sellers = new HashMap<>();
        sellers.put("init", new LinearSeller());
        for (HashMap.Entry<String, Integer> entry: playerSellers.entrySet()){
            sellers.put(entry.getKey(), new FixedSeller(entry.getValue()));
        }

        ConsolidatedBuyer conBuy = new ConsolidatedBuyer(buyers);
        ConsolidatedSeller conSell = new ConsolidatedSeller(sellers);
        ClearingHouse house = new ClearingHouse(conBuy, conSell);
        current_price = house.clear();
        return current_price;
    }

    public void set(double price) {
        current_price = price;
    }
}
