//package plushie_tycoon.global.geGlobal.adminServer;
//
//import io.grpc.ManagedChannel;
//import io.grpc.ManagedChannelBuilder;
//import plushie_tycoon.Grpc.NullObject;
//import plushie_tycoon.Grpc.ProposedChanges;
//import plushie_tycoon.AdminSendGrpc.AdminSendBlockingStub;
//import plushie_tycoon.AdminSendGrpc;
//
//public class AdminSender {
//    public static void sendCall(int portno, ProposedChanges changes){
//        AdminSendBlockingStub stub = generateBlockingStub(portno);
//        NullObject nullObject = stub.sendCall(changes);
//        System.out.println("AdminSender.sendCall called with portno " + portno);
//    }
//
//    private static AdminSendBlockingStub generateBlockingStub(int portno){
//        String target = "localhost:" + portno;
//        ManagedChannel channel = ManagedChannelBuilder.forTarget(target).usePlaintext().build();
//        System.out.println("AdminSender.AdminSendBlockingStub called with channel " + channel);
//        return AdminSendGrpc.newBlockingStub(channel);
//    }
//}