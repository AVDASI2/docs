# Mission Planner

Most useful bits of it.

Mission planner is the software used to communicate and control the cube. Your code should replace Mission Planner and provide the same basic functionality. Mission planner is still useful to use for testing and has numerous vital features.

[Installation info](https://ardupilot.org/planner/docs/mission-planner-installation.html)

[Mission Planner overview](https://ardupilot.org/planner/docs/mission-planner-overview.html)

## Connecting
Mission Planner can be connected to the Cube over Wifi and USB. If connecting through USB, <u>**make sure to use the buzzer**</u>; do not plug the cable directly into the Cube. In mission planner, on the top right of the window, you will see two selection boxes and a `Connect` button. If you know which `COM` terminal you plugged the USB into, select it, but there is an `AUTO` function too. Wait until the buzzer buzzes before clicking connect.

![Connecting MP](assets/connect-MP.png)

Using the Wifi module is a bit different but simple. After setting up the Wifi chip (for more information see [Wifi](Wifi.md)), connect the chip to the Cube’s `Telem1/Telem2` port and your computer to the Wifi network. Select the `UDP` setting and hit connect.

## Parameters

When first connecting to the cube, there are a few parameters that need changing. In Mission Planner, a parameter is a configurable setting that tells the flight controller (like the Cube) how to behave. Parameters control everything from flight modes, sensor settings, failsafes, and PID tuning, to things like which servo does what and how fast a drone should climb or descend.

To access parameters, go to config and then full parameter list. This opens up every single parameters available for you to change. Scroll or search for `NFT_BUZZ_VOLUME` and turn it down so the cube doesn’t scream at you every time you turn it on. Then click `write params` and congratulations you’ve changed the cube settings. Don’t forget to save your parameters every so often so you don’t lose them.

## Servo/Actions

`Ctrl F` opens up some sort of settings thing. Click `toggle servo safety` to turn off safety. In `Actions` there’s the arm button.
