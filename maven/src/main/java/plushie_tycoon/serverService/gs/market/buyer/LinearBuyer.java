package plushie_tycoon.serverService.gs.market.buyer;
import java.lang.Math;

public class LinearBuyer extends BuyerBase{
    private double grad;
    private int ref_q;
    private int ref_p;

    public LinearBuyer(){
        this.grad = 0.9;
        this.ref_q = 1000;
        this.ref_p = 10;
    }

    public int buy(double price){
        return (int) Math.round(this.ref_q + (this.ref_p - price) * this.grad);
    }
}
