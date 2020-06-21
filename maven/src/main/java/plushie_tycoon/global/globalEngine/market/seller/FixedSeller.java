package plushie_tycoon.global.globalEngine.market.seller;

public class FixedSeller extends SellerBase {
    private int quantity;
    public FixedSeller(int quantity) {
        this.quantity = quantity;
    }
    public int sell(double price) {
        return this.quantity;
    }
}