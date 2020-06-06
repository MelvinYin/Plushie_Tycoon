package plushie_tycoon.serverService.geGlobal.market.buyer;

public class FixedBuyer extends BuyerBase{
    private int quantity;
    public FixedBuyer(int quantity) {
        this.quantity = quantity;
    }
    public int buy(double price) {
        return this.quantity;
    }
}
