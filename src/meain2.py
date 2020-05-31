import grpc
import grpc_pb2
import grpc_pb2_grpc


class RouteGuideServicer(grpc_pb2_grpc.RouteGuideServicer):
    """Provides methods that implement functionality of route guide server."""

    def __init__(self):
        pass

    def GetFeature(self, request, context):
        print(request)
        feature = grpc_pb2.Feature(b='asdfg')
        return feature


from concurrent.futures import ThreadPoolExecutor

def main():
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    grpc_pb2_grpc.add_RouteGuideServicer_to_server(RouteGuideServicer(),
        server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

main()