FROM alpine:3.7
LABEL MAINTAINER Giulio Comi
RUN apk update --no-cache && apk add python3 \
python3-dev \
py3-pip \ 
git \
bash

RUN git clone https://github.com/pvares/skf-labs.git
WORKDIR /skf-labs/XSS-DOM-2
RUN pip3 install -r requirements.txt
CMD [ "python3", "./XSS-DOM-2.py" ]
