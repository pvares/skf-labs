FROM alpine:3.7
LABEL MAINTAINER Giulio Comi
RUN apk update --no-cache && apk add python3 \
python3-dev \
py3-pip \ 
git \
bash 

ENV secret_key secret
RUN git clone https://github.com/pvares/skf-labs.git
WORKDIR /skf-labs/DoS-regex
RUN pip3 install -r requirements.txt
ENTRYPOINT [ "python3", "./dos.py" ]
