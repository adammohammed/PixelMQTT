FROM alpine:latest

RUN apk update && apk add mosquitto-clients

ENTRYPOINT ["mosquitto_sub"]
CMD ["-h", "broker", "-p", "1883", "-t", "led/color"]