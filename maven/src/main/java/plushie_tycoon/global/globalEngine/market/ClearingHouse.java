package plushie_tycoon.global.globalEngine.market;
import plushie_tycoon.global.globalEngine.market.buyer.BuyerBase;
import plushie_tycoon.global.globalEngine.market.seller.SellerBase;
import java.util.List;
import java.util.Arrays;

public class ClearingHouse {
    private double priceResolution = 0.1;
    private BuyerBase buyer;
    private SellerBase seller;

    public ClearingHouse(BuyerBase buyer, SellerBase seller){
        this.buyer = buyer;
        this.seller = seller;
    }

    public ClearingHouse (SellerBase seller, BuyerBase buyer){
        this(buyer, seller);
    }

    public int clear() {
        int current_price = 0;
        List<String> past = Arrays.asList("low", "low", "low");
        while (true) {
            int buyer_q = this.buyer.buy(current_price);
            int seller_q = this.seller.sell(current_price);
            if (past.get(0).equals(past.get(2)) & !(past.get(0).equals(past.get(1)))){
                break;
            }
            if (buyer_q == seller_q){
                break;
            } else if (buyer_q > seller_q){
                current_price += priceResolution;
                past.remove(0);
                past.add("low");
            } else {
                current_price += priceResolution;
                past.remove(0);
                past.add("high");
            }
        }
        return current_price;
    }
}




//    For now, we sell all q at equilibrium q.
//    In future, have test calls to buyer and seller before locking it in (and
//    thereby locking long-term values)
//    Price spiking and crashing should be handled by actors, not by clearinghouse.
//
//    Implement an auction-house style in future, where purchase and selling bids
//    are posted, then final price offered/quantity received is returned later.
//    Quantity received/average price can then be a random function of the
//    clearing. Generally close to bid price, if we start from min_p of seller.
//    Maybe.
//
//    Perhaps initiate fixed prices at the start, and then variable prices
//    later on.
