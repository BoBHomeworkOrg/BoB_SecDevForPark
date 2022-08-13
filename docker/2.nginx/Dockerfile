FROM ubuntu:20.04

RUN apt update && \
    apt install nginx -y && \
    echo "Hello BOB" > /var/www/html/index.html && \
    echo "\ndaemon off;" >> /etc/nginx/nginx.conf && \
    apt clean && rm -rf /var/lib/apt/lists* /tmp/* /var/tmp/*

CMD ["nginx"]