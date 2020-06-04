package plushie_tycoon.serverService.ge.market.buyer;

public class ConsolidatedBuyer extends BuyerBase{
    BuyerBase[] buyers;
    public ConsolidatedBuyer(BuyerBase[] buyers){
        this.buyers = buyers;
    }
    public int buy(double price){
        int quantity = 0;
        for (BuyerBase buyer: this.buyers){
            quantity += buyer.buy(price);
        }
        return quantity;
    }
}
