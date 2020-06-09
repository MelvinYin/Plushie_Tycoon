package plushie_tycoon.serverService.geLocal;


import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;
import plushie_tycoon.SendCallsGrpc;
import plushie_tycoon.Grpc.UserID;
import plushie_tycoon.Grpc.ReturnCode;
import plushie_tycoon.Grpc.Snapshot;
import plushie_tycoon.Grpc.ProposedChanges;
import plushie_tycoon.SendCallsGrpc.SendCallsBlockingStub;

public class LocalServer {
    public static boolean isregistered(int portno, String userid){
        UserID grpcUserid = UserID.newBuilder().setUserid(userid).build();
        SendCallsBlockingStub stub = generateBlockingStub(portno);
        ReturnCode returnCode = stub.isregistered(grpcUserid);
        return returnCode.getCode();
    }

    public static Snapshot register(int portno, String userid){
        UserID grpcUserid = UserID.newBuilder().setUserid(userid).build();
        SendCallsBlockingStub stub = generateBlockingStub(portno);
        return stub.register(grpcUserid);
    }

    public static boolean send(int portno, ProposedChanges changes){
        SendCallsBlockingStub stub = generateBlockingStub(portno);
        ReturnCode returnCode = stub.send(changes);
        return returnCode.getCode();
    }

    public static Snapshot query(int portno, String userid){
        UserID grpcUserid = UserID.newBuilder().setUserid(userid).build();
        SendCallsBlockingStub stub = generateBlockingStub(portno);
        return stub.query(grpcUserid);
    }

//    public static Snapshot query(int portno, String userid){
//        UserID grpcUserid = UserID.newBuilder().setUserid(userid).build();
//        SendCallsBlockingStub stub = generateBlockingStub(portno);
//        return stub.query(grpcUserid);
//    }


    private static SendCallsBlockingStub generateBlockingStub(int portno){
        String target = "localhost:" + portno;
        ManagedChannel channel = ManagedChannelBuilder.forTarget(target).build();
        return SendCallsGrpc.newBlockingStub(channel);
    }


}

/*

rpc register(UserID) returns (Snapshot) {};
    rpc query(UserID) returns (Snapshot) {};
    rpc timeCheck(TimeCheck) returns (ReturnCode) {};
    rpc hasUpdate(UserID) returns (ReturnCode) {};
    */