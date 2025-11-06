# Lua Scripting

The Cube also supports Lua scripting (via ArduPilot), enabling onboard automation such as custom sensor logging, custom failsafes, LED behavior, telemetry filtering, or mission logic without requiring firmware modification. Lua is a lightweight, high-level scripting language designed for embedded systems, making it ideal for writing custom logic directly on the Cube.

!!! tip "Don't be scared of Lua!"
    Its a strange programming language but needs to be used as its the only way to write onboard code for the Cube.
    You'll get used to it don't worry.

Ardupilot scripting support page: [Common Lua scripts (ardupilot.com)](https://ardupilot.org/copter/docs/common-lua-scripts.html)

## Enabling scripting on the CubePilot

Before Lua scripts can be executed onboard the flight controller, the scripting feature must be enabled using the parameters of the Cube. Using Mission Planner (or any other similar GS program), locate the `SCR_ENABLE` parameter and set it to `1` before rebooting the Cube. A new folder should appear in the `APM` folder named `scripts`; if it doesn’t, it needs to be manually created. After this is done, any Lua code uploaded into this folder will be automatically executed when the Cube is rebooted after uploading.

To access the Cube's directories, go to Config -> MAVftp on Mission Planner.

## Example Lua Script - Outputting and Logging Analogue Sensor Data

The following script is an example code which logs data from an analogue sensor plugged into the "ADC" port on the Cube's carrier board. The script logs data for 1 minute, at 1Hz, outputting the readings to the "Messages" tab in Mission Planner and saving the results to potentiometer_log.csv. Once the minute has passed, navigate to the Cube's root directory (Config -> MAVftp).

The code is well commented - the idea is that you can adapt it to your needs and desires. Make sure to consult the scripting docs above, and see what you can create!

```
-- Minimum working example: Logging analog readings from CubeOrange+ ADC port to a .csv file on the Cube's SD card.
local file_name = "potentiometer_log.csv" -- Log file name
local file -- File object initialisation
local analog_in = analog:channel()
local pot_voltage = {} -- Table to hold potentiometer voltage readings
local count = 0 -- Readings counter initialisation
local READINGS_COUNT = 60 -- Number of readings to log
local LOOP_DELAY_MS = 1000 -- Delay between readings in milliseconds

if not analog_in:set_pin(8) then
  gcs:send_text(0, "Invalid analog pin")
end -- Sets ADC pin 8 for potentiometer input

file = io.open(file_name, "a")
if not file then
  error("Could not make file")
end -- Opens file for data logging

file:write('Time [ms], Potentiometer Voltage [V]\n')
file:flush() -- Writes CSV header

local function write_to_file()
  if not file then
    error("Could not open file")
  end -- Error check
  file:write(tostring(millis()) .. ", " .. table.concat(pot_voltage,", ") .. "\n") -- Writes data with timestamp, in CSV format
  file:flush() -- Updates the file
end -- Writes data to file

function update()
  pot_voltage[1] = analog_in:voltage_latest() -- Gets latest voltage reading from potentiometer
  gcs:send_text(0, string.format("Potentiometer Voltage: %.2f V", pot_voltage[1])) -- Outputs voltage to GCS
  write_to_file() -- Calls function to write data to file
  count = count + 1
  if count >= READINGS_COUNT then
    file:close()
    return nil
  end -- Stops logging after set number of readings
  return update, LOOP_DELAY_MS
end

return update()
```