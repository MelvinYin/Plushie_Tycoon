package plushie_tycoon.config;

import plushie_tycoon.config.baseObjects.BaseObjects;

import java.util.HashMap;

public class CallStack {
    public HashMap<BaseObjects, Integer> buySell;
    public HashMap<BaseObjects, Integer> make;

    CallStack(){
        buySell = new HashMap<>();
        make = new HashMap<>();
    }

    public void buy(BaseObjects category, Integer quantity){
        buySell.put(category, buySell.getOrDefault(category, 0) + quantity);
    }
    public void sell(BaseObjects category, Integer quantity){
        buySell.put(category, buySell.getOrDefault(category, 0) - quantity);
    }
    public void make(BaseObjects category, Integer quantity){
        make.put(category, make.getOrDefault(category, 0) + quantity);
    }
}
