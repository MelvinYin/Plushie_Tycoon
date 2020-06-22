package plushie_tycoon.host.hostEngine;

import plushie_tycoon.config.Initials;
import plushie_tycoon.config.baseObjects.BaseObjects;

import java.util.HashMap;

public class UserData {
    public HashMap<BaseObjects, Integer> inventory;
    public double budget;
    UserData(){
        inventory = Initials.quantities;
        budget = Initials.budget;
    }
}
