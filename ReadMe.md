 To run  the client you need to install these as root user

sudo apt-get install python3-pip
python3 -m pip install --upgrade pip
<!-- python3 -m pip install grpcio -->
python3 -m pip install grpcio
python3 -m pip install grpcio-tools

python3 -m pip install six==1.16.0

Make sure the version match as per you have on local machien when creating your grpc files from command.
grpcio==1.49.1
grpcio-tools==1.49.1
protobuf==4.21.7
six==1.16.0

pip3 install qiskit

We need to install these dependencies to run these
to check out client and server setup.Otherwise creating the image usong docker 
file.

We may have clash between the different versions which nede 
to be same as requirements.
In other words