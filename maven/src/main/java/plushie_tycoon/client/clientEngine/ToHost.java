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
    public static boolean isregistered(int portno, String userid){
        UserID grpcUserid = UserID.newBuilder().setUserid(userid).build();
        ClientToHostBlockingStub stub = generateBlockingStub(portno);
        ReturnCode returnCode = stub.isregistered(grpcUserid);
        System.out.println("ToHost.isregistered called with portno " + portno);
        return returnCode.getCode();
    }

    public static double ping(int portno){
        NullObject nullObject = NullObject.newBuilder().build();
        ClientToHostBlockingStub stub = generateBlockingStub(portno);
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

    public static void waitForReady(int portno, int deadline){
        NullObject nullObject = NullObject.newBuilder().build();
        ClientToHostBlockingStub stub = generateBlockingStub(portno).withDeadlineAfter(deadline, TimeUnit.SECONDS)
                .withWaitForReady();
        try {
            NullObject nullObj = stub.ping(nullObject);
        } catch (Exception e){
            System.out.println("PlushieServer waited on global server at portno " + portno + " for " + deadline
                    + " seconds but no reply is obtained.");
            throw e;
        }
    }

    public static void waitForReady(int portno){
        waitForReady(portno, 10);
    }

    public static Snapshot register(int portno, String userid){
        UserID grpcUserid = UserID.newBuilder().setUserid(userid).build();
        ClientToHostBlockingStub stub = generateBlockingStub(portno);
        System.out.println("ToHost.register called with portno " + portno);
        return stub.withWaitForReady().withDeadline(Deadline.after(3, TimeUnit.SECONDS)).register(grpcUserid);
    }

    public static boolean send(int portno, ProposedChanges changes){
        ClientToHostBlockingStub stub = generateBlockingStub(portno);
        ReturnCode returnCode = stub.send(changes);
        System.out.println("ToHost.send called with portno " + portno);
        return returnCode.getCode();
    }

    public static Snapshot query(int portno, String userid){
        UserID grpcUserid = UserID.newBuilder().setUserid(userid).build();
        ClientToHostBlockingStub stub = generateBlockingStub(portno);
        System.out.println("ToHost.query called with portno " + portno);
        return stub.query(grpcUserid);
    }

    public static int getTime(int portno){
        NullObject nullObject = Grpc.NullObject.newBuilder().build();
        ClientToHostBlockingStub stub = generateBlockingStub(portno);
        System.out.println("ToHost.getTime called with portno " + portno);
        return stub.getTime(nullObject).getItem();
    }

    public static boolean hasUpdated(int portno, String userid){
        UserID userID = Grpc.UserID.newBuilder().setUserid(userid).build();
        ClientToHostBlockingStub stub = generateBlockingStub(portno);
        System.out.println("ToHost.hasUpdated called with portno " + portno);
        return stub.hasUpdated(userID).getCode();
    }

    private static ClientToHostBlockingStub generateBlockingStub(int portno){
        String target = "localhost:" + portno;
        ManagedChannel channel = ManagedChannelBuilder.forTarget(target).usePlaintext().build();
        System.out.println("ToHost.SendCallsBlockingStub called with channel " + channel);
        return ClientToHostGrpc.newBlockingStub(channel);
    }
}

