package plushie_tycoon.serverService.ge.market.seller;

public class FixedSeller extends SellerBase {
    private int quantity;
    public FixedSeller(int quantity) {
        this.quantity = quantity;
    }
    public int sell(double price) {
        return this.quantity;
    }
}