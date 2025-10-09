# Mission Planner

Mission Planner is a full-featured ground station application for the ArduPilot open source autopilot project. We will use it to set up the Cube and for initial learning and operation.

!!! info
    Mission Planner requires Windows - I've had some success running it via [Whisky](https://getwhisky.app) on my Mac (update: Whisky is being discontinued, try [WINE](https://www.winehq.org) either directly or via [CrossOver](https://www.codeweavers.com/crossover), or use [Parallels](https://www.parallels.com), [VirtualBox](https://www.virtualbox.org) or [VMWare](https://www.vmware.com/products/desktop-hypervisor/workstation-and-fusion)), but the uni cannot offer support for this approach. **Never** use virtualisation for flight (and wind tunnel) operations.

Take a look at Ardupilot's overview page, then install Mission Planner.

* [:material-step-forward:Ardupilot - Mission Planner Overview](https://ardupilot.org/planner/docs/mission-planner-overview.html)
* [:material-step-forward:Ardupilot - Installing Mission Planner](https://ardupilot.org/planner/docs/mission-planner-installation.html)

!!! info "Mission Planner/Altitude Angel"
    Updated Sept 2025. Mission Planner now prompts you to log in to Altitude Angel - you don't need to do this. Altitude Angel is a flight-restriction update service, which is handy for outdoor flying but their scope does not cover our wind tunnels.

## Connecting

For this first stage we'll power the Cube from your computer's USB port.

!!! warning "A really important note on power"
    **Do not plug anything else into the Cube if you're just powering from USB**. Your laptop's USB port is limited in the current it can supply, and servos can draw significant current when stalled (more on this in later steps). In short, if you plug stuff in and do the wrong thing you can at best **fry the Cube** (putting your Team, Division, and Company's success at risk), and at worst **fry your laptop** (possibly putting your degree and life at risk - back things up, kids!).

!!! warning "Another important note on connectors"
    The micro-USB connector on the side of the Cube is notoriously fragile. To prevent *expensive* damage, please use the USB socket/buzzer assembly supplied to connect (these are much cheaper to replace).

Connect the USB/buzzer assembly to the carrier board's `USB` port. Follow the Ardupilot instructions, making sure you use that USB socket. When you are asked to select firmware, choose ArduPlane. Connect Mission Planner to the Autopilot and check things work as expected (ignore the parts about telemetry and multiple vehicles).

* [:material-step-forward:Ardupilot - Installing Firmware](https://ardupilot.org/planner/docs/common-loading-firmware-onto-pixhawk.html)
* [:material-step-forward:Ardupilot - Connect Mission Planner to AutoPilot](https://ardupilot.org/planner/docs/common-connect-mission-planner-autopilot.html)

!!! info "CubeOrange+"
    When uploading firmware, you are given a choice between "CubeOrange+" and "CubeOrange+ bdsht". Select "CubeOrange+" to upload firmware.

!!! info "Restoring Ardupilot firmware"
    There are some parameters that don't get reset when you re-flash the same firmware. To do a full 'factory settings' reset the easiest way we've found is to flash a different firmware. We like making our UAVs think they're a submarine then re-re-flashing one of the airborne versions.


## Parameters

In Mission Planner, a parameter is a configurable setting that tells the flight controller how to behave. Parameters control everything from flight modes, sensor settings, failsafes, and PID tuning, to things like which servo does what and how fast a drone should climb or descend.

Many parameters can be adjusted via the various Mission Planner graphical interface screens, but you can also edit them directly, and some are only available in the full parameter list. It's a little intimidating at first, and you need to be careful not to inadvertently break things!

Let's turn down the very loud (by design - you want to be able to hear it outdoors) buzzer that beeps on startup. To access parameters, go to 'config' and then 'full parameter list'. Scroll or search for `NFT_BUZZ_VOLUME` and set it to a low number (1-5). Click `write params` and settings should take effect immediately. 

| Parameter           | Recommended value     | Description                                                      |
|---------------------|-----------|--------------------------------------------------------------|
| `NTF_BUZZ_VOLUME`   | 1–5       | Sets buzzer volume level. Default is LOUD!                                     |


# More

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

* ## Initial Steps Cheat Sheet
* 	1. Flash sub firmware then plane firmware
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
