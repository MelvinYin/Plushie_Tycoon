package plushie_tycoon.serverService;

import io.grpc.Server;
import io.grpc.ServerBuilder;
import io.grpc.stub.StreamObserver;
import plushie_tycoon.Grpc;
import plushie_tycoon.MockService;
import plushie_tycoon.UITransferGrpc;
import plushie_tycoon.serverService.config.baseObjects.BaseObjects;
import plushie_tycoon.serverService.config.baseObjects.Products;
import plushie_tycoon.serverService.config.baseObjects.Resources;

import java.io.IOException;
import java.util.HashMap;
import plushie_tycoon.serverService.utils.BaseStringConverter;
import plushie_tycoon.serverService.ge.GE;

public class ServerService {
    private static GE ge;
    public int portno;

    public ServerService(int portno){
        this.portno = portno;
        ge = new GE();
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
        public void next(Grpc.SelectionObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
            Grpc.Snapshot output = ge.next();
            responseObserver.onNext(output);
            responseObserver.onCompleted();
        }
        @Override
        public void save(Grpc.SelectionObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
            Grpc.Snapshot output = ge.save();
            responseObserver.onNext(output);
            responseObserver.onCompleted();
        }
        @Override
        public void load(Grpc.SelectionObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
            Grpc.Snapshot output = ge.load();
            responseObserver.onNext(output);
            responseObserver.onCompleted();
        }
        //        @Override
        public void back(Grpc.SelectionObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
            Grpc.Snapshot output = ge.back();
            responseObserver.onNext(output);
            responseObserver.onCompleted();
        }
        //        @Override
        public void quit(Grpc.SelectionObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
            Grpc.Snapshot output = ge.quit();
            responseObserver.onNext(output);
            responseObserver.onCompleted();
        }
        //        @Override
        public void init(Grpc.SelectionObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
            Grpc.Snapshot output = ge.init();
            System.out.println(output);
            responseObserver.onNext(output);
            responseObserver.onCompleted();
        }
    }
}

