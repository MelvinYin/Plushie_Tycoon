package plushie_tycoon.global.geGlobal.market.seller;
import java.lang.Math;

public class LinearSeller extends SellerBase {
    private double gradient;
    private int reference_quantity;
    private double reference_price;

    public LinearSeller(){
        this(0.9, 1000, 10.);
    }

    public LinearSeller(double gradient, int reference_quantity, double reference_price){
        this.gradient = gradient;
        this.reference_quantity = reference_quantity;
        this.reference_price = reference_price;
    }


    public int sell(double price){
        return (int) Math.round(reference_quantity + (price - reference_price) * gradient);
    }
}
