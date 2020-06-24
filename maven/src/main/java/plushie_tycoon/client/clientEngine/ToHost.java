package plushie_tycoon.client.clientEngine;

import io.grpc.Deadline;
import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;
import plushie_tycoon.Grpc;
import plushie_tycoon.ClientToHostGrpc;
import plushie_tycoon.Grpc.UserID;
import plushie_tycoon.Grpc.ReturnCode;
import plushie_tycoon.Grpc.Snapshot;
import plushie_tycoon.Grpc.NullObject;
import plushie_tycoon.Grpc.ProposedChanges;
import plushie_tycoon.ClientToHostGrpc.ClientToHostBlockingStub;

import java.util.concurrent.TimeUnit;

public class ToHost {
    int portno;
    ManagedChannel channel;
    public ToHost(int portno){
        this.portno = portno;
        String target = "localhost:" + portno;
        channel = ManagedChannelBuilder.forTarget(target).usePlaintext().build();
    }

    public boolean isregistered(String userid){
        UserID grpcUserid = UserID.newBuilder().setUserid(userid).build();
        ClientToHostBlockingStub stub = ClientToHostGrpc.newBlockingStub(channel);
        ReturnCode returnCode = stub.isregistered(grpcUserid);
        System.out.println("ToHost.isregistered called with portno " + portno);
        return returnCode.getCode();
    }

    public double ping(){
        NullObject nullObject = NullObject.newBuilder().build();
        ClientToHostBlockingStub stub = ClientToHostGrpc.newBlockingStub(channel);
        long startTime = System.nanoTime();
        NullObject nullObj = stub.ping(nullObject);
        long endTime = System.nanoTime();
        long timeElapsed = (endTime - startTime) / 1_000_000;
        System.out.println("ToHost.ping first ping takes <" + timeElapsed + "> ms.");
        startTime = System.nanoTime();
        nullObj = stub.ping(nullObject);
        endTime = System.nanoTime();
        timeElapsed = (endTime - startTime) / 1_000_000;
        System.out.println("ToHost.ping second ping takes <" + timeElapsed + "> ms.");
        return timeElapsed;
    }

    public void waitForReady(int deadline){
        NullObject nullObject = NullObject.newBuilder().build();
        ClientToHostBlockingStub stub = ClientToHostGrpc.newBlockingStub(channel).withDeadlineAfter(deadline, TimeUnit.SECONDS)
                .withWaitForReady();
        try {
            NullObject nullObj = stub.ping(nullObject);
        } catch (Exception e){
            System.out.println("PlushieServer waited on global server at portno " + portno + " for " + deadline
                    + " seconds but no reply is obtained.");
            throw e;
        }
    }

    public Snapshot register(String userid){
        UserID grpcUserid = UserID.newBuilder().setUserid(userid).build();
        ClientToHostBlockingStub stub = ClientToHostGrpc.newBlockingStub(channel);
        System.out.println("ToHost.register called with portno " + portno);
        return stub.withWaitForReady().withDeadline(Deadline.after(3, TimeUnit.SECONDS)).register(grpcUserid);
    }

    public boolean send(ProposedChanges changes){
        ClientToHostBlockingStub stub = ClientToHostGrpc.newBlockingStub(channel);
        ReturnCode returnCode = stub.send(changes);
        System.out.println("ToHost.send called with portno " + portno);
        return returnCode.getCode();
    }

    public Snapshot query(String userid){
        UserID grpcUserid = UserID.newBuilder().setUserid(userid).build();
        ClientToHostBlockingStub stub = ClientToHostGrpc.newBlockingStub(channel);
        System.out.println("ToHost.query called with portno " + portno);
        return stub.query(grpcUserid);
    }

    public int getTime(){
        NullObject nullObject = Grpc.NullObject.newBuilder().build();
        ClientToHostBlockingStub stub = ClientToHostGrpc.newBlockingStub(channel);
        System.out.println("ToHost.getTime called with portno " + portno);
        Grpc.IntObject grpcInt = stub.getTime(nullObject);
        return grpcInt.getItem();
    }

    public boolean hasUpdated(String userid){
        UserID userID = Grpc.UserID.newBuilder().setUserid(userid).build();
        ClientToHostBlockingStub stub = ClientToHostGrpc.newBlockingStub(channel);
        System.out.println("ToHost.hasUpdated called with portno " + portno);
        return stub.hasUpdated(userID).getCode();
    }
}

