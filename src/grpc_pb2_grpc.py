# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import grpc_pb2 as grpc__pb2


class UITransferStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Buy = channel.unary_unary(
                '/UITransfer/Buy',
                request_serializer=grpc__pb2.TransactionObject.SerializeToString,
                response_deserializer=grpc__pb2.UserOutput.FromString,
                )
        self.Sell = channel.unary_unary(
                '/UITransfer/Sell',
                request_serializer=grpc__pb2.TransactionObject.SerializeToString,
                response_deserializer=grpc__pb2.UserOutput.FromString,
                )
        self.Make = channel.unary_unary(
                '/UITransfer/Make',
                request_serializer=grpc__pb2.TransactionObject.SerializeToString,
                response_deserializer=grpc__pb2.UserOutput.FromString,
                )
        self.Next = channel.unary_unary(
                '/UITransfer/Next',
                request_serializer=grpc__pb2.SelectionObject.SerializeToString,
                response_deserializer=grpc__pb2.UserOutput.FromString,
                )
        self.Save = channel.unary_unary(
                '/UITransfer/Save',
                request_serializer=grpc__pb2.SelectionObject.SerializeToString,
                response_deserializer=grpc__pb2.UserOutput.FromString,
                )
        self.Load = channel.unary_unary(
                '/UITransfer/Load',
                request_serializer=grpc__pb2.SelectionObject.SerializeToString,
                response_deserializer=grpc__pb2.UserOutput.FromString,
                )
        self.Back = channel.unary_unary(
                '/UITransfer/Back',
                request_serializer=grpc__pb2.SelectionObject.SerializeToString,
                response_deserializer=grpc__pb2.UserOutput.FromString,
                )
        self.Quit = channel.unary_unary(
                '/UITransfer/Quit',
                request_serializer=grpc__pb2.SelectionObject.SerializeToString,
                response_deserializer=grpc__pb2.UserOutput.FromString,
                )
        self.Init = channel.unary_unary(
                '/UITransfer/Init',
                request_serializer=grpc__pb2.SelectionObject.SerializeToString,
                response_deserializer=grpc__pb2.UserOutput.FromString,
                )


class UITransferServicer(object):
    """Missing associated documentation comment in .proto file"""

    def Buy(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Sell(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Make(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Next(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Save(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Load(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Back(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Quit(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Init(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UITransferServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Buy': grpc.unary_unary_rpc_method_handler(
                    servicer.Buy,
                    request_deserializer=grpc__pb2.TransactionObject.FromString,
                    response_serializer=grpc__pb2.UserOutput.SerializeToString,
            ),
            'Sell': grpc.unary_unary_rpc_method_handler(
                    servicer.Sell,
                    request_deserializer=grpc__pb2.TransactionObject.FromString,
                    response_serializer=grpc__pb2.UserOutput.SerializeToString,
            ),
            'Make': grpc.unary_unary_rpc_method_handler(
                    servicer.Make,
                    request_deserializer=grpc__pb2.TransactionObject.FromString,
                    response_serializer=grpc__pb2.UserOutput.SerializeToString,
            ),
            'Next': grpc.unary_unary_rpc_method_handler(
                    servicer.Next,
                    request_deserializer=grpc__pb2.SelectionObject.FromString,
                    response_serializer=grpc__pb2.UserOutput.SerializeToString,
            ),
            'Save': grpc.unary_unary_rpc_method_handler(
                    servicer.Save,
                    request_deserializer=grpc__pb2.SelectionObject.FromString,
                    response_serializer=grpc__pb2.UserOutput.SerializeToString,
            ),
            'Load': grpc.unary_unary_rpc_method_handler(
                    servicer.Load,
                    request_deserializer=grpc__pb2.SelectionObject.FromString,
                    response_serializer=grpc__pb2.UserOutput.SerializeToString,
            ),
            'Back': grpc.unary_unary_rpc_method_handler(
                    servicer.Back,
                    request_deserializer=grpc__pb2.SelectionObject.FromString,
                    response_serializer=grpc__pb2.UserOutput.SerializeToString,
            ),
            'Quit': grpc.unary_unary_rpc_method_handler(
                    servicer.Quit,
                    request_deserializer=grpc__pb2.SelectionObject.FromString,
                    response_serializer=grpc__pb2.UserOutput.SerializeToString,
            ),
            'Init': grpc.unary_unary_rpc_method_handler(
                    servicer.Init,
                    request_deserializer=grpc__pb2.SelectionObject.FromString,
                    response_serializer=grpc__pb2.UserOutput.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'UITransfer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UITransfer(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def Buy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UITransfer/Buy',
            grpc__pb2.TransactionObject.SerializeToString,
            grpc__pb2.UserOutput.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Sell(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UITransfer/Sell',
            grpc__pb2.TransactionObject.SerializeToString,
            grpc__pb2.UserOutput.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Make(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UITransfer/Make',
            grpc__pb2.TransactionObject.SerializeToString,
            grpc__pb2.UserOutput.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Next(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UITransfer/Next',
            grpc__pb2.SelectionObject.SerializeToString,
            grpc__pb2.UserOutput.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Save(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UITransfer/Save',
            grpc__pb2.SelectionObject.SerializeToString,
            grpc__pb2.UserOutput.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Load(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UITransfer/Load',
            grpc__pb2.SelectionObject.SerializeToString,
            grpc__pb2.UserOutput.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Back(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UITransfer/Back',
            grpc__pb2.SelectionObject.SerializeToString,
            grpc__pb2.UserOutput.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Quit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UITransfer/Quit',
            grpc__pb2.SelectionObject.SerializeToString,
            grpc__pb2.UserOutput.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Init(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UITransfer/Init',
            grpc__pb2.SelectionObject.SerializeToString,
            grpc__pb2.UserOutput.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
