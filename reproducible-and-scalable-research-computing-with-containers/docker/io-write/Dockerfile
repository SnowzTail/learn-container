FROM ubuntu

WORKDIR /usr/local/src

RUN apt update && apt install -y python3 python3-pip && pip3 install pandas

ADD py_test.py ./

ENTRYPOINT ["python3", "py_test.py"]
