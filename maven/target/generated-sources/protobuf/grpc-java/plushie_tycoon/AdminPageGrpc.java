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
public final class AdminPageGrpc {

  private AdminPageGrpc() {}

  public static final String SERVICE_NAME = "plushie_tycoon.AdminPage";

  // Static method descriptors that strictly reflect the proto.
  private static volatile io.grpc.MethodDescriptor<plushie_tycoon.Grpc.NullObject,
      plushie_tycoon.Grpc.ProposedChanges> getGetCallMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "getCall",
      requestType = plushie_tycoon.Grpc.NullObject.class,
      responseType = plushie_tycoon.Grpc.ProposedChanges.class,
      methodType = io.grpc.MethodDescriptor.MethodType.SERVER_STREAMING)
  public static io.grpc.MethodDescriptor<plushie_tycoon.Grpc.NullObject,
      plushie_tycoon.Grpc.ProposedChanges> getGetCallMethod() {
    io.grpc.MethodDescriptor<plushie_tycoon.Grpc.NullObject, plushie_tycoon.Grpc.ProposedChanges> getGetCallMethod;
    if ((getGetCallMethod = AdminPageGrpc.getGetCallMethod) == null) {
      synchronized (AdminPageGrpc.class) {
        if ((getGetCallMethod = AdminPageGrpc.getGetCallMethod) == null) {
          AdminPageGrpc.getGetCallMethod = getGetCallMethod =
              io.grpc.MethodDescriptor.<plushie_tycoon.Grpc.NullObject, plushie_tycoon.Grpc.ProposedChanges>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.SERVER_STREAMING)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "getCall"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.NullObject.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.ProposedChanges.getDefaultInstance()))
              .setSchemaDescriptor(new AdminPageMethodDescriptorSupplier("getCall"))
              .build();
        }
      }
    }
    return getGetCallMethod;
  }

  private static volatile io.grpc.MethodDescriptor<plushie_tycoon.Grpc.NullObject,
      plushie_tycoon.Grpc.ReturnCode> getNextTurnMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "nextTurn",
      requestType = plushie_tycoon.Grpc.NullObject.class,
      responseType = plushie_tycoon.Grpc.ReturnCode.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<plushie_tycoon.Grpc.NullObject,
      plushie_tycoon.Grpc.ReturnCode> getNextTurnMethod() {
    io.grpc.MethodDescriptor<plushie_tycoon.Grpc.NullObject, plushie_tycoon.Grpc.ReturnCode> getNextTurnMethod;
    if ((getNextTurnMethod = AdminPageGrpc.getNextTurnMethod) == null) {
      synchronized (AdminPageGrpc.class) {
        if ((getNextTurnMethod = AdminPageGrpc.getNextTurnMethod) == null) {
          AdminPageGrpc.getNextTurnMethod = getNextTurnMethod =
              io.grpc.MethodDescriptor.<plushie_tycoon.Grpc.NullObject, plushie_tycoon.Grpc.ReturnCode>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "nextTurn"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.NullObject.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.ReturnCode.getDefaultInstance()))
              .setSchemaDescriptor(new AdminPageMethodDescriptorSupplier("nextTurn"))
              .build();
        }
      }
    }
    return getNextTurnMethod;
  }

  private static volatile io.grpc.MethodDescriptor<plushie_tycoon.Grpc.NullObject,
      plushie_tycoon.Grpc.NullObject> getPingMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "ping",
      requestType = plushie_tycoon.Grpc.NullObject.class,
      responseType = plushie_tycoon.Grpc.NullObject.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<plushie_tycoon.Grpc.NullObject,
      plushie_tycoon.Grpc.NullObject> getPingMethod() {
    io.grpc.MethodDescriptor<plushie_tycoon.Grpc.NullObject, plushie_tycoon.Grpc.NullObject> getPingMethod;
    if ((getPingMethod = AdminPageGrpc.getPingMethod) == null) {
      synchronized (AdminPageGrpc.class) {
        if ((getPingMethod = AdminPageGrpc.getPingMethod) == null) {
          AdminPageGrpc.getPingMethod = getPingMethod =
              io.grpc.MethodDescriptor.<plushie_tycoon.Grpc.NullObject, plushie_tycoon.Grpc.NullObject>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "ping"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.NullObject.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.NullObject.getDefaultInstance()))
              .setSchemaDescriptor(new AdminPageMethodDescriptorSupplier("ping"))
              .build();
        }
      }
    }
    return getPingMethod;
  }

  /**
   * Creates a new async stub that supports all call types for the service
   */
  public static AdminPageStub newStub(io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<AdminPageStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<AdminPageStub>() {
        @java.lang.Override
        public AdminPageStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new AdminPageStub(channel, callOptions);
        }
      };
    return AdminPageStub.newStub(factory, channel);
  }

  /**
   * Creates a new blocking-style stub that supports unary and streaming output calls on the service
   */
  public static AdminPageBlockingStub newBlockingStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<AdminPageBlockingStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<AdminPageBlockingStub>() {
        @java.lang.Override
        public AdminPageBlockingStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new AdminPageBlockingStub(channel, callOptions);
        }
      };
    return AdminPageBlockingStub.newStub(factory, channel);
  }

  /**
   * Creates a new ListenableFuture-style stub that supports unary calls on the service
   */
  public static AdminPageFutureStub newFutureStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<AdminPageFutureStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<AdminPageFutureStub>() {
        @java.lang.Override
        public AdminPageFutureStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new AdminPageFutureStub(channel, callOptions);
        }
      };
    return AdminPageFutureStub.newStub(factory, channel);
  }

  /**
   */
  public static abstract class AdminPageImplBase implements io.grpc.BindableService {

    /**
     */
    public void getCall(plushie_tycoon.Grpc.NullObject request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.ProposedChanges> responseObserver) {
      asyncUnimplementedUnaryCall(getGetCallMethod(), responseObserver);
    }

    /**
     */
    public void nextTurn(plushie_tycoon.Grpc.NullObject request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.ReturnCode> responseObserver) {
      asyncUnimplementedUnaryCall(getNextTurnMethod(), responseObserver);
    }

    /**
     */
    public void ping(plushie_tycoon.Grpc.NullObject request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.NullObject> responseObserver) {
      asyncUnimplementedUnaryCall(getPingMethod(), responseObserver);
    }

    @java.lang.Override public final io.grpc.ServerServiceDefinition bindService() {
      return io.grpc.ServerServiceDefinition.builder(getServiceDescriptor())
          .addMethod(
            getGetCallMethod(),
            asyncServerStreamingCall(
              new MethodHandlers<
                plushie_tycoon.Grpc.NullObject,
                plushie_tycoon.Grpc.ProposedChanges>(
                  this, METHODID_GET_CALL)))
          .addMethod(
            getNextTurnMethod(),
            asyncUnaryCall(
              new MethodHandlers<
                plushie_tycoon.Grpc.NullObject,
                plushie_tycoon.Grpc.ReturnCode>(
                  this, METHODID_NEXT_TURN)))
          .addMethod(
            getPingMethod(),
            asyncUnaryCall(
              new MethodHandlers<
                plushie_tycoon.Grpc.NullObject,
                plushie_tycoon.Grpc.NullObject>(
                  this, METHODID_PING)))
          .build();
    }
  }

  /**
   */
  public static final class AdminPageStub extends io.grpc.stub.AbstractAsyncStub<AdminPageStub> {
    private AdminPageStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected AdminPageStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new AdminPageStub(channel, callOptions);
    }

    /**
     */
    public void getCall(plushie_tycoon.Grpc.NullObject request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.ProposedChanges> responseObserver) {
      asyncServerStreamingCall(
          getChannel().newCall(getGetCallMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void nextTurn(plushie_tycoon.Grpc.NullObject request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.ReturnCode> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(getNextTurnMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void ping(plushie_tycoon.Grpc.NullObject request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.NullObject> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(getPingMethod(), getCallOptions()), request, responseObserver);
    }
  }

  /**
   */
  public static final class AdminPageBlockingStub extends io.grpc.stub.AbstractBlockingStub<AdminPageBlockingStub> {
    private AdminPageBlockingStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected AdminPageBlockingStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new AdminPageBlockingStub(channel, callOptions);
    }

    /**
     */
    public java.util.Iterator<plushie_tycoon.Grpc.ProposedChanges> getCall(
        plushie_tycoon.Grpc.NullObject request) {
      return blockingServerStreamingCall(
          getChannel(), getGetCallMethod(), getCallOptions(), request);
    }

    /**
     */
    public plushie_tycoon.Grpc.ReturnCode nextTurn(plushie_tycoon.Grpc.NullObject request) {
      return blockingUnaryCall(
          getChannel(), getNextTurnMethod(), getCallOptions(), request);
    }

    /**
     */
    public plushie_tycoon.Grpc.NullObject ping(plushie_tycoon.Grpc.NullObject request) {
      return blockingUnaryCall(
          getChannel(), getPingMethod(), getCallOptions(), request);
    }
  }

  /**
   */
  public static final class AdminPageFutureStub extends io.grpc.stub.AbstractFutureStub<AdminPageFutureStub> {
    private AdminPageFutureStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected AdminPageFutureStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new AdminPageFutureStub(channel, callOptions);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<plushie_tycoon.Grpc.ReturnCode> nextTurn(
        plushie_tycoon.Grpc.NullObject request) {
      return futureUnaryCall(
          getChannel().newCall(getNextTurnMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<plushie_tycoon.Grpc.NullObject> ping(
        plushie_tycoon.Grpc.NullObject request) {
      return futureUnaryCall(
          getChannel().newCall(getPingMethod(), getCallOptions()), request);
    }
  }

  private static final int METHODID_GET_CALL = 0;
  private static final int METHODID_NEXT_TURN = 1;
  private static final int METHODID_PING = 2;

  private static final class MethodHandlers<Req, Resp> implements
      io.grpc.stub.ServerCalls.UnaryMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ServerStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ClientStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.BidiStreamingMethod<Req, Resp> {
    private final AdminPageImplBase serviceImpl;
    private final int methodId;

    MethodHandlers(AdminPageImplBase serviceImpl, int methodId) {
      this.serviceImpl = serviceImpl;
      this.methodId = methodId;
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public void invoke(Req request, io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        case METHODID_GET_CALL:
          serviceImpl.getCall((plushie_tycoon.Grpc.NullObject) request,
              (io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.ProposedChanges>) responseObserver);
          break;
        case METHODID_NEXT_TURN:
          serviceImpl.nextTurn((plushie_tycoon.Grpc.NullObject) request,
              (io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.ReturnCode>) responseObserver);
          break;
        case METHODID_PING:
          serviceImpl.ping((plushie_tycoon.Grpc.NullObject) request,
              (io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.NullObject>) responseObserver);
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

  private static abstract class AdminPageBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoFileDescriptorSupplier, io.grpc.protobuf.ProtoServiceDescriptorSupplier {
    AdminPageBaseDescriptorSupplier() {}

    @java.lang.Override
    public com.google.protobuf.Descriptors.FileDescriptor getFileDescriptor() {
      return plushie_tycoon.Grpc.getDescriptor();
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.ServiceDescriptor getServiceDescriptor() {
      return getFileDescriptor().findServiceByName("AdminPage");
    }
  }

  private static final class AdminPageFileDescriptorSupplier
      extends AdminPageBaseDescriptorSupplier {
    AdminPageFileDescriptorSupplier() {}
  }

  private static final class AdminPageMethodDescriptorSupplier
      extends AdminPageBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoMethodDescriptorSupplier {
    private final String methodName;

    AdminPageMethodDescriptorSupplier(String methodName) {
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
      synchronized (AdminPageGrpc.class) {
        result = serviceDescriptor;
        if (result == null) {
          serviceDescriptor = result = io.grpc.ServiceDescriptor.newBuilder(SERVICE_NAME)
              .setSchemaDescriptor(new AdminPageFileDescriptorSupplier())
              .addMethod(getGetCallMethod())
              .addMethod(getNextTurnMethod())
              .addMethod(getPingMethod())
              .build();
        }
      }
    }
    return result;
  }
}
