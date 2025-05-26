# Data Logging

## Downloading Cube logs

The flight controller automatically creates a log of all its sensors (IMUs, temp. sensors, etc.) and its attitude changes during operation into a .bin file. These are necessary to analyse the behaviour of the drone in the wind tunnel and should be downloaded after each test so that the appropriate Teams of the Company can use their data.

## Optional: Logging through LUA scripts

LUA scripts can create and modify files on the Cube’s memory; therefore, it is possible to create logs using LUA scripts (i.e. saving flap angles from the sensor into a CSV). This should only be done for a few sensors only, as it requires a lot of processing power from the flight controller. The example scripts will showcase this as well.

## MatLab data analysis

Using matlab flight add on