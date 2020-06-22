package plushie_tycoon.host.hostEngine.hostServices;

import io.grpc.stub.StreamObserver;
import plushie_tycoon.Grpc;
import plushie_tycoon.AdminPageGrpc;
import plushie_tycoon.host.hostEngine.HostEngine;


public class AdminPageService extends AdminPageGrpc.AdminPageImplBase  {
    HostEngine ge;
    public AdminPageService (HostEngine ge){
        this.ge = ge;
    }

    @Override
    public void nextTurn(Grpc.NullObject request, StreamObserver<Grpc.ReturnCode> responseObserver) {
        System.out.println("AdminServerService.nextTurn called.");
        ge.lockOrderStack();
        if (ge.orderStackIsEmpty()){
            String time = String.valueOf(ge.nextTurn());
            responseObserver.onNext(Grpc.ReturnCode.newBuilder().setCode(true).setMessage(time).build());
        } else {
            responseObserver.onNext(Grpc.ReturnCode.newBuilder().setCode(false).build());
        }
        responseObserver.onCompleted();
        ge.unlockOrderStack();
    }

    @Override
    public void getCall(Grpc.NullObject request, StreamObserver<Grpc.ProposedChanges> responseObserver) {
        System.out.println("AdminServerService.getCall called.");
        Grpc.ProposedChanges changes = ge.getCall();
        while (!changes.getUserid().equals("")){
            responseObserver.onNext(changes);
            changes = ge.getCall();
        }
        responseObserver.onCompleted();
    }

    @Override
    public void ping(Grpc.NullObject request, StreamObserver<Grpc.NullObject> responseObserver) {
        System.out.println("AdminServerService.ping called.");
        responseObserver.onNext(Grpc.NullObject.newBuilder().build());
        responseObserver.onCompleted();
    }
}

