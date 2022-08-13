FROM alpine

# RUN apt update
RUN apk update
# RUN apt install nginx
RUN apk add nginx

CMD [ "nginx". "-g", "daemin off;" ]