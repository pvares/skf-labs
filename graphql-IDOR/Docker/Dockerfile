FROM alpine:3.7
LABEL MAINTAINER Davide Cioccia <d.cioccia@dcodx.com>
RUN apk update --no-cache && apk add python3 \
    python3-dev \
    py3-pip \
    bash \
    git

ENV secret_key secret
RUN git clone https://github.com/pvares/skf-labs.git
WORKDIR /skf-labs/graphql-IDOR

RUN pip3 install -r requirements.txt
RUN python3 populate-database.py
CMD [ "python3", "app.py"]
