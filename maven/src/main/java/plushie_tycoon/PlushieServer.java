package plushie_tycoon;

import io.grpc.Server;
import io.grpc.ServerBuilder;
import io.grpc.stub.StreamObserver;
import java.util.LinkedHashMap;


public class PlushieServer {
    public static void main(String[] args) throws Exception {
        int portno = 50051;
        MockService service = new MockService(portno);
        service.run();
    }
}
