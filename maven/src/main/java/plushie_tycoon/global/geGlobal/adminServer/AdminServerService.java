package plushie_tycoon.global.geGlobal.adminServer;

import io.grpc.Server;
import io.grpc.ServerBuilder;
import io.grpc.stub.StreamObserver;
import plushie_tycoon.Grpc;
import plushie_tycoon.AdminPageGrpc;
import plushie_tycoon.global.geGlobal.GEGlobal;

import java.io.IOException;

public class AdminServerService {
    public GEGlobal ge;
    public int portno;

    public AdminServerService(int portno, GEGlobal ge){
        this.portno = portno;
        this.ge = ge;
    }

    public void run() throws IOException, InterruptedException {
        ServerBuilder builder = ServerBuilder.forPort(portno);
        AdminServerService.AdminPageService service = new AdminServerService.AdminPageService();
        builder.addService(service);
        Server server = builder.build();
        server.start();
        server.awaitTermination();
    }

    public class AdminPageService extends AdminPageGrpc.AdminPageImplBase  {
        @Override
        public void nextTurn(Grpc.NullObject request, StreamObserver<Grpc.ReturnCode> responseObserver) {
            System.out.println("AdminServerService.nextTurn called.");
            ge.lockOrderStack();
            if (ge.orderStackIsEmpty()){
                ge.nextTurn();
                responseObserver.onNext(Grpc.ReturnCode.newBuilder().setCode(true).build());
                responseObserver.onCompleted();
            }
            ge.unlockOrderStack();
            responseObserver.onNext(Grpc.ReturnCode.newBuilder().setCode(false).build());
            responseObserver.onCompleted();
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
    }


}

