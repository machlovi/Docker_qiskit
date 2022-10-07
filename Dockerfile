
FROM python:3.7
RUN pip install --upgrade pip
ADD qik_test.py .
RUN git clone https://github.com/Qiskit/qiskit-terra.git
RUN cd qiskit-terra
RUN pip install cython
# RUN pip install -r requirements-dev.txt
RUN pip install .


# RUN pip install git+https://github.com/qiskit-community/qiskit-textbook.git#subdirectory=qiskit-textbook-src
# RUN pip install qiskit
CMD ["python" , "./qik_test.py" ]