# More

Sorry, docs are quite incomplete at present! Here are links for next steps.

## Servos

* [Ardupilot Servos](https://ardupilot.org/copter/docs/common-servo.html)

You can test these via Mission Planner's 'servos' tab.

## Telemetry

To connect the Cube to your ground station laptop. Once you're talking this way, your USB cable will just be for power - you could move to your separate power supply.

* [Ardupilot Telemetry](https://ardupilot.org/copter/docs/common-telemetry-landingpage.html#common-telemetry-landingpage)
* [Beyond Robotix Kahuna](https://beyond-robotix.gitbook.io/docs/kahuna/quick-start-guide). Start in Access Point Mode, we'll move to Station Mode later on in the lab when we have a wifi router set up.

## RC

Radio comms for your 'safety pilot'. 

* [Ardupilot - RC](https://ardupilot.org/plane/docs/common-rc-systems.html)
* [FrSky Twin X14](https://www.frsky-rc.com/twin-x14-x14s/)
* [FrSky TW MX](https://www.frsky-rc.com/product/tw-mx/)
* [FrSky ETHOS Suite](https://ethos.frsky-rc.com/#ethos-suite) (use 'Getting Started' link, not top-nav menu. Make sure you download the latest 'releaase' version, not a pre-release 'RC'). Use this for updating firmware on transmitter and receiver. You'll need a special cable to connect the receiver to the transmitter for firmware updates - see me.

## Data logging

* [Ardupilot - logging](https://ardupilot.org/plane/docs/common-logs.html)
* [MATLAB - flight log analysis](https://www.mathworks.com/help/uav/flight-log-analysis.html)

## SITL/HITL

* [Software in the loop](https://ardupilot.org/dev/docs/sitl-simulator-software-in-the-loop.html) - for simulation out of the lab
* [SITL with MATLAB](https://ardupilot.org/dev/docs/sitl-with-MATLAB.html) - I haven't used this, let me know if it's any good
* [Hardware in the loop](https://ardupilot.org/dev/docs/hitl-simulators.html) - make your Cube think it's on a plane

## ADC

* [Ardupilot analog inputs](https://ardupilot.org/plane/docs/common-analog-pins.html)
* [Cubepilot ADC](https://docs.cubepilot.org/user-guides/cubenode/functional-overview#analog-to-digital-converter-adc)

## Custom control

More on this later

* [Ardupilot - MAVLink](https://ardupilot.org/dev/docs/mavlink-commands.html)
* [Pymavlink](https://mavlink.io/en/mavgen_python/)
* [Ardupilot - Lua Scripts](https://ardupilot.org/plane/docs/common-lua-scripts.html) - used for some custom mode-switching that we need for tunnel testing. More to follow.
* [Cubepilot I2C](https://docs.cubepilot.org/user-guides/cubenode/functional-overview#inter-integrated-circuit-interface-i2c)

## Initial Steps Cheat Sheet
1. Flash sub firmware then plane firmware
	a. Attach USB/buzzer cable to USB JST port on cube
	b. Connect cube to laptop via USB
	c. Select COM port
	d. Upload sub firmware
	e. Unplug and reconnect, wait for beep
	f. Connect on mission planner (via MAVLINK+ com port, first one) to test it works
	g. Disconnect on mission planner
	h. Upload plane firmware
	i. Unplug and reconnect on mission planner, wait for beep
2. Reset buzzer noise
	a. Go to config -> parameters -> search buzzer. Set to 5%, click write params
	b. To reboot (to apply buzzer), either reconnect USB or Ctrl+F then click "reboot Pixhawk"
3. Configure WiFi telemetry
	a. Connect GH TELEM Cable to purple wifi telemetry
	b. Connect to BeyondRobotix (password: beyondrobotix) then go to 192.168.4.1
	c. Change AP SSID to Kit[Num]
	d. Click save
4. RC radio binding
	a. Create new model (plane, 1 channel aileron flap elevator and rudder) on transmitter
	b. Go to register mode on transmitter, reboot cube while holding down button on rc radio
    c. Click register then click bind
