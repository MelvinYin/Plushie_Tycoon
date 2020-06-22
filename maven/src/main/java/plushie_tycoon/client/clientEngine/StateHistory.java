package plushie_tycoon.client.clientEngine;

import plushie_tycoon.client.clientEngine.clientInventory.ClientInventory;
import plushie_tycoon.client.clientEngine.clientMarket.ClientMarket;

import java.util.Stack;

public class StateHistory {
    private Stack<Double> budget;
    private Stack<ClientInventory> ClientInventory;
    private Stack<ClientMarket> market;
    private Stack<Integer> time;
    public StateHistory(){
        budget = new Stack<>();
        ClientInventory = new Stack<>();
        time = new Stack<>();
        market = new Stack<>();
    }

    public void addBudget(double budget){
        this.budget.push(budget);
    }

    public void addInventory(ClientInventory ClientInventory){
        this.ClientInventory.push(ClientInventory);
    }
    public void addMarket(ClientMarket market){
        this.market.push(market);
    }
    public void addTime(int time){
        this.time.push(time);
    }

    public boolean isValid(){
        int size = budget.size();
        return (market.size() == size) & (ClientInventory.size() == size) & (time.size() == size);
    }

    public void reset(){
        budget.empty();
        ClientInventory.empty();
        time.empty();
        market.empty();
    }

    public boolean isEmpty(){
        return (isValid() & budget.size() == 0);
    }

    public double getBudget(){
        return budget.peek();
    }
    public ClientMarket getMarket(){
        return market.peek();
    }
    public int getTime(){
        return time.peek();
    }
    public ClientInventory getClientInventory(){
        return ClientInventory.peek();
    }
    public void pop(){
        budget.pop();
        time.pop();
        ClientInventory.pop();
        market.pop();
    }
}

