# Telemetry

Let's start to free you from the shackles of the USB cable.

So far, you've been talking to your Cube over a USB-Serial connection, either with Mission Planner auto-connecting or you manually choosing the correct COM port. They can communicate over various other protocols, including WiFi.

We'll use a common WiFi chip called an ESP8266, and initially set it up so that your Cube appears as a WiFi access point to which you can connect your laptop. Later on we may move to 'station' mode when we have routers set up in the lab.

When you power on your telemetry board it will broadcast a WiFi SSID, but the default configuration means that everyone's will be called the same thing! Coordinate with other groups to ensure you're connecting to yours not theirs, and the first thing you should do is rename the SSID to match your kit number - we suggest AVDASI2-Kitx. Leave the password as default, so that we can troubleshoot easily and reset for next year.

* [:material-step-forward:Beyond Robotix Kahuna](https://beyond-robotix.gitbook.io/docs/kahuna/quick-start-guide) - the ESP8266 board we use. Connect to the TELEM1 port.
* [:material-information:Ardupilot Telemetry](https://ardupilot.org/copter/docs/common-telemetry-landingpage.html#common-telemetry-landingpage) - lots more options, but not needed for AVDASI2.

Now you're talking to the Cube wirelessly, all the USB cable is doing is providing power!

!!! tip
    Mission Planner should connect automatically - if not, set the comms protocol to UDP, baud 57600.
    
    If not working, make sure you're still connected to the chip (and not Eduroam) and your GCS isn't connected to the Cube over USB-Serial"