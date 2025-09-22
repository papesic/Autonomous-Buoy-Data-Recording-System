from flask import Flask, render_template, request, jsonify
from flask_mqtt import Mqtt

app = Flask(__name__)

# MQTT configuration (adjust broker details for your setup)
app.config['MQTT_BROKER_URL'] = 'localhost'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_KEEPALIVE'] = 60
app.config['MQTT_TOPIC'] = 'buoy/data'

mqtt = Mqtt(app)

# Store incoming data in memory for now
latest_data = []

@app.route('/')
def index():
    return render_template('index.html', data=latest_data)

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    payload = message.payload.decode()
    latest_data.append(payload)
    if len(latest_data) > 100:  # keep last 100 messages
        latest_data.pop(0)

    print(f"Received MQTT: {payload}")

@app.route('/data')
def get_data():
    return jsonify(latest_data)

if __name__ == '__main__':
    mqtt.subscribe(app.config['MQTT_TOPIC'])
    app.run(host='0.0.0.0', port=5000, debug=True)
