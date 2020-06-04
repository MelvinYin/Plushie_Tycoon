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
public final class UITransferGrpc {

  private UITransferGrpc() {}

  public static final String SERVICE_NAME = "plushie_tycoon.UITransfer";

  // Static method descriptors that strictly reflect the proto.
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
    if ((getBuyMethod = UITransferGrpc.getBuyMethod) == null) {
      synchronized (UITransferGrpc.class) {
        if ((getBuyMethod = UITransferGrpc.getBuyMethod) == null) {
          UITransferGrpc.getBuyMethod = getBuyMethod =
              io.grpc.MethodDescriptor.<plushie_tycoon.Grpc.TransactionObject, plushie_tycoon.Grpc.Snapshot>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "buy"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.TransactionObject.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.Snapshot.getDefaultInstance()))
              .setSchemaDescriptor(new UITransferMethodDescriptorSupplier("buy"))
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
    if ((getSellMethod = UITransferGrpc.getSellMethod) == null) {
      synchronized (UITransferGrpc.class) {
        if ((getSellMethod = UITransferGrpc.getSellMethod) == null) {
          UITransferGrpc.getSellMethod = getSellMethod =
              io.grpc.MethodDescriptor.<plushie_tycoon.Grpc.TransactionObject, plushie_tycoon.Grpc.Snapshot>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "sell"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.TransactionObject.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.Snapshot.getDefaultInstance()))
              .setSchemaDescriptor(new UITransferMethodDescriptorSupplier("sell"))
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
    if ((getMakeMethod = UITransferGrpc.getMakeMethod) == null) {
      synchronized (UITransferGrpc.class) {
        if ((getMakeMethod = UITransferGrpc.getMakeMethod) == null) {
          UITransferGrpc.getMakeMethod = getMakeMethod =
              io.grpc.MethodDescriptor.<plushie_tycoon.Grpc.TransactionObject, plushie_tycoon.Grpc.Snapshot>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "make"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.TransactionObject.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.Snapshot.getDefaultInstance()))
              .setSchemaDescriptor(new UITransferMethodDescriptorSupplier("make"))
              .build();
        }
      }
    }
    return getMakeMethod;
  }

  private static volatile io.grpc.MethodDescriptor<plushie_tycoon.Grpc.SelectionObject,
      plushie_tycoon.Grpc.Snapshot> getNextMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "next",
      requestType = plushie_tycoon.Grpc.SelectionObject.class,
      responseType = plushie_tycoon.Grpc.Snapshot.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<plushie_tycoon.Grpc.SelectionObject,
      plushie_tycoon.Grpc.Snapshot> getNextMethod() {
    io.grpc.MethodDescriptor<plushie_tycoon.Grpc.SelectionObject, plushie_tycoon.Grpc.Snapshot> getNextMethod;
    if ((getNextMethod = UITransferGrpc.getNextMethod) == null) {
      synchronized (UITransferGrpc.class) {
        if ((getNextMethod = UITransferGrpc.getNextMethod) == null) {
          UITransferGrpc.getNextMethod = getNextMethod =
              io.grpc.MethodDescriptor.<plushie_tycoon.Grpc.SelectionObject, plushie_tycoon.Grpc.Snapshot>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "next"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.SelectionObject.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.Snapshot.getDefaultInstance()))
              .setSchemaDescriptor(new UITransferMethodDescriptorSupplier("next"))
              .build();
        }
      }
    }
    return getNextMethod;
  }

  private static volatile io.grpc.MethodDescriptor<plushie_tycoon.Grpc.SelectionObject,
      plushie_tycoon.Grpc.Snapshot> getSaveMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "save",
      requestType = plushie_tycoon.Grpc.SelectionObject.class,
      responseType = plushie_tycoon.Grpc.Snapshot.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<plushie_tycoon.Grpc.SelectionObject,
      plushie_tycoon.Grpc.Snapshot> getSaveMethod() {
    io.grpc.MethodDescriptor<plushie_tycoon.Grpc.SelectionObject, plushie_tycoon.Grpc.Snapshot> getSaveMethod;
    if ((getSaveMethod = UITransferGrpc.getSaveMethod) == null) {
      synchronized (UITransferGrpc.class) {
        if ((getSaveMethod = UITransferGrpc.getSaveMethod) == null) {
          UITransferGrpc.getSaveMethod = getSaveMethod =
              io.grpc.MethodDescriptor.<plushie_tycoon.Grpc.SelectionObject, plushie_tycoon.Grpc.Snapshot>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "save"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.SelectionObject.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.Snapshot.getDefaultInstance()))
              .setSchemaDescriptor(new UITransferMethodDescriptorSupplier("save"))
              .build();
        }
      }
    }
    return getSaveMethod;
  }

  private static volatile io.grpc.MethodDescriptor<plushie_tycoon.Grpc.SelectionObject,
      plushie_tycoon.Grpc.Snapshot> getLoadMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "load",
      requestType = plushie_tycoon.Grpc.SelectionObject.class,
      responseType = plushie_tycoon.Grpc.Snapshot.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<plushie_tycoon.Grpc.SelectionObject,
      plushie_tycoon.Grpc.Snapshot> getLoadMethod() {
    io.grpc.MethodDescriptor<plushie_tycoon.Grpc.SelectionObject, plushie_tycoon.Grpc.Snapshot> getLoadMethod;
    if ((getLoadMethod = UITransferGrpc.getLoadMethod) == null) {
      synchronized (UITransferGrpc.class) {
        if ((getLoadMethod = UITransferGrpc.getLoadMethod) == null) {
          UITransferGrpc.getLoadMethod = getLoadMethod =
              io.grpc.MethodDescriptor.<plushie_tycoon.Grpc.SelectionObject, plushie_tycoon.Grpc.Snapshot>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "load"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.SelectionObject.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.Snapshot.getDefaultInstance()))
              .setSchemaDescriptor(new UITransferMethodDescriptorSupplier("load"))
              .build();
        }
      }
    }
    return getLoadMethod;
  }

  private static volatile io.grpc.MethodDescriptor<plushie_tycoon.Grpc.SelectionObject,
      plushie_tycoon.Grpc.Snapshot> getBackMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "back",
      requestType = plushie_tycoon.Grpc.SelectionObject.class,
      responseType = plushie_tycoon.Grpc.Snapshot.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<plushie_tycoon.Grpc.SelectionObject,
      plushie_tycoon.Grpc.Snapshot> getBackMethod() {
    io.grpc.MethodDescriptor<plushie_tycoon.Grpc.SelectionObject, plushie_tycoon.Grpc.Snapshot> getBackMethod;
    if ((getBackMethod = UITransferGrpc.getBackMethod) == null) {
      synchronized (UITransferGrpc.class) {
        if ((getBackMethod = UITransferGrpc.getBackMethod) == null) {
          UITransferGrpc.getBackMethod = getBackMethod =
              io.grpc.MethodDescriptor.<plushie_tycoon.Grpc.SelectionObject, plushie_tycoon.Grpc.Snapshot>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "back"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.SelectionObject.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.Snapshot.getDefaultInstance()))
              .setSchemaDescriptor(new UITransferMethodDescriptorSupplier("back"))
              .build();
        }
      }
    }
    return getBackMethod;
  }

  private static volatile io.grpc.MethodDescriptor<plushie_tycoon.Grpc.SelectionObject,
      plushie_tycoon.Grpc.Snapshot> getQuitMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "quit",
      requestType = plushie_tycoon.Grpc.SelectionObject.class,
      responseType = plushie_tycoon.Grpc.Snapshot.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<plushie_tycoon.Grpc.SelectionObject,
      plushie_tycoon.Grpc.Snapshot> getQuitMethod() {
    io.grpc.MethodDescriptor<plushie_tycoon.Grpc.SelectionObject, plushie_tycoon.Grpc.Snapshot> getQuitMethod;
    if ((getQuitMethod = UITransferGrpc.getQuitMethod) == null) {
      synchronized (UITransferGrpc.class) {
        if ((getQuitMethod = UITransferGrpc.getQuitMethod) == null) {
          UITransferGrpc.getQuitMethod = getQuitMethod =
              io.grpc.MethodDescriptor.<plushie_tycoon.Grpc.SelectionObject, plushie_tycoon.Grpc.Snapshot>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "quit"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.SelectionObject.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.Snapshot.getDefaultInstance()))
              .setSchemaDescriptor(new UITransferMethodDescriptorSupplier("quit"))
              .build();
        }
      }
    }
    return getQuitMethod;
  }

  private static volatile io.grpc.MethodDescriptor<plushie_tycoon.Grpc.SelectionObject,
      plushie_tycoon.Grpc.Snapshot> getInitMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "init",
      requestType = plushie_tycoon.Grpc.SelectionObject.class,
      responseType = plushie_tycoon.Grpc.Snapshot.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<plushie_tycoon.Grpc.SelectionObject,
      plushie_tycoon.Grpc.Snapshot> getInitMethod() {
    io.grpc.MethodDescriptor<plushie_tycoon.Grpc.SelectionObject, plushie_tycoon.Grpc.Snapshot> getInitMethod;
    if ((getInitMethod = UITransferGrpc.getInitMethod) == null) {
      synchronized (UITransferGrpc.class) {
        if ((getInitMethod = UITransferGrpc.getInitMethod) == null) {
          UITransferGrpc.getInitMethod = getInitMethod =
              io.grpc.MethodDescriptor.<plushie_tycoon.Grpc.SelectionObject, plushie_tycoon.Grpc.Snapshot>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "init"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.SelectionObject.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  plushie_tycoon.Grpc.Snapshot.getDefaultInstance()))
              .setSchemaDescriptor(new UITransferMethodDescriptorSupplier("init"))
              .build();
        }
      }
    }
    return getInitMethod;
  }

  /**
   * Creates a new async stub that supports all call types for the service
   */
  public static UITransferStub newStub(io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<UITransferStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<UITransferStub>() {
        @java.lang.Override
        public UITransferStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new UITransferStub(channel, callOptions);
        }
      };
    return UITransferStub.newStub(factory, channel);
  }

  /**
   * Creates a new blocking-style stub that supports unary and streaming output calls on the service
   */
  public static UITransferBlockingStub newBlockingStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<UITransferBlockingStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<UITransferBlockingStub>() {
        @java.lang.Override
        public UITransferBlockingStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new UITransferBlockingStub(channel, callOptions);
        }
      };
    return UITransferBlockingStub.newStub(factory, channel);
  }

  /**
   * Creates a new ListenableFuture-style stub that supports unary calls on the service
   */
  public static UITransferFutureStub newFutureStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<UITransferFutureStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<UITransferFutureStub>() {
        @java.lang.Override
        public UITransferFutureStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new UITransferFutureStub(channel, callOptions);
        }
      };
    return UITransferFutureStub.newStub(factory, channel);
  }

  /**
   * <pre>
   *todo: map in proto is not ordered. Perhaps switch to 2 repeated fields?
   *or alternatively we can provide an order object somewhere
   * </pre>
   */
  public static abstract class UITransferImplBase implements io.grpc.BindableService {

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
    public void next(plushie_tycoon.Grpc.SelectionObject request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot> responseObserver) {
      asyncUnimplementedUnaryCall(getNextMethod(), responseObserver);
    }

    /**
     */
    public void save(plushie_tycoon.Grpc.SelectionObject request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot> responseObserver) {
      asyncUnimplementedUnaryCall(getSaveMethod(), responseObserver);
    }

    /**
     */
    public void load(plushie_tycoon.Grpc.SelectionObject request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot> responseObserver) {
      asyncUnimplementedUnaryCall(getLoadMethod(), responseObserver);
    }

    /**
     */
    public void back(plushie_tycoon.Grpc.SelectionObject request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot> responseObserver) {
      asyncUnimplementedUnaryCall(getBackMethod(), responseObserver);
    }

    /**
     */
    public void quit(plushie_tycoon.Grpc.SelectionObject request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot> responseObserver) {
      asyncUnimplementedUnaryCall(getQuitMethod(), responseObserver);
    }

    /**
     */
    public void init(plushie_tycoon.Grpc.SelectionObject request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot> responseObserver) {
      asyncUnimplementedUnaryCall(getInitMethod(), responseObserver);
    }

    @java.lang.Override public final io.grpc.ServerServiceDefinition bindService() {
      return io.grpc.ServerServiceDefinition.builder(getServiceDescriptor())
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
                plushie_tycoon.Grpc.SelectionObject,
                plushie_tycoon.Grpc.Snapshot>(
                  this, METHODID_NEXT)))
          .addMethod(
            getSaveMethod(),
            asyncUnaryCall(
              new MethodHandlers<
                plushie_tycoon.Grpc.SelectionObject,
                plushie_tycoon.Grpc.Snapshot>(
                  this, METHODID_SAVE)))
          .addMethod(
            getLoadMethod(),
            asyncUnaryCall(
              new MethodHandlers<
                plushie_tycoon.Grpc.SelectionObject,
                plushie_tycoon.Grpc.Snapshot>(
                  this, METHODID_LOAD)))
          .addMethod(
            getBackMethod(),
            asyncUnaryCall(
              new MethodHandlers<
                plushie_tycoon.Grpc.SelectionObject,
                plushie_tycoon.Grpc.Snapshot>(
                  this, METHODID_BACK)))
          .addMethod(
            getQuitMethod(),
            asyncUnaryCall(
              new MethodHandlers<
                plushie_tycoon.Grpc.SelectionObject,
                plushie_tycoon.Grpc.Snapshot>(
                  this, METHODID_QUIT)))
          .addMethod(
            getInitMethod(),
            asyncUnaryCall(
              new MethodHandlers<
                plushie_tycoon.Grpc.SelectionObject,
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
  public static final class UITransferStub extends io.grpc.stub.AbstractAsyncStub<UITransferStub> {
    private UITransferStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected UITransferStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new UITransferStub(channel, callOptions);
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
    public void next(plushie_tycoon.Grpc.SelectionObject request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(getNextMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void save(plushie_tycoon.Grpc.SelectionObject request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(getSaveMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void load(plushie_tycoon.Grpc.SelectionObject request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(getLoadMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void back(plushie_tycoon.Grpc.SelectionObject request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(getBackMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void quit(plushie_tycoon.Grpc.SelectionObject request,
        io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(getQuitMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void init(plushie_tycoon.Grpc.SelectionObject request,
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
  public static final class UITransferBlockingStub extends io.grpc.stub.AbstractBlockingStub<UITransferBlockingStub> {
    private UITransferBlockingStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected UITransferBlockingStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new UITransferBlockingStub(channel, callOptions);
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
    public plushie_tycoon.Grpc.Snapshot next(plushie_tycoon.Grpc.SelectionObject request) {
      return blockingUnaryCall(
          getChannel(), getNextMethod(), getCallOptions(), request);
    }

    /**
     */
    public plushie_tycoon.Grpc.Snapshot save(plushie_tycoon.Grpc.SelectionObject request) {
      return blockingUnaryCall(
          getChannel(), getSaveMethod(), getCallOptions(), request);
    }

    /**
     */
    public plushie_tycoon.Grpc.Snapshot load(plushie_tycoon.Grpc.SelectionObject request) {
      return blockingUnaryCall(
          getChannel(), getLoadMethod(), getCallOptions(), request);
    }

    /**
     */
    public plushie_tycoon.Grpc.Snapshot back(plushie_tycoon.Grpc.SelectionObject request) {
      return blockingUnaryCall(
          getChannel(), getBackMethod(), getCallOptions(), request);
    }

    /**
     */
    public plushie_tycoon.Grpc.Snapshot quit(plushie_tycoon.Grpc.SelectionObject request) {
      return blockingUnaryCall(
          getChannel(), getQuitMethod(), getCallOptions(), request);
    }

    /**
     */
    public plushie_tycoon.Grpc.Snapshot init(plushie_tycoon.Grpc.SelectionObject request) {
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
  public static final class UITransferFutureStub extends io.grpc.stub.AbstractFutureStub<UITransferFutureStub> {
    private UITransferFutureStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected UITransferFutureStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new UITransferFutureStub(channel, callOptions);
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
        plushie_tycoon.Grpc.SelectionObject request) {
      return futureUnaryCall(
          getChannel().newCall(getNextMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<plushie_tycoon.Grpc.Snapshot> save(
        plushie_tycoon.Grpc.SelectionObject request) {
      return futureUnaryCall(
          getChannel().newCall(getSaveMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<plushie_tycoon.Grpc.Snapshot> load(
        plushie_tycoon.Grpc.SelectionObject request) {
      return futureUnaryCall(
          getChannel().newCall(getLoadMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<plushie_tycoon.Grpc.Snapshot> back(
        plushie_tycoon.Grpc.SelectionObject request) {
      return futureUnaryCall(
          getChannel().newCall(getBackMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<plushie_tycoon.Grpc.Snapshot> quit(
        plushie_tycoon.Grpc.SelectionObject request) {
      return futureUnaryCall(
          getChannel().newCall(getQuitMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<plushie_tycoon.Grpc.Snapshot> init(
        plushie_tycoon.Grpc.SelectionObject request) {
      return futureUnaryCall(
          getChannel().newCall(getInitMethod(), getCallOptions()), request);
    }
  }

  private static final int METHODID_BUY = 0;
  private static final int METHODID_SELL = 1;
  private static final int METHODID_MAKE = 2;
  private static final int METHODID_NEXT = 3;
  private static final int METHODID_SAVE = 4;
  private static final int METHODID_LOAD = 5;
  private static final int METHODID_BACK = 6;
  private static final int METHODID_QUIT = 7;
  private static final int METHODID_INIT = 8;

  private static final class MethodHandlers<Req, Resp> implements
      io.grpc.stub.ServerCalls.UnaryMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ServerStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ClientStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.BidiStreamingMethod<Req, Resp> {
    private final UITransferImplBase serviceImpl;
    private final int methodId;

    MethodHandlers(UITransferImplBase serviceImpl, int methodId) {
      this.serviceImpl = serviceImpl;
      this.methodId = methodId;
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public void invoke(Req request, io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
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
          serviceImpl.next((plushie_tycoon.Grpc.SelectionObject) request,
              (io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot>) responseObserver);
          break;
        case METHODID_SAVE:
          serviceImpl.save((plushie_tycoon.Grpc.SelectionObject) request,
              (io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot>) responseObserver);
          break;
        case METHODID_LOAD:
          serviceImpl.load((plushie_tycoon.Grpc.SelectionObject) request,
              (io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot>) responseObserver);
          break;
        case METHODID_BACK:
          serviceImpl.back((plushie_tycoon.Grpc.SelectionObject) request,
              (io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot>) responseObserver);
          break;
        case METHODID_QUIT:
          serviceImpl.quit((plushie_tycoon.Grpc.SelectionObject) request,
              (io.grpc.stub.StreamObserver<plushie_tycoon.Grpc.Snapshot>) responseObserver);
          break;
        case METHODID_INIT:
          serviceImpl.init((plushie_tycoon.Grpc.SelectionObject) request,
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

  private static abstract class UITransferBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoFileDescriptorSupplier, io.grpc.protobuf.ProtoServiceDescriptorSupplier {
    UITransferBaseDescriptorSupplier() {}

    @java.lang.Override
    public com.google.protobuf.Descriptors.FileDescriptor getFileDescriptor() {
      return plushie_tycoon.Grpc.getDescriptor();
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.ServiceDescriptor getServiceDescriptor() {
      return getFileDescriptor().findServiceByName("UITransfer");
    }
  }

  private static final class UITransferFileDescriptorSupplier
      extends UITransferBaseDescriptorSupplier {
    UITransferFileDescriptorSupplier() {}
  }

  private static final class UITransferMethodDescriptorSupplier
      extends UITransferBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoMethodDescriptorSupplier {
    private final String methodName;

    UITransferMethodDescriptorSupplier(String methodName) {
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
      synchronized (UITransferGrpc.class) {
        result = serviceDescriptor;
        if (result == null) {
          serviceDescriptor = result = io.grpc.ServiceDescriptor.newBuilder(SERVICE_NAME)
              .setSchemaDescriptor(new UITransferFileDescriptorSupplier())
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
