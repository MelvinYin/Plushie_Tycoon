package plushie_tycoon.serverService.geGlobal;

import plushie_tycoon.Grpc;
import plushie_tycoon.serverService.config.Initials;
import plushie_tycoon.serverService.config.baseObjects.BaseObjects;
import plushie_tycoon.serverService.utils.BaseStringConverter;

import java.util.HashMap;

public class MockGEGlobal {
    public HashMap<String, Boolean> hasUpdated;
    MockGEGlobal() {hasUpdated = new HashMap<>();}

    public Grpc.ReturnCode addCall(String userid, HashMap<BaseObjects, Integer> buySellOrders,
                                   HashMap<BaseObjects, Integer> makeOrders){
        hasUpdated.put(userid, true);
        return Grpc.ReturnCode.newBuilder().build();
    }

    public boolean timeCheck(int time){
        return (time == 0);
    }

    public Grpc.Snapshot query(String userid){
        return Grpc.Snapshot.newBuilder().build();
    }

    public boolean hasupdate(String userid){
        return hasUpdated.get(userid);
    }


}
