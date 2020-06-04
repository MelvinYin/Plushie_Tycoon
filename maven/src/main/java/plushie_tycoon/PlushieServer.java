package plushie_tycoon;

import io.grpc.Server;
import io.grpc.ServerBuilder;
import io.grpc.stub.StreamObserver;
import java.util.LinkedHashMap;

public class PlushieServer {

    public static void main(String[] args) throws Exception {
        ServerBuilder builder = ServerBuilder.forPort(50051);
        UITransferService service = new UITransferService();
        builder.addService(service);
        Server server = builder.build();
        server.start();
        server.awaitTermination();
    }

    private static class UITransferService extends UITransferGrpc.UITransferImplBase  {
        int curr_count = 0;
        int curr_sign = -1;

        private Grpc.UserOutput getReturn(){
            return getReturn("update");
        }

        private Grpc.UserOutput getReturn(String action){
            curr_count++;
            curr_sign *= -1;
            int addition = curr_count * curr_sign;

            String[] resources = {"cloth", "stuffing", "accessories", "packaging"};
            String[] products = {"aisha", "beta", "chama"};
            String[] bases = new String[resources.length + products.length];  //resultant array of size first array and second array
            System.arraycopy(resources, 0, bases, 0, resources.length);
            System.arraycopy(products, 0, bases, resources.length, products.length);

            Grpc.UserOutput.Builder userOutput = Grpc.UserOutput.newBuilder();
//        prices
            int count = 0;
            for (String base: bases){
                userOutput.putPrices(base, 10+count+addition);
                count++;
            }

//        quantities
            count = 0;
            for (String base: bases){
                userOutput.putQuantities(base, 20+count+addition);
                count++;
            }

            //        weights
            count = 0;
            for (String base: bases){
                userOutput.putWeights(base, 0.1+count*0.01+addition*0.01);
                count++;
            }

            //        volumes
            count = 0;
            for (String base: bases){
                userOutput.putVolumes(base, 0.2+count*0.01+addition*0.01);
                count++;
            }

            //        item_cost
            count = 0;
            for (String base: bases){
                Grpc.mItemCost.Builder itemcost = Grpc.mItemCost.newBuilder();
                itemcost.setMovein(0.3+count*0.01+addition*0.01);
                itemcost.setMoveout(0.4+count*0.01+addition*0.01);
                itemcost.setStorage(0.5+count*0.01+addition*0.01);
                userOutput.putItemCost(base, itemcost.build());
                count++;
            }

            //        resource_ratio
            count = 0;

            for (String product: products){
                Grpc.mRatioPerProduct.Builder ratioPerProduct = Grpc.mRatioPerProduct.newBuilder();
                for (String resource: resources){
                    ratioPerProduct.putRatio(resource, 1+count);
                    count++;
                }
                userOutput.putResourceRatio(product, ratioPerProduct.build());
            }

            userOutput.setTime(1);
            userOutput.setAction(action);
            userOutput.setBudget(100000 + addition);
            userOutput.setConsoleOutput("console_");
            return userOutput.build();
        }

        @Override
        public void buy(Grpc.TransactionObject request, StreamObserver<Grpc.UserOutput> responseObserver) {
            responseObserver.onNext(getReturn());
            responseObserver.onCompleted();
        }
        @Override
        public void sell(Grpc.TransactionObject request, StreamObserver<Grpc.UserOutput> responseObserver) {
            responseObserver.onNext(getReturn());
            responseObserver.onCompleted();
        }
        @Override
        public void make(Grpc.TransactionObject request, StreamObserver<Grpc.UserOutput> responseObserver) {
            responseObserver.onNext(getReturn());
            responseObserver.onCompleted();
        }
        @Override
        public void next(Grpc.SelectionObject request, StreamObserver<Grpc.UserOutput> responseObserver) {
            responseObserver.onNext(getReturn());
            responseObserver.onCompleted();
        }
        @Override
        public void save(Grpc.SelectionObject request, StreamObserver<Grpc.UserOutput> responseObserver) {
            responseObserver.onNext(getReturn());
            responseObserver.onCompleted();
        }
        @Override
        public void load(Grpc.SelectionObject request, StreamObserver<Grpc.UserOutput> responseObserver) {
            responseObserver.onNext(getReturn());
            responseObserver.onCompleted();
        }
//        @Override
        public void back(Grpc.SelectionObject request, StreamObserver<Grpc.UserOutput> responseObserver) {
            responseObserver.onNext(getReturn());
            responseObserver.onCompleted();
        }
//        @Override
        public void quit(Grpc.SelectionObject request, StreamObserver<Grpc.UserOutput> responseObserver) {
            responseObserver.onNext(getReturn());
            responseObserver.onCompleted();
        }
//        @Override
        public void init(Grpc.SelectionObject request, StreamObserver<Grpc.UserOutput> responseObserver) {
            responseObserver.onNext(getReturn());
            responseObserver.onCompleted();
        }
    }
}
