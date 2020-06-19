package plushie_tycoon.serverService.geLocal;

import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;
import plushie_tycoon.Grpc;
import plushie_tycoon.SendCallsGrpc;
import plushie_tycoon.Grpc.UserID;
import plushie_tycoon.Grpc.ReturnCode;
import plushie_tycoon.Grpc.Snapshot;
import plushie_tycoon.Grpc.NullObject;
import plushie_tycoon.Grpc.ProposedChanges;
import plushie_tycoon.SendCallsGrpc.SendCallsBlockingStub;

public class LocalServer {
    public static boolean isregistered(int portno, String userid){
        UserID grpcUserid = UserID.newBuilder().setUserid(userid).build();
        SendCallsBlockingStub stub = generateBlockingStub(portno);
        ReturnCode returnCode = stub.isregistered(grpcUserid);
        System.out.println("LocalServer.isregistered called with portno " + portno);
        return returnCode.getCode();
    }

    public static Snapshot register(int portno, String userid){
        UserID grpcUserid = UserID.newBuilder().setUserid(userid).build();
        SendCallsBlockingStub stub = generateBlockingStub(portno);
        System.out.println("LocalServer.register called with portno " + portno);
        return stub.register(grpcUserid);
    }

    public static boolean send(int portno, ProposedChanges changes){
        SendCallsBlockingStub stub = generateBlockingStub(portno);
        ReturnCode returnCode = stub.send(changes);
        System.out.println("LocalServer.send called with portno " + portno);
        return returnCode.getCode();
    }

    public static Snapshot query(int portno, String userid){
        UserID grpcUserid = UserID.newBuilder().setUserid(userid).build();
        SendCallsBlockingStub stub = generateBlockingStub(portno);
        System.out.println("LocalServer.query called with portno " + portno);
        return stub.query(grpcUserid);
    }

    public static int getTime(int portno){
        NullObject nullObject = Grpc.NullObject.newBuilder().build();
        SendCallsBlockingStub stub = generateBlockingStub(portno);
        System.out.println("LocalServer.getTime called with portno " + portno);
        return stub.getTime(nullObject).getItem();
    }

    public static boolean hasUpdated(int portno, String userid){
        UserID userID = Grpc.UserID.newBuilder().setUserid(userid).build();
        SendCallsBlockingStub stub = generateBlockingStub(portno);
        System.out.println("LocalServer.hasUpdated called with portno " + portno);
        return stub.hasUpdated(userID).getCode();
    }

    private static SendCallsBlockingStub generateBlockingStub(int portno){
        String target = "localhost:" + portno;
        ManagedChannel channel = ManagedChannelBuilder.forTarget(target).usePlaintext().build();
        System.out.println("LocalServer.SendCallsBlockingStub called with channel " + channel);
        return SendCallsGrpc.newBlockingStub(channel);
    }
}

