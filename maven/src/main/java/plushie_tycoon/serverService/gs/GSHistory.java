package plushie_tycoon.serverService.gs;

import plushie_tycoon.serverService.gs.inventory.GlobalInventory;
import plushie_tycoon.serverService.gs.market.GlobalMarket;
import plushie_tycoon.serverService.gs.inventory.GlobalInventory;

import java.util.Stack;

public class GSHistory {
    private Stack<Integer> budget;
    private Stack<GlobalInventory> inventory;
    private Stack<GlobalMarket> market;
    private Stack<Integer> time;
    public GSHistory(){
        budget = new Stack<>();
        inventory = new Stack<>();
        time = new Stack<>();
        market = new Stack<>();
    }

    public void addBudget(int budget){
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

    public int getBudget(){
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

