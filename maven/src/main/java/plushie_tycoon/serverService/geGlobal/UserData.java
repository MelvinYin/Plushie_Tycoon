package plushie_tycoon.serverService.geGlobal;

import com.sun.org.apache.xml.internal.security.Init;
import plushie_tycoon.serverService.config.Initials;
import plushie_tycoon.serverService.config.baseObjects.BaseObjects;

import java.util.HashMap;

public class UserData {
    public HashMap<BaseObjects, Integer> inventory;
    public double budget;
    UserData(){
        inventory = Initials.quantities;
        budget = Initials.budget;
    }
}
