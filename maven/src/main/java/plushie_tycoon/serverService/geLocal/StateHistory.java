package plushie_tycoon.serverService.geLocal;

import plushie_tycoon.serverService.geLocal.inventory.LocalInventory;
import plushie_tycoon.serverService.geLocal.market.LocalMarket;

import java.util.Stack;

public class StateHistory {
    private Stack<Double> budget;
    private Stack<LocalInventory> localInventory;
    private Stack<LocalMarket> market;
    private Stack<Integer> time;
    public StateHistory(){
        budget = new Stack<>();
        localInventory = new Stack<>();
        time = new Stack<>();
        market = new Stack<>();
    }

    public void addBudget(double budget){
        this.budget.push(budget);
    }

    public void addInventory(LocalInventory localInventory){
        this.localInventory.push(localInventory);
    }
    public void addMarket(LocalMarket market){
        this.market.push(market);
    }
    public void addTime(int time){
        this.time.push(time);
    }

    public boolean isValid(){
        int size = budget.size();
        return (market.size() == size) & (localInventory.size() == size) & (time.size() == size);
    }

    public void reset(){
        budget.empty();
        localInventory.empty();
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
        return localInventory.peek();
    }
    public void pop(){
        budget.pop();
        time.pop();
        localInventory.pop();
        market.pop();
    }
}

