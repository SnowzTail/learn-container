FROM ubuntu

RUN apt update && apt install -y python3

ADD py_test.py ./

#CMD ["python", "py_test.py"]
CMD ["python3", "py_test.py"]
