from __future__ import print_function

import logging
import grpc
import qik_test
import qik_test_pb2
import qik_test_pb2_grpc

# Step 1: Create a Channel
channel = grpc.insecure_channel('localhost:50051')

# Step 2: Create a Stub
stub = qik_test_pb2_grpc.QuantamStub(channel)

# Step 3: call API
number = qik_test_pb2.Number(value=1)
#stub.circut(number) where circut is the rpc <<circut>> from
response = stub.circut(number)
print(response.name)



# def run():
#     # NOTE(gRPC Python Team): .close() is possible on a channel and should be
#     # used in circumstances in which the with statement does not fit the needs
#     # of the code.
#     with grpc.insecure_channel('localhost:50051') as channel:
#         stub = qik_test_pb2_grpc.QiskitStub(channel)
#         response = stub.SayHello(qik_test_pb2.HelloRequest(name='you'))
#     print("Greeter client received: " + response.message)


# if __name__ == '__main__':
#     logging.basicConfig()
#     run()
