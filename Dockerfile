FROM alpine:latest
RUN apk add --no-cache python3-dev  \
    && pip3 install --upgrade pip 
COPY . /subweb
WORKDIR /subweb
RUN pip3 install --no-cache-dir -r requirements.txt &&\
    chmod 777 /subweb/config/subconverter
EXPOSE 10086 10010
ENTRYPOINT [ "/bin/sh", "/subweb/docker.sh"]