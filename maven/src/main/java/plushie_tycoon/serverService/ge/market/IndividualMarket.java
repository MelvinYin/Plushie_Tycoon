package plushie_tycoon.serverService.ge.market;
import plushie_tycoon.serverService.ge.market.buyer.BuyerBase;
import plushie_tycoon.serverService.ge.market.buyer.FixedBuyer;
import plushie_tycoon.serverService.ge.market.buyer.LinearBuyer;
import plushie_tycoon.serverService.ge.market.buyer.ConsolidatedBuyer;
import plushie_tycoon.serverService.ge.market.seller.FixedSeller;
import plushie_tycoon.serverService.ge.market.seller.LinearSeller;
import plushie_tycoon.serverService.ge.market.seller.ConsolidatedSeller;
import plushie_tycoon.serverService.ge.market.seller.SellerBase;

public class IndividualMarket {
    int current_price;

    public IndividualMarket(int price) {
        current_price = price;
    }

    public int get() {
        return current_price;
    }

    public int clearMarket(int buy_q, int sell_q){
        BuyerBase[] buyers = new BuyerBase[2];
        buyers[0] = new FixedBuyer(buy_q);
        buyers[1] = new LinearBuyer();
        SellerBase[] sellers = new SellerBase[2];
        sellers[0] = new FixedSeller(buy_q);
        sellers[1] = new LinearSeller();
        ConsolidatedBuyer conBuy = new ConsolidatedBuyer(buyers);
        ConsolidatedSeller conSell = new ConsolidatedSeller(sellers);
        ClearingHouse house = new ClearingHouse(conBuy, conSell);
        current_price = house.clear();
        return current_price;
    }

    public void set(int price) {
        current_price = price;
    }
}
