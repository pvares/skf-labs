FROM alpine:3.7
LABEL MAINTAINER Semen Rozkhov <life.start.rs@gmail.com>
RUN apk update --no-cache && apk add python3 \
python3-dev \
py3-pip \ 
git \
bash \ 
zip

ENV secret_key secret
RUN git clone https://github.com/pvares/skf-labs.git
WORKDIR /skf-labs/CMD2
RUN pip3 install -r requirements.txt
CMD [ "python3", "./CMD2.py" ]
