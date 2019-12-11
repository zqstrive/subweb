FROM alpine:latest
MAINTAINER NicoNewBeee "lzd596049368@gmail.com"
RUN apk add --no-cache python3-dev git \
    && pip3 install --upgrade pip \
    && git clone https://github.com/lzdnico/subweb.git
COPY ./aff.py /subweb/api/aff.py
COPY ./my.sh /subweb/my.sh
COPY ./pref.ini /subweb/config/pref.ini
WORKDIR /subweb
RUN pip3 install --no-cache-dir -r requirements.txt &&\
    cd /subweb/config &&\
    chmod 777 /subweb/config/subconverter
EXPOSE 10086 10010
ENTRYPOINT [ "/bin/sh", "/subweb/my.sh"]