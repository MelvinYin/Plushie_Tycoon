import grpc
import grpc_pb2
import grpc_pb2_grpc


class GrpcUIAdapter:
    def __init__(self, grpc_stub):
        self.stub = grpc_stub
        pass

    def Buy(self, name="aisha", quantity=11):
        print(f"GrpcUIAdapter.Buy({name}, {quantity}) called.")
        request_object = grpc_pb2.TransactionObject(name=name, quantity=quantity)
        return_object = self.stub.Buy(request_object)
        print("Success.")
        return return_object

    def Sell(self, name="aisha", quantity=11):
        print(f"GrpcUIAdapter.Sell({name}, {quantity}) called.")
        request_object = grpc_pb2.TransactionObject(name=name, quantity=quantity)
        return_object = self.stub.Sell(request_object)
        print("Success.")
        return return_object

    def Make(self, name="aisha", quantity=11):
        print(f"GrpcUIAdapter.Make({name}, {quantity}) called.")
        request_object = grpc_pb2.TransactionObject(name=name, quantity=quantity)
        return_object = self.stub.Make(request_object)
        print("Success.")
        return return_object

    def Next(self):
        print(f"GrpcUIAdapter.Next() called.")
        request_object = grpc_pb2.SelectionObject()
        return_object = self.stub.Next(request_object)
        print("Success.")
        return return_object

    def Save(self):
        print(f"GrpcUIAdapter.Save() called.")
        request_object = grpc_pb2.SelectionObject()
        return_object = self.stub.Save(request_object)
        print("Success.")
        return return_object

    def Load(self):
        print(f"GrpcUIAdapter.Load() called.")
        request_object = grpc_pb2.SelectionObject()
        return_object = self.stub.Load(request_object)
        print("Success.")
        return return_object

    def Back(self):
        print(f"GrpcUIAdapter.Back() called.")
        request_object = grpc_pb2.SelectionObject()
        return_object = self.stub.Back(request_object)
        print("Success.")
        return return_object

    def Quit(self):
        print(f"GrpcUIAdapter.Quit() called.")
        request_object = grpc_pb2.SelectionObject()
        return_object = self.stub.Quit(request_object)
        print("Success.")
        return return_object

    def Init(self):
        print(f"GrpcUIAdapter.Init() called.")
        request_object = grpc_pb2.SelectionObject()
        return_object = self.stub.Init(request_object)
        print("Success.")
        return return_object
