package plushie_tycoon;

import static io.grpc.MethodDescriptor.generateFullMethodName;
import static io.grpc.stub.ClientCalls.asyncBidiStreamingCall;
import static io.grpc.stub.ClientCalls.asyncClientStreamingCall;
import static io.grpc.stub.ClientCalls.asyncServerStreamingCall;
import static io.grpc.stub.ClientCalls.asyncUnaryCall;
import static io.grpc.stub.ClientCalls.blockingServerStreamingCall;
import static io.grpc.stub.ClientCalls.blockingUnaryCall;
import static io.grpc.stub.ClientCalls.futureUnaryCall;
import static io.grpc.stub.ServerCalls.asyncBidiStreamingCall;
import static io.grpc.stub.ServerCalls.asyncClientStreamingCall;
import static io.grpc.stub.ServerCalls.asyncServerStreamingCall;
import static io.grpc.stub.ServerCalls.asyncUnaryCall;
import static io.grpc.stub.ServerCalls.asyncUnimplementedStreamingCall;
import static io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall;

/**
 */
@javax.annotation.Generated(
    value = "by gRPC proto compiler (version 1.29.0)",
    comments = "Source: grpc.proto")
public final class SendCallsGrpc {

  private SendCallsGrpc() {}

  public static final String SERVICE_NAME = "plushie_tycoon.SendCalls";

  // Static method descriptors that strictly reflect the proto.
  private static volatile io.grpc.MethodDescriptor<plushie_tycoon.Grpc.ProposedChanges,
      plushie_tycoon.Grpc.ReturnCode> getSendMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "send",
      requestType = plushie_tycoon.Grpc.ProposedChanges.class,
      responseType = plushie_tycoon.Grpc.ReturnCode.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<plushie_tycoon.Grpc.ProposedChanges,
      plushie_tycoon.Grpc.ReturnCode> getSendMethod() {
    io.grpc.MethodDescriptor<plushie_tycoon.Grpc.ProposedChanges, plushie_tycoon.Grpc.ReturnCode> getSendMethod;
    if ((getSendMethod = SendCallsGrpc.getSendMethod) == null) {
      synchronized (SendCallsGrpc.class) {
        if ((getSendMethod = SendCallsGrpc.getSendMethod) == null) {
          SendCallsGrpc.getSendMethod = getSendMethod =
              io.grpc.MethodDescriptor.<plushie_tycoon.Grpc.ProposedChanges, plushie_tycoon.Grpc.ReturnCode>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "send"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.ProposedChanges.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.ReturnCode.getDefaultInstance()))
              .setSchemaDescriptor(new SendCallsMethodDescriptorSupplier("send"))
              .build();
        }
      }
    }
    return getSendMethod;
  }

  private static volatile io.grpc.MethodDescriptor<plushie_tycoon.Grpc.UserID,
      plushie_tycoon.Grpc.Snapshot> getQueryMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "query",
      requestType = plushie_tycoon.Grpc.UserID.class,
      responseType = plushie_tycoon.Grpc.Snapshot.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<plushie_tycoon.Grpc.UserID,
      plushie_tycoon.Grpc.Snapshot> getQueryMethod() {
    io.grpc.MethodDescriptor<plushie_tycoon.Grpc.UserID, plushie_tycoon.Grpc.Snapshot> getQueryMethod;
    if ((getQueryMethod = SendCallsGrpc.getQueryMethod) == null) {
      synchronized (SendCallsGrpc.class) {
        if ((getQueryMethod = SendCallsGrpc.getQueryMethod) == null) {
          SendCallsGrpc.getQueryMethod = getQueryMethod =
              io.grpc.MethodDescriptor.<plushie_tycoon.Grpc.UserID, plushie_tycoon.Grpc.Snapshot>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "query"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.UserID.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.Snapshot.getDefaultInstance()))
              .setSchemaDescriptor(new SendCallsMethodDescriptorSupplier("query"))
              .build();
        }
      }
    }
    return getQueryMethod;
  }

  private static volatile io.grpc.MethodDescriptor<plushie_tycoon.Grpc.TimeCheck,
      plushie_tycoon.Grpc.ReturnCode> getTimeCheckMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "timeCheck",
      requestType = plushie_tycoon.Grpc.TimeCheck.class,
      responseType = plushie_tycoon.Grpc.ReturnCode.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<plushie_tycoon.Grpc.TimeCheck,
      plushie_tycoon.Grpc.ReturnCode> getTimeCheckMethod() {
    io.grpc.MethodDescriptor<plushie_tycoon.Grpc.TimeCheck, plushie_tycoon.Grpc.ReturnCode> getTimeCheckMethod;
    if ((getTimeCheckMethod = SendCallsGrpc.getTimeCheckMethod) == null) {
      synchronized (SendCallsGrpc.class) {
        if ((getTimeCheckMethod = SendCallsGrpc.getTimeCheckMethod) == null) {
          SendCallsGrpc.getTimeCheckMethod = getTimeCheckMethod =
              io.grpc.MethodDescriptor.<plushie_tycoon.Grpc.TimeCheck, plushie_tycoon.Grpc.ReturnCode>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "timeCheck"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.TimeCheck.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.ReturnCode.getDefaultInstance()))
              .setSchemaDescriptor(new SendCallsMethodDescriptorSupplier("timeCheck"))
              .build();
        }
      }
    }
    return getTimeCheckMethod;
  }

  private static volatile io.grpc.MethodDescriptor<plushie_tycoon.Grpc.UserID,
      plushie_tycoon.Grpc.ReturnCode> getHasUpdateMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "hasUpdate",
      requestType = plushie_tycoon.Grpc.UserID.class,
      responseType = plushie_tycoon.Grpc.ReturnCode.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<plushie_tycoon.Grpc.UserID,
      plushie_tycoon.Grpc.ReturnCode> getHasUpdateMethod() {
    io.grpc.MethodDescriptor<plushie_tycoon.Grpc.UserID, plushie_tycoon.Grpc.ReturnCode> getHasUpdateMethod;
    if ((getHasUpdateMethod = SendCallsGrpc.getHasUpdateMethod) == null) {
      synchronized (SendCallsGrpc.class) {
        if ((getHasUpdateMethod = SendCallsGrpc.getHasUpdateMethod) == null) {
          SendCallsGrpc.getHasUpdateMethod = getHasUpdateMethod =
              io.grpc.MethodDescriptor.<plushie_tycoon.Grpc.UserID, plushie_tycoon.Grpc.ReturnCode>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "hasUpdate"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.UserID.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.ReturnCode.getDefaultInstance()))
              .setSchemaDescriptor(new SendCallsMethodDescriptorSupplier("hasUpdate"))
              .build();
        }
      }
    }
    return getHasUpdateMethod;
  }

  /**
   * Creates a new async stub that supports all call types for the service
   */
  public static SendCallsStub newStub(io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<SendCallsStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<SendCallsStub>() {
        @java.lang.Override
        public SendCallsStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new SendCallsStub(channel, callOptions);
        }
      };
    return SendCallsStub.newStub(factory, channel);
  }

  /**
   * Creates a new blocking-style stub that supports unary and streaming output calls on the service
   */
  public static SendCallsBlockingStub newBlockingStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<SendCallsBlockingStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<SendCallsBlockingStub>() {
        @java.lang.Override
        public SendCallsBlockingStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new SendCallsBlockingStub(channel, callOptions);
        }
      };
    return SendCallsBlockingStub.newStub(factory, channel);
  }

  /**
   * Creates a new ListenableFuture-style stub that supports unary calls on the service
   */
  public static SendCallsFutureStub newFutureStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<SendCallsFutureStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<SendCallsFutureStub>() {
        @java.lang.Override
        public SendCallsFutureStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new SendCallsFutureStub(channel, callOptions);
        }
      };
    return SendCallsFutureStub.newStub(factory, channel);
  }

  /**
   */
  public static abstract class SendCallsImplBase implements io.grpc.BindableService {

    /**
     */
    public void send(plushie_tycoon.Grpc.ProposedChanges request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.ReturnCode> responseObserver) {
      asyncUnimplementedUnaryCall(getSendMethod(), responseObserver);
    }

    /**
     */
    public void query(plushie_tycoon.Grpc.UserID request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot> responseObserver) {
      asyncUnimplementedUnaryCall(getQueryMethod(), responseObserver);
    }

    /**
     */
    public void timeCheck(plushie_tycoon.Grpc.TimeCheck request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.ReturnCode> responseObserver) {
      asyncUnimplementedUnaryCall(getTimeCheckMethod(), responseObserver);
    }

    /**
     */
    public void hasUpdate(plushie_tycoon.Grpc.UserID request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.ReturnCode> responseObserver) {
      asyncUnimplementedUnaryCall(getHasUpdateMethod(), responseObserver);
    }

    @java.lang.Override public final io.grpc.ServerServiceDefinition bindService() {
      return io.grpc.ServerServiceDefinition.builder(getServiceDescriptor())
          .addMethod(
            getSendMethod(),
            asyncUnaryCall(
              new MethodHandlers<
                plushie_tycoon.Grpc.ProposedChanges,
                plushie_tycoon.Grpc.ReturnCode>(
                  this, METHODID_SEND)))
          .addMethod(
            getQueryMethod(),
            asyncUnaryCall(
              new MethodHandlers<
                plushie_tycoon.Grpc.UserID,
                plushie_tycoon.Grpc.Snapshot>(
                  this, METHODID_QUERY)))
          .addMethod(
            getTimeCheckMethod(),
            asyncUnaryCall(
              new MethodHandlers<
                plushie_tycoon.Grpc.TimeCheck,
                plushie_tycoon.Grpc.ReturnCode>(
                  this, METHODID_TIME_CHECK)))
          .addMethod(
            getHasUpdateMethod(),
            asyncUnaryCall(
              new MethodHandlers<
                plushie_tycoon.Grpc.UserID,
                plushie_tycoon.Grpc.ReturnCode>(
                  this, METHODID_HAS_UPDATE)))
          .build();
    }
  }

  /**
   */
  public static final class SendCallsStub extends io.grpc.stub.AbstractAsyncStub<SendCallsStub> {
    private SendCallsStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected SendCallsStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new SendCallsStub(channel, callOptions);
    }

    /**
     */
    public void send(plushie_tycoon.Grpc.ProposedChanges request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.ReturnCode> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(getSendMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void query(plushie_tycoon.Grpc.UserID request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(getQueryMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void timeCheck(plushie_tycoon.Grpc.TimeCheck request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.ReturnCode> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(getTimeCheckMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void hasUpdate(plushie_tycoon.Grpc.UserID request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.ReturnCode> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(getHasUpdateMethod(), getCallOptions()), request, responseObserver);
    }
  }

  /**
   */
  public static final class SendCallsBlockingStub extends io.grpc.stub.AbstractBlockingStub<SendCallsBlockingStub> {
    private SendCallsBlockingStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected SendCallsBlockingStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new SendCallsBlockingStub(channel, callOptions);
    }

    /**
     */
    public plushie_tycoon.Grpc.ReturnCode send(plushie_tycoon.Grpc.ProposedChanges request) {
      return blockingUnaryCall(
          getChannel(), getSendMethod(), getCallOptions(), request);
    }

    /**
     */
    public plushie_tycoon.Grpc.Snapshot query(plushie_tycoon.Grpc.UserID request) {
      return blockingUnaryCall(
          getChannel(), getQueryMethod(), getCallOptions(), request);
    }

    /**
     */
    public plushie_tycoon.Grpc.ReturnCode timeCheck(plushie_tycoon.Grpc.TimeCheck request) {
      return blockingUnaryCall(
          getChannel(), getTimeCheckMethod(), getCallOptions(), request);
    }

    /**
     */
    public plushie_tycoon.Grpc.ReturnCode hasUpdate(plushie_tycoon.Grpc.UserID request) {
      return blockingUnaryCall(
          getChannel(), getHasUpdateMethod(), getCallOptions(), request);
    }
  }

  /**
   */
  public static final class SendCallsFutureStub extends io.grpc.stub.AbstractFutureStub<SendCallsFutureStub> {
    private SendCallsFutureStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected SendCallsFutureStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new SendCallsFutureStub(channel, callOptions);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<plushie_tycoon.Grpc.ReturnCode> send(
        plushie_tycoon.Grpc.ProposedChanges request) {
      return futureUnaryCall(
          getChannel().newCall(getSendMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<plushie_tycoon.Grpc.Snapshot> query(
        plushie_tycoon.Grpc.UserID request) {
      return futureUnaryCall(
          getChannel().newCall(getQueryMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<plushie_tycoon.Grpc.ReturnCode> timeCheck(
        plushie_tycoon.Grpc.TimeCheck request) {
      return futureUnaryCall(
          getChannel().newCall(getTimeCheckMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<plushie_tycoon.Grpc.ReturnCode> hasUpdate(
        plushie_tycoon.Grpc.UserID request) {
      return futureUnaryCall(
          getChannel().newCall(getHasUpdateMethod(), getCallOptions()), request);
    }
  }

  private static final int METHODID_SEND = 0;
  private static final int METHODID_QUERY = 1;
  private static final int METHODID_TIME_CHECK = 2;
  private static final int METHODID_HAS_UPDATE = 3;

  private static final class MethodHandlers<Req, Resp> implements
      io.grpc.stub.ServerCalls.UnaryMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ServerStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ClientStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.BidiStreamingMethod<Req, Resp> {
    private final SendCallsImplBase serviceImpl;
    private final int methodId;

    MethodHandlers(SendCallsImplBase serviceImpl, int methodId) {
      this.serviceImpl = serviceImpl;
      this.methodId = methodId;
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public void invoke(Req request, io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        case METHODID_SEND:
          serviceImpl.send((plushie_tycoon.Grpc.ProposedChanges) request,
              (io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.ReturnCode>) responseObserver);
          break;
        case METHODID_QUERY:
          serviceImpl.query((plushie_tycoon.Grpc.UserID) request,
              (io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot>) responseObserver);
          break;
        case METHODID_TIME_CHECK:
          serviceImpl.timeCheck((plushie_tycoon.Grpc.TimeCheck) request,
              (io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.ReturnCode>) responseObserver);
          break;
        case METHODID_HAS_UPDATE:
          serviceImpl.hasUpdate((plushie_tycoon.Grpc.UserID) request,
              (io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.ReturnCode>) responseObserver);
          break;
        default:
          throw new AssertionError();
      }
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public io.grpc.stub.StreamObserver<Req> invoke(
        io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        default:
          throw new AssertionError();
      }
    }
  }

  private static abstract class SendCallsBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoFileDescriptorSupplier, io.grpc.protobuf.ProtoServiceDescriptorSupplier {
    SendCallsBaseDescriptorSupplier() {}

    @java.lang.Override
    public com.google.protobuf.Descriptors.FileDescriptor getFileDescriptor() {
      return plushie_tycoon.Grpc.getDescriptor();
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.ServiceDescriptor getServiceDescriptor() {
      return getFileDescriptor().findServiceByName("SendCalls");
    }
  }

  private static final class SendCallsFileDescriptorSupplier
      extends SendCallsBaseDescriptorSupplier {
    SendCallsFileDescriptorSupplier() {}
  }

  private static final class SendCallsMethodDescriptorSupplier
      extends SendCallsBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoMethodDescriptorSupplier {
    private final String methodName;

    SendCallsMethodDescriptorSupplier(String methodName) {
      this.methodName = methodName;
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.MethodDescriptor getMethodDescriptor() {
      return getServiceDescriptor().findMethodByName(methodName);
    }
  }

  private static volatile io.grpc.ServiceDescriptor serviceDescriptor;

  public static io.grpc.ServiceDescriptor getServiceDescriptor() {
    io.grpc.ServiceDescriptor result = serviceDescriptor;
    if (result == null) {
      synchronized (SendCallsGrpc.class) {
        result = serviceDescriptor;
        if (result == null) {
          serviceDescriptor = result = io.grpc.ServiceDescriptor.newBuilder(SERVICE_NAME)
              .setSchemaDescriptor(new SendCallsFileDescriptorSupplier())
              .addMethod(getSendMethod())
              .addMethod(getQueryMethod())
              .addMethod(getTimeCheckMethod())
              .addMethod(getHasUpdateMethod())
              .build();
        }
      }
    }
    return result;
  }
}
