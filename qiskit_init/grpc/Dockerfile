
FROM gcr.io/google_appengine/python:latest
FROM python:3.8
# RUN pip install --upgrade pip
# ADD qik_test.py .
WORKDIR /app
ADD . /app

RUN pip install -r requirements.txt

RUN git clone https://github.com/Qiskit/qiskit-terra.git
RUN cd qiskit-terra
RUN pip install qiskit

RUN pip install -r requirements.txt



# RUN pip install git+https://github.com/qiskit-community/qiskit-textbook.git#subdirectory=qiskit-textbook-src
# RUN pip install qiskit
ENTRYPOINT ["python" , "./server.py"]