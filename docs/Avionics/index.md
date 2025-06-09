# Avionics Guidelines

The goal of this section is to lay out a minimum viable product for the avionics portion of the AVDASI 2 course. Hopefully a clear baseline is established for a test-ready avionics system.

Most links are to external open-source resources from which you should be able to get creative and implement creative solutions to fulfill the requirements of the course.

!!! tip "When in doubt consult the [ardupilot.org](ardupilot.org) website."

!!! abstract "The docs will walk you through all the necessary subcomponents of your Avionics system."

    The Cube is your main flight computer, you will be guided on how to plug it in and what all its gadgets do. 

    Mission Planner is a software that lets you do your initial setup, you'll be shown how to connect to the cube, configure parameters, and set up servos. 

    PyMAVLink is the communication protocol used in your custom GCS. 

    The Wifi and RC sections show you how to set up the necessary telemtry systems. 

    I2C & LUA section gives you a quick runthrough on how to write onboard code for the Cube and set up sensor communication. 
 
    Data Logging is a vital component of your system, necesarry for the other subteams in your company that rely on the test results, you'll be shown various ways to store, extract, and postprocess data from the Cube.

    The example code section is a series of scripts written to demonstrate a minimum viable ground station, carefully crafted by master coders for you to use as a basis for your own development.

- [Cube Information](Cube-Information.md)
- [Mission Planner](Mission-Planner.md)
- [PyMAVLink](PyMavlink.md)
- [Wifi](Wifi.md)
- [RC](RC.md)
- [I2C & LUA](I2C&LUA.md)
- [Data Logging](Data-Logging.md)
- [Example Code](Example-code.md)
- [Pressure Sensor PDF](pressure.md)