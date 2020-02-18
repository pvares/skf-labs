FROM alpine:3.7
LABEL MAINTAINER Abhishek "abhiabhi2306@gmail.com"
RUN apk update --no-cache && apk add git \
python2-dev \
py2-pip \ 
git \
bash

ENV secret_key secret
RUN git clone https://github.com/pvares/skf-labs.git
WORKDIR /skf-labs/ratelimiting
RUN pip install -r requirements.txt
CMD [ "python2", "./ratelimiting.py" ]