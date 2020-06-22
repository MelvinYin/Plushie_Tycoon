package plushie_tycoon.host.hostEngine.hostServices;

import io.grpc.stub.StreamObserver;
import plushie_tycoon.Grpc;
import plushie_tycoon.ClientToHostGrpc;
import plushie_tycoon.config.baseObjects.BaseObjects;
import plushie_tycoon.config.baseObjects.Products;
import plushie_tycoon.host.hostEngine.HostEngine;
import plushie_tycoon.utils.BaseStringConverter;

import java.util.HashMap;


public class ClientToHostService extends ClientToHostGrpc.ClientToHostImplBase  {
    HostEngine ge;

    public ClientToHostService(HostEngine ge){
        this.ge = ge;
    }


    @Override
    public void send(Grpc.ProposedChanges request, StreamObserver<Grpc.ReturnCode> responseObserver) {
        System.out.println("GlobalServerService.send called.");
        HashMap<BaseObjects, Integer> buySellOrders = new HashMap<>();
        for (HashMap.Entry<String, Integer> entry: request.getBuySellMap().entrySet()){
            buySellOrders.put(BaseStringConverter.convert(entry.getKey()), entry.getValue());
        }
        HashMap<Products, Integer> makeOrders = new HashMap<>();
        for (HashMap.Entry<String, Integer> entry: request.getMakeMap().entrySet()){
            makeOrders.put((Products) BaseStringConverter.convert(entry.getKey()), entry.getValue());
        }

        Grpc.ReturnCode output = ge.addCall(request.getUserid(), buySellOrders, makeOrders);
        responseObserver.onNext(output);
        responseObserver.onCompleted();
    }

    @Override
    public void ping(Grpc.NullObject request, StreamObserver<Grpc.NullObject> responseObserver) {
        System.out.println("GlobalServerService.ping called.");
        responseObserver.onNext(Grpc.NullObject.newBuilder().build());
        responseObserver.onCompleted();
    }

    @Override
    public void query(Grpc.UserID request, StreamObserver<Grpc.Snapshot> responseObserver) {
        System.out.println("GlobalServerService.query called.");
        Grpc.Snapshot output = ge.query(request.getUserid());
        responseObserver.onNext(output);
        responseObserver.onCompleted();
    }

    @Override
    public void register(Grpc.UserID request, StreamObserver<Grpc.Snapshot> responseObserver) {
        System.out.println("GlobalServerService.register called.");
        Grpc.Snapshot output = ge.register(request.getUserid());
        responseObserver.onNext(output);
        responseObserver.onCompleted();
    }

    @Override
    public void isregistered(Grpc.UserID request, StreamObserver<Grpc.ReturnCode> responseObserver) {
        System.out.println("GlobalServerService.isregistered called.");
        boolean returnCode = ge.isRegistered(request.getUserid());
        Grpc.ReturnCode output = Grpc.ReturnCode.newBuilder().setCode(returnCode).build();
        responseObserver.onNext(output);
        responseObserver.onCompleted();
    }

    @Override
    public void getTime(Grpc.NullObject request, StreamObserver<Grpc.IntObject> responseObserver) {
        System.out.println("GlobalServerService.getTime called.");
        int time = ge.getTime();
        Grpc.IntObject output = Grpc.IntObject.newBuilder().setItem(time).build();
        responseObserver.onNext(output);
        responseObserver.onCompleted();
    }

    @Override
    public void hasUpdated(Grpc.UserID request, StreamObserver<Grpc.ReturnCode> responseObserver) {
        System.out.println("GlobalServerService.hasUpdated called.");
        boolean returnCode = ge.hasUpdated(request.getUserid());
        Grpc.ReturnCode output = Grpc.ReturnCode.newBuilder().setCode(returnCode).build();
        responseObserver.onNext(output);
        responseObserver.onCompleted();
    }
}

