package plushie_tycoon;

import io.grpc.Server;
import io.grpc.ServerBuilder;
import io.grpc.stub.StreamObserver;
import java.util.LinkedHashMap;
import plushie_tycoon.serverService.ServerService;

public class PlushieServer {
    public static void main(String[] args) throws Exception {
        int portno = 50051;
        ServerService service = new ServerService(portno);
        service.run();
    }
}
