package plushie_tycoon.client;

import io.grpc.stub.StreamObserver;
import plushie_tycoon.Grpc;
import plushie_tycoon.ClientPageGrpc;

import plushie_tycoon.utils.BaseStringConverter;
import plushie_tycoon.client.clientEngine.ClientEngine;


public class ClientPageService extends ClientPageGrpc.ClientPageImplBase  {
    ClientEngine ge;
    public ClientPageService(ClientEngine ge){
        this.ge = ge;
    }
    @Override
    public void buy(Grpc.TransactionObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
        System.out.println("ClientPageService.buy called");
        Grpc.Snapshot output = ge.buy(BaseStringConverter.convert(request.getName()), request.getQuantity());
        responseObserver.onNext(output);
        responseObserver.onCompleted();
    }
    @Override
    public void sell(Grpc.TransactionObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
        System.out.println("ClientPageService.sell called");
        Grpc.Snapshot output = ge.sell(BaseStringConverter.convert(request.getName()), request.getQuantity());
        responseObserver.onNext(output);
        responseObserver.onCompleted();
    }
    @Override
    public void make(Grpc.TransactionObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
        System.out.println("ClientPageService.make called");
        Grpc.Snapshot output = ge.make(BaseStringConverter.convert(request.getName()), request.getQuantity());
        responseObserver.onNext(output);
        responseObserver.onCompleted();
    }
    @Override
    public void next(Grpc.NullObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
        System.out.println("ClientPageService.next called");
        Grpc.Snapshot output = ge.next();
        responseObserver.onNext(output);
        responseObserver.onCompleted();
    }
    @Override
    public void save(Grpc.NullObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
        System.out.println("ClientPageService.save called");
        Grpc.Snapshot output = ge.save();
        responseObserver.onNext(output);
        responseObserver.onCompleted();
    }
    @Override
    public void load(Grpc.NullObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
        System.out.println("ClientPageService.load called");
        Grpc.Snapshot output = ge.load();
        responseObserver.onNext(output);
        responseObserver.onCompleted();
    }
    @Override
    public void back(Grpc.NullObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
        System.out.println("ClientPageService.back called");
        Grpc.Snapshot output = ge.back();
        responseObserver.onNext(output);
        responseObserver.onCompleted();
    }
    @Override
    public void quit(Grpc.NullObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
        System.out.println("ClientPageService.quit called");
        Grpc.Snapshot output = ge.quit();
        responseObserver.onNext(output);
        responseObserver.onCompleted();
    }
    @Override
    public void init(Grpc.NullObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
        System.out.println("ClientPageService.init called");
        Grpc.Snapshot output = ge.init();
        responseObserver.onNext(output);
        responseObserver.onCompleted();
    }
    @Override
    public void update(Grpc.IntObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
        System.out.println("ClientPageService.update called");
        Grpc.Snapshot output = ge.updateFromHost();
        responseObserver.onNext(output);
        responseObserver.onCompleted();
    }
}
