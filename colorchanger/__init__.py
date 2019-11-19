from flask import Flask, render_template, request, redirect
from flask_mqtt import Mqtt

app = Flask(__name__)
app.config["MQTT_BROKER_URL"] = "broker"
app.config["MQTT_BROKER_PORT"] = 1883
app.config["MQTT_TLS_ENABLED"] = False

mqtt = Mqtt(app)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/leds", methods=["POST"])
def change_leds():
    red =  int(request.form["red"])
    green = int(request.form["green"])
    blue = int(request.form["blue"])
    brightness =  int(request.form["brightness"])


    mqtt.publish("led/color", f"{red}, {green}, {blue}, {brightness}")
    return redirect("/")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888, debug=True)
