# Autonomous Buoy Data Recording System
**June 2024 version**
--
An end-to-end IoT platform for **environmental data collection at sea** using an ESP32-based buoy node and a Flask + MQTT server.

The system is designed for research and prototyping of **autonomous sail buoys**.  
It integrates multiple environmental sensors, long-range wireless communication (LoRa), local data logging, and a real-time web dashboard.

---

## Firmware (ESP32)

### Features
- Reads multiple sensors:
  - **SST (DS18B20 waterproof temperature)**
  - **AM2302 (air temperature + humidity)**
  - **MMA8451 accelerometer (motion/orientation)**
  - **MS5607 barometric pressure + temperature**
  - **GY-271 magnetometer (compass)**
  - **GPS (TinyGPS++)**
- Logs data to **SD card**.
- Transmits data packets via **LoRa**.

### How to Build & Upload
1. Install [PlatformIO](https://platformio.org/) in VS Code.   
2. Navigate to `firmware/buoy_node/`.  
3. Run tasks in PlatformIO:
   - **Build** → compile the firmware  
   - **Upload** → flash to ESP32  
   - **Monitor** → view serial output at `115200 baud`  

### Sensor Tests
Standalone codes for hardware debugging and testing are available in `firmware/sensor_tests/`:
- `gps_test.ino` → GPS only  
- `lora_basic_send.ino` → LoRa only  
- `sd_log_test.ino` → SD card only  

---

## Server (Flask + MQTT)

### Features
- Subscribes to **MQTT topic** (`buoy/data`)  
- Stores the latest messages in memory  
- Displays data on a **real-time web dashboard** (Chart.js)  
- Easy to extend with a database (PostgreSQL, InfluxDB, etc.)  

### How to Run
1. Install Python 3.10+  
2. Navigate to `server/` and install dependencies:  
   ```bash
   pip install -r requirements.txt
3. Run the server: python app.py
4. Open http://localhost:5000 in your browser

---

## System Architecture

1. **ESP32 buoy node**
   Reads sensors -> logs to SD -> transmits via LoRa
2. **LoRa reciever gateaway (e.g. Raspberry Pi)**
   Forwards recieved packets to an MQTT broker.
3. **Flask server**
   Subscribes to MQTT -> serves real-time dashboard via web browser

---

## Future improvements

1. Persistent database logging (PostgreSQL, InfluxDB).
2. Authentication & access control for the dashboard.
3. Advanced visualization (wave height, wind rose, hazard alerts).
4. Remote command/control (server → buoy).
5. Integration with cloud platforms.
