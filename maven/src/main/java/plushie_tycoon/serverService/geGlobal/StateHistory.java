package plushie_tycoon.serverService.geGlobal;

import plushie_tycoon.serverService.geGlobal.inventory.GlobalInventory;
import plushie_tycoon.serverService.geGlobal.market.GlobalMarket;

import java.util.Stack;

public class StateHistory {
    private Stack<Double> budget;
    private Stack<GlobalInventory> inventory;
    private Stack<GlobalMarket> market;
    private Stack<Integer> time;
    public StateHistory(){
        budget = new Stack<>();
        inventory = new Stack<>();
        time = new Stack<>();
        market = new Stack<>();
    }

    public void addBudget(double budget){
        this.budget.push(budget);
    }

    public void addInventory(GlobalInventory inventory){
        this.inventory.push(inventory);
    }
    public void addMarket(GlobalMarket market){
        this.market.push(market);
    }
    public void addTime(int time){
        this.time.push(time);
    }

    public boolean isValid(){
        int size = budget.size();
        return (market.size() == size) & (inventory.size() == size) & (time.size() == size);
    }

    public boolean isEmpty(){
        return (isValid() & budget.size() == 0);
    }

    public double getBudget(){
        return budget.peek();
    }
    public GlobalMarket getMarket(){
        return market.peek();
    }
    public int getTime(){
        return time.peek();
    }
    public GlobalInventory getInventory(){
        return inventory.peek();
    }
    public void pop(){
        budget.pop();
        time.pop();
        inventory.pop();
        market.pop();
    }
}

