FROM alpine:3.7
LABEL MAINTAINER Giulio Comi
RUN apk update --no-cache && apk add python2-dev \
python2-dev \
py2-pip \ 
gcc \
linux-headers \
libc-dev \
openldap-dev \
git 

ENV secret_key secret
RUN git clone https://github.com/pvares/skf-labs.git
WORKDIR /skf-labs/Ldap-injection-harder
RUN pip2 install -r requirements.txt
ENTRYPOINT [ "python2", "./ldap-injection-harder.py" ]
