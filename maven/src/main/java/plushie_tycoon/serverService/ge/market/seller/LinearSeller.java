package plushie_tycoon.serverService.ge.market.seller;
import java.lang.Math;

public class LinearSeller extends SellerBase {
    private double grad;
    private int ref_q;
    private int ref_p;

    public LinearSeller(){
        this.grad = 0.9;
        this.ref_q = 1000;
        this.ref_p = 10;
    }

    public int sell(double price){
        return (int) Math.round(this.ref_q + (price - this.ref_p) * this.grad);
    }
}
