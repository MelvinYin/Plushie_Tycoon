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
public final class ClientToHostGrpc {

  private ClientToHostGrpc() {}

  public static final String SERVICE_NAME = "plushie_tycoon.ClientToHost";

  // Static method descriptors that strictly reflect the proto.
  private static volatile io.grpc.MethodDescriptor<plushie_tycoon.Grpc.UserID,
      plushie_tycoon.Grpc.Snapshot> getRegisterMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "register",
      requestType = plushie_tycoon.Grpc.UserID.class,
      responseType = plushie_tycoon.Grpc.Snapshot.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<plushie_tycoon.Grpc.UserID,
      plushie_tycoon.Grpc.Snapshot> getRegisterMethod() {
    io.grpc.MethodDescriptor<plushie_tycoon.Grpc.UserID, plushie_tycoon.Grpc.Snapshot> getRegisterMethod;
    if ((getRegisterMethod = ClientToHostGrpc.getRegisterMethod) == null) {
      synchronized (ClientToHostGrpc.class) {
        if ((getRegisterMethod = ClientToHostGrpc.getRegisterMethod) == null) {
          ClientToHostGrpc.getRegisterMethod = getRegisterMethod =
              io.grpc.MethodDescriptor.<plushie_tycoon.Grpc.UserID, plushie_tycoon.Grpc.Snapshot>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "register"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.UserID.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.Snapshot.getDefaultInstance()))
              .setSchemaDescriptor(new ClientToHostMethodDescriptorSupplier("register"))
              .build();
        }
      }
    }
    return getRegisterMethod;
  }

  private static volatile io.grpc.MethodDescriptor<plushie_tycoon.Grpc.UserID,
      plushie_tycoon.Grpc.ReturnCode> getIsregisteredMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "isregistered",
      requestType = plushie_tycoon.Grpc.UserID.class,
      responseType = plushie_tycoon.Grpc.ReturnCode.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<plushie_tycoon.Grpc.UserID,
      plushie_tycoon.Grpc.ReturnCode> getIsregisteredMethod() {
    io.grpc.MethodDescriptor<plushie_tycoon.Grpc.UserID, plushie_tycoon.Grpc.ReturnCode> getIsregisteredMethod;
    if ((getIsregisteredMethod = ClientToHostGrpc.getIsregisteredMethod) == null) {
      synchronized (ClientToHostGrpc.class) {
        if ((getIsregisteredMethod = ClientToHostGrpc.getIsregisteredMethod) == null) {
          ClientToHostGrpc.getIsregisteredMethod = getIsregisteredMethod =
              io.grpc.MethodDescriptor.<plushie_tycoon.Grpc.UserID, plushie_tycoon.Grpc.ReturnCode>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "isregistered"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.UserID.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.ReturnCode.getDefaultInstance()))
              .setSchemaDescriptor(new ClientToHostMethodDescriptorSupplier("isregistered"))
              .build();
        }
      }
    }
    return getIsregisteredMethod;
  }

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
    if ((getSendMethod = ClientToHostGrpc.getSendMethod) == null) {
      synchronized (ClientToHostGrpc.class) {
        if ((getSendMethod = ClientToHostGrpc.getSendMethod) == null) {
          ClientToHostGrpc.getSendMethod = getSendMethod =
              io.grpc.MethodDescriptor.<plushie_tycoon.Grpc.ProposedChanges, plushie_tycoon.Grpc.ReturnCode>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "send"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.ProposedChanges.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.ReturnCode.getDefaultInstance()))
              .setSchemaDescriptor(new ClientToHostMethodDescriptorSupplier("send"))
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
    if ((getQueryMethod = ClientToHostGrpc.getQueryMethod) == null) {
      synchronized (ClientToHostGrpc.class) {
        if ((getQueryMethod = ClientToHostGrpc.getQueryMethod) == null) {
          ClientToHostGrpc.getQueryMethod = getQueryMethod =
              io.grpc.MethodDescriptor.<plushie_tycoon.Grpc.UserID, plushie_tycoon.Grpc.Snapshot>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "query"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.UserID.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.Snapshot.getDefaultInstance()))
              .setSchemaDescriptor(new ClientToHostMethodDescriptorSupplier("query"))
              .build();
        }
      }
    }
    return getQueryMethod;
  }

  private static volatile io.grpc.MethodDescriptor<plushie_tycoon.Grpc.NullObject,
      plushie_tycoon.Grpc.IntObject> getGetTimeMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "getTime",
      requestType = plushie_tycoon.Grpc.NullObject.class,
      responseType = plushie_tycoon.Grpc.IntObject.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<plushie_tycoon.Grpc.NullObject,
      plushie_tycoon.Grpc.IntObject> getGetTimeMethod() {
    io.grpc.MethodDescriptor<plushie_tycoon.Grpc.NullObject, plushie_tycoon.Grpc.IntObject> getGetTimeMethod;
    if ((getGetTimeMethod = ClientToHostGrpc.getGetTimeMethod) == null) {
      synchronized (ClientToHostGrpc.class) {
        if ((getGetTimeMethod = ClientToHostGrpc.getGetTimeMethod) == null) {
          ClientToHostGrpc.getGetTimeMethod = getGetTimeMethod =
              io.grpc.MethodDescriptor.<plushie_tycoon.Grpc.NullObject, plushie_tycoon.Grpc.IntObject>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "getTime"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.NullObject.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.IntObject.getDefaultInstance()))
              .setSchemaDescriptor(new ClientToHostMethodDescriptorSupplier("getTime"))
              .build();
        }
      }
    }
    return getGetTimeMethod;
  }

  private static volatile io.grpc.MethodDescriptor<plushie_tycoon.Grpc.UserID,
      plushie_tycoon.Grpc.ReturnCode> getHasUpdatedMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "hasUpdated",
      requestType = plushie_tycoon.Grpc.UserID.class,
      responseType = plushie_tycoon.Grpc.ReturnCode.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<plushie_tycoon.Grpc.UserID,
      plushie_tycoon.Grpc.ReturnCode> getHasUpdatedMethod() {
    io.grpc.MethodDescriptor<plushie_tycoon.Grpc.UserID, plushie_tycoon.Grpc.ReturnCode> getHasUpdatedMethod;
    if ((getHasUpdatedMethod = ClientToHostGrpc.getHasUpdatedMethod) == null) {
      synchronized (ClientToHostGrpc.class) {
        if ((getHasUpdatedMethod = ClientToHostGrpc.getHasUpdatedMethod) == null) {
          ClientToHostGrpc.getHasUpdatedMethod = getHasUpdatedMethod =
              io.grpc.MethodDescriptor.<plushie_tycoon.Grpc.UserID, plushie_tycoon.Grpc.ReturnCode>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "hasUpdated"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.UserID.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.ReturnCode.getDefaultInstance()))
              .setSchemaDescriptor(new ClientToHostMethodDescriptorSupplier("hasUpdated"))
              .build();
        }
      }
    }
    return getHasUpdatedMethod;
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
    if ((getPingMethod = ClientToHostGrpc.getPingMethod) == null) {
      synchronized (ClientToHostGrpc.class) {
        if ((getPingMethod = ClientToHostGrpc.getPingMethod) == null) {
          ClientToHostGrpc.getPingMethod = getPingMethod =
              io.grpc.MethodDescriptor.<plushie_tycoon.Grpc.NullObject, plushie_tycoon.Grpc.NullObject>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "ping"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.NullObject.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.NullObject.getDefaultInstance()))
              .setSchemaDescriptor(new ClientToHostMethodDescriptorSupplier("ping"))
              .build();
        }
      }
    }
    return getPingMethod;
  }

  /**
   * Creates a new async stub that supports all call types for the service
   */
  public static ClientToHostStub newStub(io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<ClientToHostStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<ClientToHostStub>() {
        @java.lang.Override
        public ClientToHostStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new ClientToHostStub(channel, callOptions);
        }
      };
    return ClientToHostStub.newStub(factory, channel);
  }

  /**
   * Creates a new blocking-style stub that supports unary and streaming output calls on the service
   */
  public static ClientToHostBlockingStub newBlockingStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<ClientToHostBlockingStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<ClientToHostBlockingStub>() {
        @java.lang.Override
        public ClientToHostBlockingStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new ClientToHostBlockingStub(channel, callOptions);
        }
      };
    return ClientToHostBlockingStub.newStub(factory, channel);
  }

  /**
   * Creates a new ListenableFuture-style stub that supports unary calls on the service
   */
  public static ClientToHostFutureStub newFutureStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<ClientToHostFutureStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<ClientToHostFutureStub>() {
        @java.lang.Override
        public ClientToHostFutureStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new ClientToHostFutureStub(channel, callOptions);
        }
      };
    return ClientToHostFutureStub.newStub(factory, channel);
  }

  /**
   */
  public static abstract class ClientToHostImplBase implements io.grpc.BindableService {

    /**
     */
    public void register(plushie_tycoon.Grpc.UserID request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot> responseObserver) {
      asyncUnimplementedUnaryCall(getRegisterMethod(), responseObserver);
    }

    /**
     */
    public void isregistered(plushie_tycoon.Grpc.UserID request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.ReturnCode> responseObserver) {
      asyncUnimplementedUnaryCall(getIsregisteredMethod(), responseObserver);
    }

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
    public void getTime(plushie_tycoon.Grpc.NullObject request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.IntObject> responseObserver) {
      asyncUnimplementedUnaryCall(getGetTimeMethod(), responseObserver);
    }

    /**
     */
    public void hasUpdated(plushie_tycoon.Grpc.UserID request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.ReturnCode> responseObserver) {
      asyncUnimplementedUnaryCall(getHasUpdatedMethod(), responseObserver);
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
            getRegisterMethod(),
            asyncUnaryCall(
              new MethodHandlers<
                plushie_tycoon.Grpc.UserID,
                plushie_tycoon.Grpc.Snapshot>(
                  this, METHODID_REGISTER)))
          .addMethod(
            getIsregisteredMethod(),
            asyncUnaryCall(
              new MethodHandlers<
                plushie_tycoon.Grpc.UserID,
                plushie_tycoon.Grpc.ReturnCode>(
                  this, METHODID_ISREGISTERED)))
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
            getGetTimeMethod(),
            asyncUnaryCall(
              new MethodHandlers<
                plushie_tycoon.Grpc.NullObject,
                plushie_tycoon.Grpc.IntObject>(
                  this, METHODID_GET_TIME)))
          .addMethod(
            getHasUpdatedMethod(),
            asyncUnaryCall(
              new MethodHandlers<
                plushie_tycoon.Grpc.UserID,
                plushie_tycoon.Grpc.ReturnCode>(
                  this, METHODID_HAS_UPDATED)))
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
  public static final class ClientToHostStub extends io.grpc.stub.AbstractAsyncStub<ClientToHostStub> {
    private ClientToHostStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected ClientToHostStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new ClientToHostStub(channel, callOptions);
    }

    /**
     */
    public void register(plushie_tycoon.Grpc.UserID request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(getRegisterMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void isregistered(plushie_tycoon.Grpc.UserID request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.ReturnCode> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(getIsregisteredMethod(), getCallOptions()), request, responseObserver);
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
    public void getTime(plushie_tycoon.Grpc.NullObject request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.IntObject> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(getGetTimeMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void hasUpdated(plushie_tycoon.Grpc.UserID request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.ReturnCode> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(getHasUpdatedMethod(), getCallOptions()), request, responseObserver);
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
  public static final class ClientToHostBlockingStub extends io.grpc.stub.AbstractBlockingStub<ClientToHostBlockingStub> {
    private ClientToHostBlockingStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected ClientToHostBlockingStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new ClientToHostBlockingStub(channel, callOptions);
    }

    /**
     */
    public plushie_tycoon.Grpc.Snapshot register(plushie_tycoon.Grpc.UserID request) {
      return blockingUnaryCall(
          getChannel(), getRegisterMethod(), getCallOptions(), request);
    }

    /**
     */
    public plushie_tycoon.Grpc.ReturnCode isregistered(plushie_tycoon.Grpc.UserID request) {
      return blockingUnaryCall(
          getChannel(), getIsregisteredMethod(), getCallOptions(), request);
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
    public plushie_tycoon.Grpc.IntObject getTime(plushie_tycoon.Grpc.NullObject request) {
      return blockingUnaryCall(
          getChannel(), getGetTimeMethod(), getCallOptions(), request);
    }

    /**
     */
    public plushie_tycoon.Grpc.ReturnCode hasUpdated(plushie_tycoon.Grpc.UserID request) {
      return blockingUnaryCall(
          getChannel(), getHasUpdatedMethod(), getCallOptions(), request);
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
  public static final class ClientToHostFutureStub extends io.grpc.stub.AbstractFutureStub<ClientToHostFutureStub> {
    private ClientToHostFutureStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected ClientToHostFutureStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new ClientToHostFutureStub(channel, callOptions);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<plushie_tycoon.Grpc.Snapshot> register(
        plushie_tycoon.Grpc.UserID request) {
      return futureUnaryCall(
          getChannel().newCall(getRegisterMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<plushie_tycoon.Grpc.ReturnCode> isregistered(
        plushie_tycoon.Grpc.UserID request) {
      return futureUnaryCall(
          getChannel().newCall(getIsregisteredMethod(), getCallOptions()), request);
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
    public com.google.common.util.concurrent.ListenableFuture<plushie_tycoon.Grpc.IntObject> getTime(
        plushie_tycoon.Grpc.NullObject request) {
      return futureUnaryCall(
          getChannel().newCall(getGetTimeMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<plushie_tycoon.Grpc.ReturnCode> hasUpdated(
        plushie_tycoon.Grpc.UserID request) {
      return futureUnaryCall(
          getChannel().newCall(getHasUpdatedMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<plushie_tycoon.Grpc.NullObject> ping(
        plushie_tycoon.Grpc.NullObject request) {
      return futureUnaryCall(
          getChannel().newCall(getPingMethod(), getCallOptions()), request);
    }
  }

  private static final int METHODID_REGISTER = 0;
  private static final int METHODID_ISREGISTERED = 1;
  private static final int METHODID_SEND = 2;
  private static final int METHODID_QUERY = 3;
  private static final int METHODID_GET_TIME = 4;
  private static final int METHODID_HAS_UPDATED = 5;
  private static final int METHODID_PING = 6;

  private static final class MethodHandlers<Req, Resp> implements
      io.grpc.stub.ServerCalls.UnaryMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ServerStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ClientStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.BidiStreamingMethod<Req, Resp> {
    private final ClientToHostImplBase serviceImpl;
    private final int methodId;

    MethodHandlers(ClientToHostImplBase serviceImpl, int methodId) {
      this.serviceImpl = serviceImpl;
      this.methodId = methodId;
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public void invoke(Req request, io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        case METHODID_REGISTER:
          serviceImpl.register((plushie_tycoon.Grpc.UserID) request,
              (io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot>) responseObserver);
          break;
        case METHODID_ISREGISTERED:
          serviceImpl.isregistered((plushie_tycoon.Grpc.UserID) request,
              (io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.ReturnCode>) responseObserver);
          break;
        case METHODID_SEND:
          serviceImpl.send((plushie_tycoon.Grpc.ProposedChanges) request,
              (io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.ReturnCode>) responseObserver);
          break;
        case METHODID_QUERY:
          serviceImpl.query((plushie_tycoon.Grpc.UserID) request,
              (io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot>) responseObserver);
          break;
        case METHODID_GET_TIME:
          serviceImpl.getTime((plushie_tycoon.Grpc.NullObject) request,
              (io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.IntObject>) responseObserver);
          break;
        case METHODID_HAS_UPDATED:
          serviceImpl.hasUpdated((plushie_tycoon.Grpc.UserID) request,
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

  private static abstract class ClientToHostBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoFileDescriptorSupplier, io.grpc.protobuf.ProtoServiceDescriptorSupplier {
    ClientToHostBaseDescriptorSupplier() {}

    @java.lang.Override
    public com.google.protobuf.Descriptors.FileDescriptor getFileDescriptor() {
      return plushie_tycoon.Grpc.getDescriptor();
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.ServiceDescriptor getServiceDescriptor() {
      return getFileDescriptor().findServiceByName("ClientToHost");
    }
  }

  private static final class ClientToHostFileDescriptorSupplier
      extends ClientToHostBaseDescriptorSupplier {
    ClientToHostFileDescriptorSupplier() {}
  }

  private static final class ClientToHostMethodDescriptorSupplier
      extends ClientToHostBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoMethodDescriptorSupplier {
    private final String methodName;

    ClientToHostMethodDescriptorSupplier(String methodName) {
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
      synchronized (ClientToHostGrpc.class) {
        result = serviceDescriptor;
        if (result == null) {
          serviceDescriptor = result = io.grpc.ServiceDescriptor.newBuilder(SERVICE_NAME)
              .setSchemaDescriptor(new ClientToHostFileDescriptorSupplier())
              .addMethod(getRegisterMethod())
              .addMethod(getIsregisteredMethod())
              .addMethod(getSendMethod())
              .addMethod(getQueryMethod())
              .addMethod(getGetTimeMethod())
              .addMethod(getHasUpdatedMethod())
              .addMethod(getPingMethod())
              .build();
        }
      }
    }
    return result;
  }
}
