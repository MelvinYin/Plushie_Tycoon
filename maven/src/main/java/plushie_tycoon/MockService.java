//package plushie_tycoon;
//
//import io.grpc.Server;
//import io.grpc.ServerBuilder;
//import io.grpc.stub.StreamObserver;
//
//import java.io.IOException;
//
//public class MockService {
//    public int portno;
//    MockService(int portno){
//        this.portno = portno;
//    }
//
//    public void run() throws IOException, InterruptedException {
//        ServerBuilder builder = ServerBuilder.forPort(portno);
//        MockService.UITransferService service = new MockService.UITransferService();
//        builder.addService(service);
//        Server server = builder.build();
//        server.start();
//        server.awaitTermination();
//    }
//
//    public static class UITransferService extends UITransferGrpc.UITransferImplBase  {
//        int curr_count = 0;
//        int curr_sign = -1;
//
//        private Grpc.Snapshot getReturn(){
//            return getReturn("update");
//        }
//
//        private Grpc.Snapshot getReturn(String action){
//            curr_count++;
//            curr_sign *= -1;
//            int addition = curr_count * curr_sign;
//
//            String[] resources = {"cloth", "stuffing", "accessory", "packaging"};
//            String[] products = {"aisha", "beta", "chama"};
//            String[] bases = new String[resources.length + products.length];
//            System.arraycopy(resources, 0, bases, 0, resources.length);
//            System.arraycopy(products, 0, bases, resources.length, products.length);
//
//            Grpc.Snapshot.Builder Snapshot = Grpc.Snapshot.newBuilder();
////        prices
//            int count = 0;
//            for (String base: bases){
//                Snapshot.putPrices(base, 10+count+addition);
//                count++;
//            }
//
////        quantities
//            count = 0;
//            for (String base: bases){
//                Snapshot.putQuantities(base, 20+count+addition);
//                count++;
//            }
//
//            //        weights
//            count = 0;
//            for (String base: bases){
//                Snapshot.putWeights(base, 0.1+count*0.01+addition*0.01);
//                count++;
//            }
//
//            //        volumes
//            count = 0;
//            for (String base: bases){
//                Snapshot.putVolumes(base, 0.2+count*0.01+addition*0.01);
//                count++;
//            }
//
//            //        item_cost
//            count = 0;
//            for (String base: bases){
//                Grpc.mItemCost.Builder itemcost = Grpc.mItemCost.newBuilder();
//                itemcost.setMovein(0.3+count*0.01+addition*0.01);
//                itemcost.setMoveout(0.4+count*0.01+addition*0.01);
//                itemcost.setStorage(0.5+count*0.01+addition*0.01);
//                Snapshot.putItemCost(base, itemcost.build());
//                count++;
//            }
//
//            //        resource_ratio
//            count = 0;
//
//            for (String product: products){
//                Grpc.mRatioPerProduct.Builder ratioPerProduct = Grpc.mRatioPerProduct.newBuilder();
//                for (String resource: resources){
//                    ratioPerProduct.putRatio(resource, 1+count);
//                    count++;
//                }
//                Snapshot.putResourceRatio(product, ratioPerProduct.build());
//            }
//
//            Snapshot.setTime(1);
//            Snapshot.setAction(action);
//            Snapshot.setBudget(100000 + addition);
//            Snapshot.setConsoleOutput("console_");
//            return Snapshot.build();
//        }
//
//        @Override
//        public void buy(Grpc.TransactionObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
//            responseObserver.onNext(getReturn());
//            responseObserver.onCompleted();
//        }
//        @Override
//        public void sell(Grpc.TransactionObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
//            responseObserver.onNext(getReturn());
//            responseObserver.onCompleted();
//        }
//        @Override
//        public void make(Grpc.TransactionObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
//            responseObserver.onNext(getReturn());
//            responseObserver.onCompleted();
//        }
//        @Override
//        public void next(Grpc.NullObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
//            responseObserver.onNext(getReturn());
//            responseObserver.onCompleted();
//        }
//        @Override
//        public void save(Grpc.NullObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
//            responseObserver.onNext(getReturn());
//            responseObserver.onCompleted();
//        }
//        @Override
//        public void load(Grpc.NullObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
//            responseObserver.onNext(getReturn());
//            responseObserver.onCompleted();
//        }
//        //        @Override
//        public void back(Grpc.NullObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
//            responseObserver.onNext(getReturn());
//            responseObserver.onCompleted();
//        }
//        //        @Override
//        public void quit(Grpc.NullObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
//            responseObserver.onNext(getReturn());
//            responseObserver.onCompleted();
//        }
//        //        @Override
//        public void init(Grpc.NullObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
//            responseObserver.onNext(getReturn());
//            responseObserver.onCompleted();
//        }
//    }
//}
