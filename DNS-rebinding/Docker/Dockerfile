FROM alpine:3.7
LABEL MAINTAINER Giulio Comi <github.com/giuliocomi>
RUN apk update --no-cache && apk add python3 \
py3-pip \ 
git \
bash

ENV secret_key secret
RUN git clone https://github.com/pvares/skf-labs.git
WORKDIR /skf-labs/DNS-rebinding
RUN pip3 install -r requirements.txt
ENTRYPOINT [ "python3", "./rebind.py" ]
