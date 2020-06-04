package plushie_tycoon.serverService.ge;

public class BudgetBackend {
    private double budget;
    public BudgetBackend(double budget) {
        this.budget = budget;
    }
    public double get () {
        return this.budget;
    }

    public boolean sub (double other) {
        double item = this.budget - other;
        if (item < 0){
            String msg = "Insufficient quantity in " + getClass().getName() + ". Attempting to deduct " + other +
                    " from " + this.budget + ".";
            System.out.println(msg);
            return false;
        }
        this.budget = item;
        return true;
    }

    public void add (double other) {
        this.budget += other;
    }

    public void replace(double other) {
        this.budget = other;
    }
}
