FROM ubuntu

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /usr/local/src

RUN apt update && apt install -y r-base && \

    R -e "install.packages('dplyr', repos='http://cran.r-project.org')"

ADD test.r ./

ENTRYPOINT ["Rscript", "test.r"]
