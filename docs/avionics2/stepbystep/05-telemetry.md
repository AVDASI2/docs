# Wifi

The Adafruit HUZZAH ESP8266 is a compact Wi-Fi microcontroller module based on the ESP8266 chip, ideal for IoT projects. It features built-in Wi-Fi, GPIO pins, and supports programming via Arduino or Lua. It can be configured to communicate with the Cube flight controller over Wi-Fi, enabling wireless telemetry, MAVLink communication, and remote parameter tuning.

How to set up the Wifi chip: [ESP8266 Ardupilot guide (ardupilot.org)](https://ardupilot.org/copter/docs/common-esp8266-telemetry.html)

!!! note "You shouldn't need to flash the chip, just set a name and password"

Wifi chip documentation: [Adafruit HUZZAH ESP8266 breakout doc (adafruit.com)](https://cdn-learn.adafruit.com/downloads/pdf/adafruit-huzzah-esp8266-breakout.pdf)

Going to need to update this all for the new wifi protocols.



Using the Wifi module is a bit different but simple. After setting up the Wifi chip (for more information see [Wifi](Wifi.md)), connect the chip to the Cube’s `Telem1/Telem2` port and your computer to the Wifi network. Select the `UDP` setting and hit connect.

!!! tip "If not working, make sure you're still connected to the chip (and not Eduroam) and your GCS isn't connected to the cube"