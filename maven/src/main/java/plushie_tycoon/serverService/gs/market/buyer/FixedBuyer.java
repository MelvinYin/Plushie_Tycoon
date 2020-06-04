package plushie_tycoon.serverService.gs.market.buyer;

public class FixedBuyer extends BuyerBase{
    private int quantity;
    public FixedBuyer(int quantity) {
        this.quantity = quantity;
    }
    public int buy(double price) {
        return this.quantity;
    }
}
