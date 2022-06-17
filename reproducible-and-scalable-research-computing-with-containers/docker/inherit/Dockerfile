FROM io-write

WORKDIR /usr/local/src

RUN pip3 install pandas

ADD py_test.py ./

ENTRYPOINT ["python3", "py_test.py"]
