FROM alpine:3.7
LABEL MAINTAINER Giulio Comi
RUN apk update --no-cache && apk add python3 \
python2-dev \
py2-pip \ 
git \
bash

RUN git clone https://github.com/pvares/skf-labs.git
WORKDIR /skf-labs/RFI
RUN pip2 install -r requirements.txt
CMD [ "python2", "./RFI.py" ]
