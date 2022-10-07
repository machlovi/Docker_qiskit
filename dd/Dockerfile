

FROM python:3.7
ADD py.py .
RUN apt-get update && apt-get install -y git
RUN pip install git+https://github.com/qiskit-community/qiskit-textbook.git#subdirectory=qiskit-textbook-src

CMD ["python" , "./py.py" ]


# FROM python:3.8

# ADD qiskit.py .


# CMD ["python" , "./qiskit.py" ]
