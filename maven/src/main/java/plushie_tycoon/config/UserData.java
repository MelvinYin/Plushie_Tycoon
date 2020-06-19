package plushie_tycoon.config;

import plushie_tycoon.config.baseObjects.BaseObjects;

import java.util.HashMap;

public class UserData {
    public HashMap<BaseObjects, Integer> inventory;
    double budget;
    UserData(){
        inventory = Initials.quantities;
        budget = Initials.budget;
    }
    public void addInventory(BaseObjects base, int quantity){
        inventory.put(base, inventory.get(base) + quantity);
    }
    public void setInventory(BaseObjects base, int quantity){
        inventory.put(base, quantity);
    }
    public void setBudget(double budget){
        this.budget = budget;
    }
    public void addBudget(double addition){
        budget += addition;
    }
}
