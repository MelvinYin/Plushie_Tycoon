package plushie_tycoon.serverService;

import io.grpc.Server;
import io.grpc.ServerBuilder;
import io.grpc.stub.StreamObserver;
import jdk.internal.net.http.common.Pair;
import plushie_tycoon.Grpc;
import plushie_tycoon.MockService;
import plushie_tycoon.UITransferGrpc;
import plushie_tycoon.serverService.config.baseObjects.BaseObjects;
import plushie_tycoon.serverService.config.baseObjects.Products;
import plushie_tycoon.serverService.config.baseObjects.Resources;

import java.io.IOException;
import java.util.HashMap;

public class ServerService {
    private static GE ge;
    public int portno;

    ServerService(int portno){
        this.portno = portno;
        ge = new GE();
    }

    public void run() throws IOException, InterruptedException {
        ServerBuilder builder = ServerBuilder.forPort(portno);
        MockService.UITransferService service = new MockService.UITransferService();
        builder.addService(service);
        Server server = builder.build();
        server.start();
        server.awaitTermination();
    }

    private static Pair<BaseObjects, Integer> GrpcRequestToGeAdapter(Grpc.TransactionObject request){
//        convert it to a grpc enum class eventually, and then a project-wide json config file.
        HashMap<String, BaseObjects> strToBaseObjects = new HashMap<>();
        strToBaseObjects.put("stuffing", Resources.STUFFING);
        strToBaseObjects.put("accessory", Resources.ACCESSORY);
        strToBaseObjects.put("packaging", Resources.PACKAGING);
        strToBaseObjects.put("cloth", Resources.CLOTH);
        strToBaseObjects.put("aisha", Products.AISHA);
        strToBaseObjects.put("beta", Products.BETA);
        strToBaseObjects.put("chama", Products.CHAMA);
        BaseObjects baseObject = strToBaseObjects.get(request.getName());
        int quantity = request.getQuantity();
        return new Pair<>(baseObject, quantity);
    }

    public static class UITransferService extends UITransferGrpc.UITransferImplBase  {

        @Override
        public void buy(Grpc.TransactionObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
            Pair<BaseObjects, Integer> converted = GrpcRequestToGeAdapter(request);
            Grpc.Snapshot output = ge.buy(converted.first, converted.second);
            responseObserver.onNext(output);
            responseObserver.onCompleted();
        }
        @Override
        public void sell(Grpc.TransactionObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
            Pair<BaseObjects, Integer> converted = GrpcRequestToGeAdapter(request);
            Grpc.Snapshot output = ge.sell(converted.first, converted.second);
            responseObserver.onNext(output);
            responseObserver.onCompleted();
        }
        @Override
        public void make(Grpc.TransactionObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
            Pair<BaseObjects, Integer> converted = GrpcRequestToGeAdapter(request);
            Grpc.Snapshot output = ge.make(converted.first, converted.second);
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
            responseObserver.onNext(output);
            responseObserver.onCompleted();
        }
    }
}

