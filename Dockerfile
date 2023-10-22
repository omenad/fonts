FROM ubuntu:22.04

RUN set -ex \
    && deps=" \
        fontforge \
    " \
    && apt update && apt install -y $deps --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /usr/local/src

WORKDIR /usr/local/src
ENTRYPOINT ["/bin/bash", "-c"]
