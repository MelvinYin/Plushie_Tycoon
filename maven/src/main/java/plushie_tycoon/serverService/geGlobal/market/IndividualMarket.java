package plushie_tycoon.serverService.geGlobal.market;
import plushie_tycoon.serverService.geGlobal.market.buyer.BuyerBase;
import plushie_tycoon.serverService.geGlobal.market.buyer.FixedBuyer;
import plushie_tycoon.serverService.geGlobal.market.buyer.LinearBuyer;
import plushie_tycoon.serverService.geGlobal.market.buyer.ConsolidatedBuyer;
import plushie_tycoon.serverService.geGlobal.market.seller.FixedSeller;
import plushie_tycoon.serverService.geGlobal.market.seller.LinearSeller;
import plushie_tycoon.serverService.geGlobal.market.seller.ConsolidatedSeller;
import plushie_tycoon.serverService.geGlobal.market.seller.SellerBase;

public class IndividualMarket {
    double current_price;

    public IndividualMarket(double price) {
        current_price = price;
    }

    public double get() {
        return current_price;
    }

    public double clearMarket(int buy_q, int sell_q){
        BuyerBase[] buyers = new BuyerBase[2];
        buyers[0] = new FixedBuyer(buy_q);
        buyers[1] = new LinearBuyer();
        SellerBase[] sellers = new SellerBase[2];
        sellers[0] = new FixedSeller(sell_q);
        sellers[1] = new LinearSeller();
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
