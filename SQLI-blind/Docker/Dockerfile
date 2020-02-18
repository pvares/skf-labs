FROM alpine:3.7
LABEL MAINTAINER Glenn ten Cate <glenn.ten.cate@owasp.org>
RUN apk update --no-cache && apk add python3 \
python3-dev \
py3-pip \ 
git \
bash

ENV secret_key secret
RUN git clone https://github.com/pvares/skf-labs.git
WORKDIR /skf-labs/SQLI-blind
RUN pip3 install -r requirements.txt
CMD [ "python3", "./SQLI-blind.py" ]
