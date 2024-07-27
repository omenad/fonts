FROM alpine:3.20.2

RUN mkdir -p /opt/fontdev
RUN apk add python3 fontforge=20230101-r5 py3-fontforge=20230101-r5

WORKDIR /opt/fontdev
