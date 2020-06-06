package plushie_tycoon.serverService.geGlobal.market.buyer;
import java.lang.Math;

public class LinearBuyer extends BuyerBase{
    private double gradient;
    private int reference_quantity;
    private double reference_price;

    public LinearBuyer(){
        this(0.9, 1000, 10.);
    }

    public LinearBuyer(double gradient, int reference_quantity, double reference_price){
        this.gradient = gradient;
        this.reference_quantity = reference_quantity;
        this.reference_price = reference_price;
    }

    public int buy(double price){
        return ((int) Math.round(reference_quantity + (reference_price - price) * gradient));
    }
}
