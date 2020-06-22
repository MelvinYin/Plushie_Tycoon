import grpc
import grpc_pb2
import grpc_pb2_grpc

def ping(portno):
    print(f"AdminPage.ping called.")
    with grpc.insecure_channel(f'localhost:{portno}') as channel:
        stub = grpc_pb2_grpc.AdminPageStub(channel)
        request_object = grpc_pb2.NullObject()
        return_object = stub.ping(request_object)
    print(f"AdminPage.ping completed.\n")

def nextTurn(portno):
    print(f"AdminPage.nextTurn called.")
    with grpc.insecure_channel(f'localhost:{portno}') as channel:
        stub = grpc_pb2_grpc.AdminPageStub(channel)
        request_object = grpc_pb2.NullObject()
        return_object = stub.nextTurn(request_object)
    print(f"AdminPage.nextTurn completed.\n")
    return return_object

def getCall(portno):
    print(f"AdminPage.getCall called.")
    with grpc.insecure_channel(f'localhost:{portno}') as channel:
        stub = grpc_pb2_grpc.AdminPageStub(channel)
        request_object = grpc_pb2.NullObject()
        for call in stub.getCall(request_object):
            yield call

    print(f"AdminPage.getCall completed.\n")