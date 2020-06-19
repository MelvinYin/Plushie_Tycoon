import grpc
import grpc_pb2
import grpc_pb2_grpc


class GrpcUIAdapter:
    def __init__(self, grpc_stub, verbose=False):
        self.stub = grpc_stub
        self.verbose = verbose

    def _print(self, message):
        if self.verbose:
            print(message)

    def Buy(self, name="aisha", quantity=11):
        self._print(f"GrpcUIAdapter.Buy({name}, {quantity}) called.")
        request_object = grpc_pb2.TransactionObject(name=name, quantity=quantity)
        return_object = self.stub.buy(request_object)
        self._print("Success.")
        return return_object

    def Sell(self, name="aisha", quantity=11):
        self._print(f"GrpcUIAdapter.Sell({name}, {quantity}) called.")
        request_object = grpc_pb2.TransactionObject(name=name, quantity=quantity)
        return_object = self.stub.sell(request_object)
        self._print("Success.")
        return return_object

    def Make(self, name="aisha", quantity=11):
        self._print(f"GrpcUIAdapter.Make({name}, {quantity}) called.")
        request_object = grpc_pb2.TransactionObject(name=name, quantity=quantity)
        return_object = self.stub.make(request_object)
        self._print("Success.")
        return return_object

    def Next(self):
        self._print(f"GrpcUIAdapter.Next() called.")
        request_object = grpc_pb2.NullObject()
        return_object = self.stub.next(request_object)
        self._print("Success.")
        return return_object

    def Save(self):
        self._print(f"GrpcUIAdapter.Save() called.")
        request_object = grpc_pb2.NullObject()
        return_object = self.stub.save(request_object)
        self._print("Success.")
        return return_object

    def Load(self):
        self._print(f"GrpcUIAdapter.Load() called.")
        request_object = grpc_pb2.NullObject()
        return_object = self.stub.load(request_object)
        self._print("Success.")
        return return_object

    def Back(self):
        self._print(f"GrpcUIAdapter.Back() called.")
        request_object = grpc_pb2.NullObject()
        return_object = self.stub.back(request_object)
        self._print("Success.")
        return return_object

    def Quit(self):
        self._print(f"GrpcUIAdapter.Quit() called.")
        request_object = grpc_pb2.NullObject()
        return_object = self.stub.quit(request_object)
        self._print("Success.")
        return return_object

    def Init(self):
        self._print(f"GrpcUIAdapter.Init() called.")
        request_object = grpc_pb2.NullObject()
        return_object = self.stub.init(request_object)
        self._print("Success.")
        return return_object
