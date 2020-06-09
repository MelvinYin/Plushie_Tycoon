package plushie_tycoon.serverService;

import io.grpc.Server;
import io.grpc.ServerBuilder;
import io.grpc.stub.StreamObserver;
import plushie_tycoon.Grpc;
import plushie_tycoon.UITransferGrpc;

import java.io.IOException;

import plushie_tycoon.serverService.utils.BaseStringConverter;
import plushie_tycoon.serverService.geLocal.GELocal;

public class ServerService {
    private static GELocal ge;
    public int portno;

    public ServerService(int portno){
        this.portno = portno;
        ge = new GELocal();
    }

    public void run() throws IOException, InterruptedException {
        ServerBuilder builder = ServerBuilder.forPort(portno);
        UITransferService service = new UITransferService();
        builder.addService(service);
        Server server = builder.build();
        server.start();
        server.awaitTermination();
    }

    public static class UITransferService extends UITransferGrpc.UITransferImplBase  {

        @Override
        public void buy(Grpc.TransactionObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
            Grpc.Snapshot output = ge.buy(BaseStringConverter.convert(request.getName()), request.getQuantity());
            responseObserver.onNext(output);
            responseObserver.onCompleted();
        }
        @Override
        public void sell(Grpc.TransactionObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
            Grpc.Snapshot output = ge.sell(BaseStringConverter.convert(request.getName()), request.getQuantity());
            responseObserver.onNext(output);
            responseObserver.onCompleted();
        }
        @Override
        public void make(Grpc.TransactionObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
            Grpc.Snapshot output = ge.make(BaseStringConverter.convert(request.getName()), request.getQuantity());
            responseObserver.onNext(output);
            responseObserver.onCompleted();
        }
        @Override
        public void next(Grpc.NullObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
            Grpc.Snapshot output = ge.next();
            responseObserver.onNext(output);
            responseObserver.onCompleted();
        }
        @Override
        public void save(Grpc.NullObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
            Grpc.Snapshot output = ge.save();
            responseObserver.onNext(output);
            responseObserver.onCompleted();
        }
        @Override
        public void load(Grpc.NullObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
            Grpc.Snapshot output = ge.load();
            responseObserver.onNext(output);
            responseObserver.onCompleted();
        }
        //        @Override
        public void back(Grpc.NullObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
            Grpc.Snapshot output = ge.back();
            responseObserver.onNext(output);
            responseObserver.onCompleted();
        }
        //        @Override
        public void quit(Grpc.NullObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
            Grpc.Snapshot output = ge.quit();
            responseObserver.onNext(output);
            responseObserver.onCompleted();
        }
        //        @Override
        public void init(Grpc.NullObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
            Grpc.Snapshot output = ge.init();
            System.out.println(output);
            responseObserver.onNext(output);
            responseObserver.onCompleted();
        }
    }
}

