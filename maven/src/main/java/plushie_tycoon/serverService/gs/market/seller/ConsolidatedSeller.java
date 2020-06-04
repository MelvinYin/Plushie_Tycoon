package plushie_tycoon.serverService.gs.market.seller;

public class ConsolidatedSeller extends SellerBase{
    SellerBase[] sellers;

    public ConsolidatedSeller(SellerBase[] sellers){
        this.sellers = sellers;
    }
    public int sell(double price){
        int quantity = 0;
        for (SellerBase seller: this.sellers){
            quantity += seller.sell(price);
        }
        return quantity;
    }
}
