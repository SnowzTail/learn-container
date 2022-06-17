FROM ubuntu:bionic

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y r-base && \

    R -e "install.packages('dplyr', repos='http://cran.r-project.org')"

ADD test.r ./

CMD ["Rscript", "test.r"]
