# PyMAVLink

The cube uses MAVLink, a lightweight communication protocol to receive commands and transmit data to and from the Ground Station. Python has a MAVLink module called Pymavlink that will allow to send and capture MAVLink messages.

To be able to do so, first the code must connect to the Cube through MAVLink (see [Cube Information](Cube-Information.md) for how to physically connect to the Cube). An example code will be provided to show a baseline for how to connect to the flight controller with python. (See [GS.py](Example-code.md#gs-py))

Another example code will show how to send commands over MAVLink (in particular, arming the Cube see [Arm.py](Example-code.md#arm-py)). Use this to develop your code.

Sending Commands using MAVLINK: Use the `command_long_send` function of the mavlink library to send control demands to the cube.

This command takes 7 parameters: 
```
(target_system, target_component, command, confirmation, param1 - 7)
```