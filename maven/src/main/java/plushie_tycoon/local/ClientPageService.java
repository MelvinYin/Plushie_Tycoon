package plushie_tycoon.local;

import io.grpc.Server;
import io.grpc.ServerBuilder;
import io.grpc.stub.StreamObserver;
import plushie_tycoon.Grpc;
import plushie_tycoon.ClientPageGrpc;

import java.io.IOException;

import plushie_tycoon.local.utils.BaseStringConverter;
import plushie_tycoon.local.localEngine.LocalEngine;


public class ClientPageService extends ClientPageGrpc.ClientPageImplBase  {
    LocalEngine ge;
    public ClientPageService(LocalEngine ge){
        this.ge = ge;
    }
    @Override
    public void buy(Grpc.TransactionObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
        System.out.println("UITransferService.buy called");
        Grpc.Snapshot output = ge.buy(BaseStringConverter.convert(request.getName()), request.getQuantity());
        responseObserver.onNext(output);
        responseObserver.onCompleted();
    }
    @Override
    public void sell(Grpc.TransactionObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
        System.out.println("UITransferService.sell called");
        Grpc.Snapshot output = ge.sell(BaseStringConverter.convert(request.getName()), request.getQuantity());
        responseObserver.onNext(output);
        responseObserver.onCompleted();
    }
    @Override
    public void make(Grpc.TransactionObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
        System.out.println("UITransferService.make called");
        Grpc.Snapshot output = ge.make(BaseStringConverter.convert(request.getName()), request.getQuantity());
        responseObserver.onNext(output);
        responseObserver.onCompleted();
    }
    @Override
    public void next(Grpc.NullObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
        System.out.println("UITransferService.next called");
        Grpc.Snapshot output = ge.next();
        responseObserver.onNext(output);
        responseObserver.onCompleted();
    }
    @Override
    public void save(Grpc.NullObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
        System.out.println("UITransferService.save called");
        Grpc.Snapshot output = ge.save();
        responseObserver.onNext(output);
        responseObserver.onCompleted();
    }
    @Override
    public void load(Grpc.NullObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
        System.out.println("UITransferService.load called");
        Grpc.Snapshot output = ge.load();
        responseObserver.onNext(output);
        responseObserver.onCompleted();
    }
    //        @Override
    public void back(Grpc.NullObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
        System.out.println("UITransferService.back called");
        Grpc.Snapshot output = ge.back();
        responseObserver.onNext(output);
        responseObserver.onCompleted();
    }
    //        @Override
    public void quit(Grpc.NullObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
        System.out.println("UITransferService.quit called");
        Grpc.Snapshot output = ge.quit();
        responseObserver.onNext(output);
        responseObserver.onCompleted();
    }
    //        @Override
    public void init(Grpc.NullObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
        System.out.println("UITransferService.init called");
        Grpc.Snapshot output = ge.init();
        responseObserver.onNext(output);
        responseObserver.onCompleted();
    }
}


//public class ServerService {
//    private static LocalEngine ge;
//    public int toUIPortno;
//    public int toGlobalPortno;
//
//    public ServerService(int toUIPortno, int toGlobalPortno){
//        this.toUIPortno = toUIPortno;
//        this.toGlobalPortno = toGlobalPortno;
//        ge = new LocalEngine(toGlobalPortno);
//    }
//
//    public void run() throws IOException, InterruptedException {
//        ServerBuilder builder = ServerBuilder.forPort(toUIPortno);
//        UITransferService service = new UITransferService();
//        builder.addService(service);
//        Server server = builder.build();
//        server.start();
//        server.awaitTermination();
//    }
//
//    public static class UITransferService extends UITransferGrpc.UITransferImplBase  {
//        @Override
//        public void buy(Grpc.TransactionObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
//            System.out.println("UITransferService.buy called");
//            Grpc.Snapshot output = ge.buy(BaseStringConverter.convert(request.getName()), request.getQuantity());
//            responseObserver.onNext(output);
//            responseObserver.onCompleted();
//        }
//        @Override
//        public void sell(Grpc.TransactionObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
//            System.out.println("UITransferService.sell called");
//            Grpc.Snapshot output = ge.sell(BaseStringConverter.convert(request.getName()), request.getQuantity());
//            responseObserver.onNext(output);
//            responseObserver.onCompleted();
//        }
//        @Override
//        public void make(Grpc.TransactionObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
//            System.out.println("UITransferService.make called");
//            Grpc.Snapshot output = ge.make(BaseStringConverter.convert(request.getName()), request.getQuantity());
//            responseObserver.onNext(output);
//            responseObserver.onCompleted();
//        }
//        @Override
//        public void next(Grpc.NullObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
//            System.out.println("UITransferService.next called");
//            Grpc.Snapshot output = ge.next();
//            responseObserver.onNext(output);
//            responseObserver.onCompleted();
//        }
//        @Override
//        public void save(Grpc.NullObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
//            System.out.println("UITransferService.save called");
//            Grpc.Snapshot output = ge.save();
//            responseObserver.onNext(output);
//            responseObserver.onCompleted();
//        }
//        @Override
//        public void load(Grpc.NullObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
//            System.out.println("UITransferService.load called");
//            Grpc.Snapshot output = ge.load();
//            responseObserver.onNext(output);
//            responseObserver.onCompleted();
//        }
//        //        @Override
//        public void back(Grpc.NullObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
//            System.out.println("UITransferService.back called");
//            Grpc.Snapshot output = ge.back();
//            responseObserver.onNext(output);
//            responseObserver.onCompleted();
//        }
//        //        @Override
//        public void quit(Grpc.NullObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
//            System.out.println("UITransferService.quit called");
//            Grpc.Snapshot output = ge.quit();
//            responseObserver.onNext(output);
//            responseObserver.onCompleted();
//        }
//        //        @Override
//        public void init(Grpc.NullObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
//            System.out.println("UITransferService.init called");
//            Grpc.Snapshot output = ge.init();
//            responseObserver.onNext(output);
//            responseObserver.onCompleted();
//        }
//    }
//}

