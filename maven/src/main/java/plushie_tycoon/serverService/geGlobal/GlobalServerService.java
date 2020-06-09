package plushie_tycoon.serverService.geGlobal;

import io.grpc.Server;
import io.grpc.ServerBuilder;
import io.grpc.stub.StreamObserver;
import plushie_tycoon.Grpc;
import plushie_tycoon.SendCallsGrpc;
import plushie_tycoon.serverService.config.baseObjects.BaseObjects;
import plushie_tycoon.serverService.utils.BaseStringConverter;

import java.io.IOException;
import java.util.HashMap;
//todo user initialisation
public class GlobalServerService {
    private static GEGlobal ge;
    public int portno;

    public GlobalServerService(int portno){
        this.portno = portno;
        ge = new GEGlobal();
    }

    public void run() throws IOException, InterruptedException {
        ServerBuilder builder = ServerBuilder.forPort(portno);
        GlobalServerService.SendCallsService service = new GlobalServerService.SendCallsService();
        builder.addService(service);
        Server server = builder.build();
        server.start();
        server.awaitTermination();
    }

    public static class SendCallsService extends SendCallsGrpc.SendCallsImplBase  {

        @Override
        public void send(Grpc.ProposedChanges request, StreamObserver<Grpc.ReturnCode> responseObserver) {
            HashMap<BaseObjects, Integer> buySellOrders = new HashMap<>();
            for (HashMap.Entry<String, Integer> entry: request.getBuySellMap().entrySet()){
                buySellOrders.put(BaseStringConverter.convert(entry.getKey()), entry.getValue());
            }
            HashMap<BaseObjects, Integer> makeOrders = new HashMap<>();
            for (HashMap.Entry<String, Integer> entry: request.getMakeMap().entrySet()){
                makeOrders.put(BaseStringConverter.convert(entry.getKey()), entry.getValue());
            }

            Grpc.ReturnCode output = ge.addCall(request.getUserid(), buySellOrders, makeOrders);
            responseObserver.onNext(output);
            responseObserver.onCompleted();
        }
        @Override
        public void query(Grpc.UserID request, StreamObserver<Grpc.Snapshot> responseObserver) {
            Grpc.Snapshot output = ge.query(request.getUserid());
            responseObserver.onNext(output);
            responseObserver.onCompleted();
        }

        @Override
        public void register(Grpc.UserID request, StreamObserver<Grpc.Snapshot> responseObserver) {
            Grpc.Snapshot output = ge.register(request.getUserid());
            responseObserver.onNext(output);
            responseObserver.onCompleted();
        }

        @Override
        public void isregistered(Grpc.UserID request, StreamObserver<Grpc.ReturnCode> responseObserver) {
            boolean returnCode = ge.isRegistered(request.getUserid());
            Grpc.ReturnCode output = Grpc.ReturnCode.newBuilder().setCode(returnCode).build();
            responseObserver.onNext(output);
            responseObserver.onCompleted();
        }

        @Override
        public void getTime(Grpc.SelectionObject request, StreamObserver<Grpc.IntObject> responseObserver) {
            int time = ge.getTime();
            Grpc.IntObject output = Grpc.IntObject.newBuilder().setItem(time).build();
            responseObserver.onNext(output);
            responseObserver.onCompleted();
        }

        @Override
        public void hasUpdate(Grpc.UserID request, StreamObserver<Grpc.ReturnCode> responseObserver) {
            boolean returnCode = ge.hasUpdate(request.getUserid());
            Grpc.ReturnCode output = Grpc.ReturnCode.newBuilder().setCode(returnCode).build();
            responseObserver.onNext(output);
            responseObserver.onCompleted();
        }
    }
}

