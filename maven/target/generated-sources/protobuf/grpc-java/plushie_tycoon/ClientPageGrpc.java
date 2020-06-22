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
 * <pre>
 *todo: map in proto is not ordered. Perhaps switch to 2 repeated fields?
 *or alternatively we can provide an order object somewhere
 * </pre>
 */
@javax.annotation.Generated(
    value = "by gRPC proto compiler (version 1.29.0)",
    comments = "Source: grpc.proto")
public final class ClientPageGrpc {

  private ClientPageGrpc() {}

  public static final String SERVICE_NAME = "plushie_tycoon.ClientPage";

  // Static method descriptors that strictly reflect the proto.
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
    if ((getPingMethod = ClientPageGrpc.getPingMethod) == null) {
      synchronized (ClientPageGrpc.class) {
        if ((getPingMethod = ClientPageGrpc.getPingMethod) == null) {
          ClientPageGrpc.getPingMethod = getPingMethod =
              io.grpc.MethodDescriptor.<plushie_tycoon.Grpc.NullObject, plushie_tycoon.Grpc.NullObject>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "ping"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.NullObject.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.NullObject.getDefaultInstance()))
              .setSchemaDescriptor(new ClientPageMethodDescriptorSupplier("ping"))
              .build();
        }
      }
    }
    return getPingMethod;
  }

  private static volatile io.grpc.MethodDescriptor<plushie_tycoon.Grpc.TransactionObject,
      plushie_tycoon.Grpc.Snapshot> getBuyMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "buy",
      requestType = plushie_tycoon.Grpc.TransactionObject.class,
      responseType = plushie_tycoon.Grpc.Snapshot.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<plushie_tycoon.Grpc.TransactionObject,
      plushie_tycoon.Grpc.Snapshot> getBuyMethod() {
    io.grpc.MethodDescriptor<plushie_tycoon.Grpc.TransactionObject, plushie_tycoon.Grpc.Snapshot> getBuyMethod;
    if ((getBuyMethod = ClientPageGrpc.getBuyMethod) == null) {
      synchronized (ClientPageGrpc.class) {
        if ((getBuyMethod = ClientPageGrpc.getBuyMethod) == null) {
          ClientPageGrpc.getBuyMethod = getBuyMethod =
              io.grpc.MethodDescriptor.<plushie_tycoon.Grpc.TransactionObject, plushie_tycoon.Grpc.Snapshot>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "buy"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.TransactionObject.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.Snapshot.getDefaultInstance()))
              .setSchemaDescriptor(new ClientPageMethodDescriptorSupplier("buy"))
              .build();
        }
      }
    }
    return getBuyMethod;
  }

  private static volatile io.grpc.MethodDescriptor<plushie_tycoon.Grpc.TransactionObject,
      plushie_tycoon.Grpc.Snapshot> getSellMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "sell",
      requestType = plushie_tycoon.Grpc.TransactionObject.class,
      responseType = plushie_tycoon.Grpc.Snapshot.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<plushie_tycoon.Grpc.TransactionObject,
      plushie_tycoon.Grpc.Snapshot> getSellMethod() {
    io.grpc.MethodDescriptor<plushie_tycoon.Grpc.TransactionObject, plushie_tycoon.Grpc.Snapshot> getSellMethod;
    if ((getSellMethod = ClientPageGrpc.getSellMethod) == null) {
      synchronized (ClientPageGrpc.class) {
        if ((getSellMethod = ClientPageGrpc.getSellMethod) == null) {
          ClientPageGrpc.getSellMethod = getSellMethod =
              io.grpc.MethodDescriptor.<plushie_tycoon.Grpc.TransactionObject, plushie_tycoon.Grpc.Snapshot>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "sell"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.TransactionObject.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.Snapshot.getDefaultInstance()))
              .setSchemaDescriptor(new ClientPageMethodDescriptorSupplier("sell"))
              .build();
        }
      }
    }
    return getSellMethod;
  }

  private static volatile io.grpc.MethodDescriptor<plushie_tycoon.Grpc.TransactionObject,
      plushie_tycoon.Grpc.Snapshot> getMakeMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "make",
      requestType = plushie_tycoon.Grpc.TransactionObject.class,
      responseType = plushie_tycoon.Grpc.Snapshot.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<plushie_tycoon.Grpc.TransactionObject,
      plushie_tycoon.Grpc.Snapshot> getMakeMethod() {
    io.grpc.MethodDescriptor<plushie_tycoon.Grpc.TransactionObject, plushie_tycoon.Grpc.Snapshot> getMakeMethod;
    if ((getMakeMethod = ClientPageGrpc.getMakeMethod) == null) {
      synchronized (ClientPageGrpc.class) {
        if ((getMakeMethod = ClientPageGrpc.getMakeMethod) == null) {
          ClientPageGrpc.getMakeMethod = getMakeMethod =
              io.grpc.MethodDescriptor.<plushie_tycoon.Grpc.TransactionObject, plushie_tycoon.Grpc.Snapshot>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "make"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.TransactionObject.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.Snapshot.getDefaultInstance()))
              .setSchemaDescriptor(new ClientPageMethodDescriptorSupplier("make"))
              .build();
        }
      }
    }
    return getMakeMethod;
  }

  private static volatile io.grpc.MethodDescriptor<plushie_tycoon.Grpc.NullObject,
      plushie_tycoon.Grpc.Snapshot> getNextMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "next",
      requestType = plushie_tycoon.Grpc.NullObject.class,
      responseType = plushie_tycoon.Grpc.Snapshot.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<plushie_tycoon.Grpc.NullObject,
      plushie_tycoon.Grpc.Snapshot> getNextMethod() {
    io.grpc.MethodDescriptor<plushie_tycoon.Grpc.NullObject, plushie_tycoon.Grpc.Snapshot> getNextMethod;
    if ((getNextMethod = ClientPageGrpc.getNextMethod) == null) {
      synchronized (ClientPageGrpc.class) {
        if ((getNextMethod = ClientPageGrpc.getNextMethod) == null) {
          ClientPageGrpc.getNextMethod = getNextMethod =
              io.grpc.MethodDescriptor.<plushie_tycoon.Grpc.NullObject, plushie_tycoon.Grpc.Snapshot>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "next"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.NullObject.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.Snapshot.getDefaultInstance()))
              .setSchemaDescriptor(new ClientPageMethodDescriptorSupplier("next"))
              .build();
        }
      }
    }
    return getNextMethod;
  }

  private static volatile io.grpc.MethodDescriptor<plushie_tycoon.Grpc.NullObject,
      plushie_tycoon.Grpc.Snapshot> getSaveMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "save",
      requestType = plushie_tycoon.Grpc.NullObject.class,
      responseType = plushie_tycoon.Grpc.Snapshot.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<plushie_tycoon.Grpc.NullObject,
      plushie_tycoon.Grpc.Snapshot> getSaveMethod() {
    io.grpc.MethodDescriptor<plushie_tycoon.Grpc.NullObject, plushie_tycoon.Grpc.Snapshot> getSaveMethod;
    if ((getSaveMethod = ClientPageGrpc.getSaveMethod) == null) {
      synchronized (ClientPageGrpc.class) {
        if ((getSaveMethod = ClientPageGrpc.getSaveMethod) == null) {
          ClientPageGrpc.getSaveMethod = getSaveMethod =
              io.grpc.MethodDescriptor.<plushie_tycoon.Grpc.NullObject, plushie_tycoon.Grpc.Snapshot>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "save"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.NullObject.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.Snapshot.getDefaultInstance()))
              .setSchemaDescriptor(new ClientPageMethodDescriptorSupplier("save"))
              .build();
        }
      }
    }
    return getSaveMethod;
  }

  private static volatile io.grpc.MethodDescriptor<plushie_tycoon.Grpc.NullObject,
      plushie_tycoon.Grpc.Snapshot> getLoadMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "load",
      requestType = plushie_tycoon.Grpc.NullObject.class,
      responseType = plushie_tycoon.Grpc.Snapshot.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<plushie_tycoon.Grpc.NullObject,
      plushie_tycoon.Grpc.Snapshot> getLoadMethod() {
    io.grpc.MethodDescriptor<plushie_tycoon.Grpc.NullObject, plushie_tycoon.Grpc.Snapshot> getLoadMethod;
    if ((getLoadMethod = ClientPageGrpc.getLoadMethod) == null) {
      synchronized (ClientPageGrpc.class) {
        if ((getLoadMethod = ClientPageGrpc.getLoadMethod) == null) {
          ClientPageGrpc.getLoadMethod = getLoadMethod =
              io.grpc.MethodDescriptor.<plushie_tycoon.Grpc.NullObject, plushie_tycoon.Grpc.Snapshot>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "load"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.NullObject.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.Snapshot.getDefaultInstance()))
              .setSchemaDescriptor(new ClientPageMethodDescriptorSupplier("load"))
              .build();
        }
      }
    }
    return getLoadMethod;
  }

  private static volatile io.grpc.MethodDescriptor<plushie_tycoon.Grpc.NullObject,
      plushie_tycoon.Grpc.Snapshot> getBackMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "back",
      requestType = plushie_tycoon.Grpc.NullObject.class,
      responseType = plushie_tycoon.Grpc.Snapshot.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<plushie_tycoon.Grpc.NullObject,
      plushie_tycoon.Grpc.Snapshot> getBackMethod() {
    io.grpc.MethodDescriptor<plushie_tycoon.Grpc.NullObject, plushie_tycoon.Grpc.Snapshot> getBackMethod;
    if ((getBackMethod = ClientPageGrpc.getBackMethod) == null) {
      synchronized (ClientPageGrpc.class) {
        if ((getBackMethod = ClientPageGrpc.getBackMethod) == null) {
          ClientPageGrpc.getBackMethod = getBackMethod =
              io.grpc.MethodDescriptor.<plushie_tycoon.Grpc.NullObject, plushie_tycoon.Grpc.Snapshot>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "back"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.NullObject.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.Snapshot.getDefaultInstance()))
              .setSchemaDescriptor(new ClientPageMethodDescriptorSupplier("back"))
              .build();
        }
      }
    }
    return getBackMethod;
  }

  private static volatile io.grpc.MethodDescriptor<plushie_tycoon.Grpc.NullObject,
      plushie_tycoon.Grpc.Snapshot> getQuitMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "quit",
      requestType = plushie_tycoon.Grpc.NullObject.class,
      responseType = plushie_tycoon.Grpc.Snapshot.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<plushie_tycoon.Grpc.NullObject,
      plushie_tycoon.Grpc.Snapshot> getQuitMethod() {
    io.grpc.MethodDescriptor<plushie_tycoon.Grpc.NullObject, plushie_tycoon.Grpc.Snapshot> getQuitMethod;
    if ((getQuitMethod = ClientPageGrpc.getQuitMethod) == null) {
      synchronized (ClientPageGrpc.class) {
        if ((getQuitMethod = ClientPageGrpc.getQuitMethod) == null) {
          ClientPageGrpc.getQuitMethod = getQuitMethod =
              io.grpc.MethodDescriptor.<plushie_tycoon.Grpc.NullObject, plushie_tycoon.Grpc.Snapshot>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "quit"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.NullObject.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.Snapshot.getDefaultInstance()))
              .setSchemaDescriptor(new ClientPageMethodDescriptorSupplier("quit"))
              .build();
        }
      }
    }
    return getQuitMethod;
  }

  private static volatile io.grpc.MethodDescriptor<plushie_tycoon.Grpc.NullObject,
      plushie_tycoon.Grpc.Snapshot> getInitMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "init",
      requestType = plushie_tycoon.Grpc.NullObject.class,
      responseType = plushie_tycoon.Grpc.Snapshot.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<plushie_tycoon.Grpc.NullObject,
      plushie_tycoon.Grpc.Snapshot> getInitMethod() {
    io.grpc.MethodDescriptor<plushie_tycoon.Grpc.NullObject, plushie_tycoon.Grpc.Snapshot> getInitMethod;
    if ((getInitMethod = ClientPageGrpc.getInitMethod) == null) {
      synchronized (ClientPageGrpc.class) {
        if ((getInitMethod = ClientPageGrpc.getInitMethod) == null) {
          ClientPageGrpc.getInitMethod = getInitMethod =
              io.grpc.MethodDescriptor.<plushie_tycoon.Grpc.NullObject, plushie_tycoon.Grpc.Snapshot>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "init"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.NullObject.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.Snapshot.getDefaultInstance()))
              .setSchemaDescriptor(new ClientPageMethodDescriptorSupplier("init"))
              .build();
        }
      }
    }
    return getInitMethod;
  }

  /**
   * Creates a new async stub that supports all call types for the service
   */
  public static ClientPageStub newStub(io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<ClientPageStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<ClientPageStub>() {
        @java.lang.Override
        public ClientPageStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new ClientPageStub(channel, callOptions);
        }
      };
    return ClientPageStub.newStub(factory, channel);
  }

  /**
   * Creates a new blocking-style stub that supports unary and streaming output calls on the service
   */
  public static ClientPageBlockingStub newBlockingStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<ClientPageBlockingStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<ClientPageBlockingStub>() {
        @java.lang.Override
        public ClientPageBlockingStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new ClientPageBlockingStub(channel, callOptions);
        }
      };
    return ClientPageBlockingStub.newStub(factory, channel);
  }

  /**
   * Creates a new ListenableFuture-style stub that supports unary calls on the service
   */
  public static ClientPageFutureStub newFutureStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<ClientPageFutureStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<ClientPageFutureStub>() {
        @java.lang.Override
        public ClientPageFutureStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new ClientPageFutureStub(channel, callOptions);
        }
      };
    return ClientPageFutureStub.newStub(factory, channel);
  }

  /**
   * <pre>
   *todo: map in proto is not ordered. Perhaps switch to 2 repeated fields?
   *or alternatively we can provide an order object somewhere
   * </pre>
   */
  public static abstract class ClientPageImplBase implements io.grpc.BindableService {

    /**
     */
    public void ping(plushie_tycoon.Grpc.NullObject request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.NullObject> responseObserver) {
      asyncUnimplementedUnaryCall(getPingMethod(), responseObserver);
    }

    /**
     */
    public void buy(plushie_tycoon.Grpc.TransactionObject request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot> responseObserver) {
      asyncUnimplementedUnaryCall(getBuyMethod(), responseObserver);
    }

    /**
     */
    public void sell(plushie_tycoon.Grpc.TransactionObject request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot> responseObserver) {
      asyncUnimplementedUnaryCall(getSellMethod(), responseObserver);
    }

    /**
     */
    public void make(plushie_tycoon.Grpc.TransactionObject request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot> responseObserver) {
      asyncUnimplementedUnaryCall(getMakeMethod(), responseObserver);
    }

    /**
     */
    public void next(plushie_tycoon.Grpc.NullObject request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot> responseObserver) {
      asyncUnimplementedUnaryCall(getNextMethod(), responseObserver);
    }

    /**
     */
    public void save(plushie_tycoon.Grpc.NullObject request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot> responseObserver) {
      asyncUnimplementedUnaryCall(getSaveMethod(), responseObserver);
    }

    /**
     */
    public void load(plushie_tycoon.Grpc.NullObject request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot> responseObserver) {
      asyncUnimplementedUnaryCall(getLoadMethod(), responseObserver);
    }

    /**
     */
    public void back(plushie_tycoon.Grpc.NullObject request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot> responseObserver) {
      asyncUnimplementedUnaryCall(getBackMethod(), responseObserver);
    }

    /**
     */
    public void quit(plushie_tycoon.Grpc.NullObject request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot> responseObserver) {
      asyncUnimplementedUnaryCall(getQuitMethod(), responseObserver);
    }

    /**
     */
    public void init(plushie_tycoon.Grpc.NullObject request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot> responseObserver) {
      asyncUnimplementedUnaryCall(getInitMethod(), responseObserver);
    }

    @java.lang.Override public final io.grpc.ServerServiceDefinition bindService() {
      return io.grpc.ServerServiceDefinition.builder(getServiceDescriptor())
          .addMethod(
            getPingMethod(),
            asyncUnaryCall(
              new MethodHandlers<
                plushie_tycoon.Grpc.NullObject,
                plushie_tycoon.Grpc.NullObject>(
                  this, METHODID_PING)))
          .addMethod(
            getBuyMethod(),
            asyncUnaryCall(
              new MethodHandlers<
                plushie_tycoon.Grpc.TransactionObject,
                plushie_tycoon.Grpc.Snapshot>(
                  this, METHODID_BUY)))
          .addMethod(
            getSellMethod(),
            asyncUnaryCall(
              new MethodHandlers<
                plushie_tycoon.Grpc.TransactionObject,
                plushie_tycoon.Grpc.Snapshot>(
                  this, METHODID_SELL)))
          .addMethod(
            getMakeMethod(),
            asyncUnaryCall(
              new MethodHandlers<
                plushie_tycoon.Grpc.TransactionObject,
                plushie_tycoon.Grpc.Snapshot>(
                  this, METHODID_MAKE)))
          .addMethod(
            getNextMethod(),
            asyncUnaryCall(
              new MethodHandlers<
                plushie_tycoon.Grpc.NullObject,
                plushie_tycoon.Grpc.Snapshot>(
                  this, METHODID_NEXT)))
          .addMethod(
            getSaveMethod(),
            asyncUnaryCall(
              new MethodHandlers<
                plushie_tycoon.Grpc.NullObject,
                plushie_tycoon.Grpc.Snapshot>(
                  this, METHODID_SAVE)))
          .addMethod(
            getLoadMethod(),
            asyncUnaryCall(
              new MethodHandlers<
                plushie_tycoon.Grpc.NullObject,
                plushie_tycoon.Grpc.Snapshot>(
                  this, METHODID_LOAD)))
          .addMethod(
            getBackMethod(),
            asyncUnaryCall(
              new MethodHandlers<
                plushie_tycoon.Grpc.NullObject,
                plushie_tycoon.Grpc.Snapshot>(
                  this, METHODID_BACK)))
          .addMethod(
            getQuitMethod(),
            asyncUnaryCall(
              new MethodHandlers<
                plushie_tycoon.Grpc.NullObject,
                plushie_tycoon.Grpc.Snapshot>(
                  this, METHODID_QUIT)))
          .addMethod(
            getInitMethod(),
            asyncUnaryCall(
              new MethodHandlers<
                plushie_tycoon.Grpc.NullObject,
                plushie_tycoon.Grpc.Snapshot>(
                  this, METHODID_INIT)))
          .build();
    }
  }

  /**
   * <pre>
   *todo: map in proto is not ordered. Perhaps switch to 2 repeated fields?
   *or alternatively we can provide an order object somewhere
   * </pre>
   */
  public static final class ClientPageStub extends io.grpc.stub.AbstractAsyncStub<ClientPageStub> {
    private ClientPageStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected ClientPageStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new ClientPageStub(channel, callOptions);
    }

    /**
     */
    public void ping(plushie_tycoon.Grpc.NullObject request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.NullObject> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(getPingMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void buy(plushie_tycoon.Grpc.TransactionObject request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(getBuyMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void sell(plushie_tycoon.Grpc.TransactionObject request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(getSellMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void make(plushie_tycoon.Grpc.TransactionObject request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(getMakeMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void next(plushie_tycoon.Grpc.NullObject request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(getNextMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void save(plushie_tycoon.Grpc.NullObject request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(getSaveMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void load(plushie_tycoon.Grpc.NullObject request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(getLoadMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void back(plushie_tycoon.Grpc.NullObject request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(getBackMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void quit(plushie_tycoon.Grpc.NullObject request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(getQuitMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void init(plushie_tycoon.Grpc.NullObject request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(getInitMethod(), getCallOptions()), request, responseObserver);
    }
  }

  /**
   * <pre>
   *todo: map in proto is not ordered. Perhaps switch to 2 repeated fields?
   *or alternatively we can provide an order object somewhere
   * </pre>
   */
  public static final class ClientPageBlockingStub extends io.grpc.stub.AbstractBlockingStub<ClientPageBlockingStub> {
    private ClientPageBlockingStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected ClientPageBlockingStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new ClientPageBlockingStub(channel, callOptions);
    }

    /**
     */
    public plushie_tycoon.Grpc.NullObject ping(plushie_tycoon.Grpc.NullObject request) {
      return blockingUnaryCall(
          getChannel(), getPingMethod(), getCallOptions(), request);
    }

    /**
     */
    public plushie_tycoon.Grpc.Snapshot buy(plushie_tycoon.Grpc.TransactionObject request) {
      return blockingUnaryCall(
          getChannel(), getBuyMethod(), getCallOptions(), request);
    }

    /**
     */
    public plushie_tycoon.Grpc.Snapshot sell(plushie_tycoon.Grpc.TransactionObject request) {
      return blockingUnaryCall(
          getChannel(), getSellMethod(), getCallOptions(), request);
    }

    /**
     */
    public plushie_tycoon.Grpc.Snapshot make(plushie_tycoon.Grpc.TransactionObject request) {
      return blockingUnaryCall(
          getChannel(), getMakeMethod(), getCallOptions(), request);
    }

    /**
     */
    public plushie_tycoon.Grpc.Snapshot next(plushie_tycoon.Grpc.NullObject request) {
      return blockingUnaryCall(
          getChannel(), getNextMethod(), getCallOptions(), request);
    }

    /**
     */
    public plushie_tycoon.Grpc.Snapshot save(plushie_tycoon.Grpc.NullObject request) {
      return blockingUnaryCall(
          getChannel(), getSaveMethod(), getCallOptions(), request);
    }

    /**
     */
    public plushie_tycoon.Grpc.Snapshot load(plushie_tycoon.Grpc.NullObject request) {
      return blockingUnaryCall(
          getChannel(), getLoadMethod(), getCallOptions(), request);
    }

    /**
     */
    public plushie_tycoon.Grpc.Snapshot back(plushie_tycoon.Grpc.NullObject request) {
      return blockingUnaryCall(
          getChannel(), getBackMethod(), getCallOptions(), request);
    }

    /**
     */
    public plushie_tycoon.Grpc.Snapshot quit(plushie_tycoon.Grpc.NullObject request) {
      return blockingUnaryCall(
          getChannel(), getQuitMethod(), getCallOptions(), request);
    }

    /**
     */
    public plushie_tycoon.Grpc.Snapshot init(plushie_tycoon.Grpc.NullObject request) {
      return blockingUnaryCall(
          getChannel(), getInitMethod(), getCallOptions(), request);
    }
  }

  /**
   * <pre>
   *todo: map in proto is not ordered. Perhaps switch to 2 repeated fields?
   *or alternatively we can provide an order object somewhere
   * </pre>
   */
  public static final class ClientPageFutureStub extends io.grpc.stub.AbstractFutureStub<ClientPageFutureStub> {
    private ClientPageFutureStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected ClientPageFutureStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new ClientPageFutureStub(channel, callOptions);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<plushie_tycoon.Grpc.NullObject> ping(
        plushie_tycoon.Grpc.NullObject request) {
      return futureUnaryCall(
          getChannel().newCall(getPingMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<plushie_tycoon.Grpc.Snapshot> buy(
        plushie_tycoon.Grpc.TransactionObject request) {
      return futureUnaryCall(
          getChannel().newCall(getBuyMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<plushie_tycoon.Grpc.Snapshot> sell(
        plushie_tycoon.Grpc.TransactionObject request) {
      return futureUnaryCall(
          getChannel().newCall(getSellMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<plushie_tycoon.Grpc.Snapshot> make(
        plushie_tycoon.Grpc.TransactionObject request) {
      return futureUnaryCall(
          getChannel().newCall(getMakeMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<plushie_tycoon.Grpc.Snapshot> next(
        plushie_tycoon.Grpc.NullObject request) {
      return futureUnaryCall(
          getChannel().newCall(getNextMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<plushie_tycoon.Grpc.Snapshot> save(
        plushie_tycoon.Grpc.NullObject request) {
      return futureUnaryCall(
          getChannel().newCall(getSaveMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<plushie_tycoon.Grpc.Snapshot> load(
        plushie_tycoon.Grpc.NullObject request) {
      return futureUnaryCall(
          getChannel().newCall(getLoadMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<plushie_tycoon.Grpc.Snapshot> back(
        plushie_tycoon.Grpc.NullObject request) {
      return futureUnaryCall(
          getChannel().newCall(getBackMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<plushie_tycoon.Grpc.Snapshot> quit(
        plushie_tycoon.Grpc.NullObject request) {
      return futureUnaryCall(
          getChannel().newCall(getQuitMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<plushie_tycoon.Grpc.Snapshot> init(
        plushie_tycoon.Grpc.NullObject request) {
      return futureUnaryCall(
          getChannel().newCall(getInitMethod(), getCallOptions()), request);
    }
  }

  private static final int METHODID_PING = 0;
  private static final int METHODID_BUY = 1;
  private static final int METHODID_SELL = 2;
  private static final int METHODID_MAKE = 3;
  private static final int METHODID_NEXT = 4;
  private static final int METHODID_SAVE = 5;
  private static final int METHODID_LOAD = 6;
  private static final int METHODID_BACK = 7;
  private static final int METHODID_QUIT = 8;
  private static final int METHODID_INIT = 9;

  private static final class MethodHandlers<Req, Resp> implements
      io.grpc.stub.ServerCalls.UnaryMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ServerStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ClientStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.BidiStreamingMethod<Req, Resp> {
    private final ClientPageImplBase serviceImpl;
    private final int methodId;

    MethodHandlers(ClientPageImplBase serviceImpl, int methodId) {
      this.serviceImpl = serviceImpl;
      this.methodId = methodId;
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public void invoke(Req request, io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        case METHODID_PING:
          serviceImpl.ping((plushie_tycoon.Grpc.NullObject) request,
              (io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.NullObject>) responseObserver);
          break;
        case METHODID_BUY:
          serviceImpl.buy((plushie_tycoon.Grpc.TransactionObject) request,
              (io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot>) responseObserver);
          break;
        case METHODID_SELL:
          serviceImpl.sell((plushie_tycoon.Grpc.TransactionObject) request,
              (io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot>) responseObserver);
          break;
        case METHODID_MAKE:
          serviceImpl.make((plushie_tycoon.Grpc.TransactionObject) request,
              (io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot>) responseObserver);
          break;
        case METHODID_NEXT:
          serviceImpl.next((plushie_tycoon.Grpc.NullObject) request,
              (io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot>) responseObserver);
          break;
        case METHODID_SAVE:
          serviceImpl.save((plushie_tycoon.Grpc.NullObject) request,
              (io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot>) responseObserver);
          break;
        case METHODID_LOAD:
          serviceImpl.load((plushie_tycoon.Grpc.NullObject) request,
              (io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot>) responseObserver);
          break;
        case METHODID_BACK:
          serviceImpl.back((plushie_tycoon.Grpc.NullObject) request,
              (io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot>) responseObserver);
          break;
        case METHODID_QUIT:
          serviceImpl.quit((plushie_tycoon.Grpc.NullObject) request,
              (io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot>) responseObserver);
          break;
        case METHODID_INIT:
          serviceImpl.init((plushie_tycoon.Grpc.NullObject) request,
              (io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot>) responseObserver);
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

  private static abstract class ClientPageBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoFileDescriptorSupplier, io.grpc.protobuf.ProtoServiceDescriptorSupplier {
    ClientPageBaseDescriptorSupplier() {}

    @java.lang.Override
    public com.google.protobuf.Descriptors.FileDescriptor getFileDescriptor() {
      return plushie_tycoon.Grpc.getDescriptor();
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.ServiceDescriptor getServiceDescriptor() {
      return getFileDescriptor().findServiceByName("ClientPage");
    }
  }

  private static final class ClientPageFileDescriptorSupplier
      extends ClientPageBaseDescriptorSupplier {
    ClientPageFileDescriptorSupplier() {}
  }

  private static final class ClientPageMethodDescriptorSupplier
      extends ClientPageBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoMethodDescriptorSupplier {
    private final String methodName;

    ClientPageMethodDescriptorSupplier(String methodName) {
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
      synchronized (ClientPageGrpc.class) {
        result = serviceDescriptor;
        if (result == null) {
          serviceDescriptor = result = io.grpc.ServiceDescriptor.newBuilder(SERVICE_NAME)
              .setSchemaDescriptor(new ClientPageFileDescriptorSupplier())
              .addMethod(getPingMethod())
              .addMethod(getBuyMethod())
              .addMethod(getSellMethod())
              .addMethod(getMakeMethod())
              .addMethod(getNextMethod())
              .addMethod(getSaveMethod())
              .addMethod(getLoadMethod())
              .addMethod(getBackMethod())
              .addMethod(getQuitMethod())
              .addMethod(getInitMethod())
              .build();
        }
      }
    }
    return result;
  }
}
