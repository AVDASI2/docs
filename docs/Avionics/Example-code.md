# Example Code

A series of scripts were written to show a minimum viable ground station. Keep in mind your code will need to be better than this, you can’t just copy it and hope for the best. It does provide a baseline to build off of and an example of how to meet the basic functionality needed.

Each script should be able to be executed individually but Main.py allows you to execute them all simultaneously. You don’t need to take your approach in your own GS but this is good since you can debug each function independently.

## Main.py

Links all the scripts together. Call each script as a function after defining them up top.

```python title="main.py"
--8<-- "docs/code/main_example.py"
```

## GS.py {#gs-py}

This script is what connects the cube to your ground station. It creates the connection, waits for a heartbeat, and after heartbeat is received it listens and prints messages. There’s a wide range of messages and statuses you can listen for from the cube, some more useful than others, so up to you to figure out which ones you want. It also notifies you if the heartbeat is interrupted.

## Arm.py {#arm-py}

This script allows you to arm/disarm the cube and toggle its safety switch. Arming allows logging and the safety switch locks all servo movement. 

## Servo.py

This script actuates the movement of a servo. You’ll have to edit it to allow multiple servos moving simultaneously. 

## UI.py

This script is a barebones user interface for a GCS. It uses tkinter python module. This was used for its simplicity but you can use whatever module or language you want (there’s some that can make really nice looking UIs). The UI calls functions from the previous arming and servo controller scripts and maps them to buttons. It also allows you to input a specific servo angle and move the servo accordingly.