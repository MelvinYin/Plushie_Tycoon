package plushie_tycoon.serverService.config;

import jdk.vm.ci.code.site.Call;
import plushie_tycoon.serverService.config.baseObjects.BaseObjects;

import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

public class CallStack {
    String userID;
    Stack<CallObject> calls;

    CallStack(String userID){
        this.userID = userID;
        calls = new Stack<>();
    }

    public void buy(BaseObjects category, Integer quantity){
        CallObject call = new CallObject("buy", category, quantity);
        calls.add(call);
    }
    public void sell(BaseObjects category, Integer quantity){
        CallObject call = new CallObject("sell", category, quantity);
        calls.add(call);
    }
    public void make(BaseObjects category, Integer quantity){
        CallObject call = new CallObject("make", category, quantity);
        calls.add(call);
    }
    public boolean reverse(){
        if (calls.empty()){
            return false;
        }
        calls.pop();
        return true;
    }

    public HashMap<String, HashMap<BaseObjects, Integer>> returnCalls(){
        HashMap<BaseObjects, Integer> buySell = new HashMap<>();
        HashMap<BaseObjects, Integer> make = new HashMap<>();
        while (!calls.empty()){
            CallObject call = calls.pop();
            if (call.command.equals("make")){
                make.put(call.category, make.getOrDefault(call.category, 0) + call.quantity);
            } else {
                buySell.put(call.category, buySell.getOrDefault(call.category, 0) + call.quantity);
            }
        }
        HashMap<String, HashMap<BaseObjects, Integer>> output = new HashMap<>();
        for (Map.Entry<BaseObjects, Integer> entry: buySell.entrySet()){
            if (entry.getValue() > 0){
                output.putIfAbsent("buy", new HashMap<>());
                output.get("buy").put(entry.getKey(), entry.getValue());
            } else if (entry.getValue() < 0){
                output.putIfAbsent("sell", new HashMap<>());
                output.get("sell").put(entry.getKey(), entry.getValue());
            }
        }
        for (Map.Entry<BaseObjects, Integer> entry: make.entrySet()){
            if (entry.getValue() > 0){
                output.putIfAbsent("make", new HashMap<>());
                output.get("make").put(entry.getKey(), entry.getValue());
            }
        }
        return output;
    }

    private static class CallObject {
        String command;
        BaseObjects category;
        int quantity;
        CallObject(String command, BaseObjects category, int quantity){
            //            do checking if command in make, sell, etc
            this.command = command;
            this.category = category;
            this.quantity = quantity;
        }
    }
}
