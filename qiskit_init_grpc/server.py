# from urllib import response
# from ast import Num
import grpc
from concurrent import futures
import time
from function import qik_test
from grpc_generated_files import (qik_test_pb2_grpc,qik_test_pb2)


print("All Modules loaded ")


_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class QuantamServicer(qik_test_pb2_grpc.QuantamServicer):
    #  the function name must be the same as service define in the one in  .proto file as
    # service Qiskit { rpc <<<circut>>>(Number) returns (Number){} }

    def circut(self, request,context):
        response = qik_test_pb2.Response()
        response.name=qik_test.circut_value(request.value) 
        # where circut_name is the name of
        return response


def run():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    qik_test_pb2_grpc.add_QuantamServicer_to_server(QuantamServicer(), server)
    print('Starting server. Listening on port 80.')
    server.add_insecure_port('[::]:80')
    server.start()

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)



if __name__ == '__main__':
    run()