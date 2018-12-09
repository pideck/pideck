FROM debian:stretch
RUN apt-get update && apt-get install -y dpkg-dev dh-make
