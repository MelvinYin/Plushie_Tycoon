package plushie_tycoon.local.localEngine;

import plushie_tycoon.local.localEngine.inventory.LocalInventory;
import plushie_tycoon.local.localEngine.market.LocalMarket;

import java.util.Stack;

public class StateHistory {
    private Stack<Double> budget;
    private Stack<LocalInventory> LocalInventory;
    private Stack<LocalMarket> market;
    private Stack<Integer> time;
    public StateHistory(){
        budget = new Stack<>();
        LocalInventory = new Stack<>();
        time = new Stack<>();
        market = new Stack<>();
    }

    public void addBudget(double budget){
        this.budget.push(budget);
    }

    public void addInventory(LocalInventory LocalInventory){
        this.LocalInventory.push(LocalInventory);
    }
    public void addMarket(LocalMarket market){
        this.market.push(market);
    }
    public void addTime(int time){
        this.time.push(time);
    }

    public boolean isValid(){
        int size = budget.size();
        return (market.size() == size) & (LocalInventory.size() == size) & (time.size() == size);
    }

    public void reset(){
        budget.empty();
        LocalInventory.empty();
        time.empty();
        market.empty();
    }

    public boolean isEmpty(){
        return (isValid() & budget.size() == 0);
    }

    public double getBudget(){
        return budget.peek();
    }
    public LocalMarket getMarket(){
        return market.peek();
    }
    public int getTime(){
        return time.peek();
    }
    public LocalInventory getLocalInventory(){
        return LocalInventory.peek();
    }
    public void pop(){
        budget.pop();
        time.pop();
        LocalInventory.pop();
        market.pop();
    }
}

