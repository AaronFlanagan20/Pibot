# Gesture-based UI project

Supervisor: Damien Costello

Developers: David Hynes, Ciaran Brennan, Aaron Flanagan.

Video: [Video of project running](https://www.youtube.com/watch?v=VdV43RQy9BA&feature=youtu.be)

# Background
This project was developed for our 4th year of software development in Galway-Mayo Institute of Technology. It is based on a human controlled search and rescue robot using the [Myo Gesture controlled armband](https://www.myo.com/) as the controller and a [Raspberry PI](https://www.raspberrypi.org/) acting as the robot.

# Technology

* Raspberry PI
* Myo armband
* Breadboard
* 220k and 330k resistors.
* Male and female connector cables
* Led lights
* Putty to telnet from the hosts computer to the pi.
* Xming to view the pi's GUI on the hosts machine.

The main component is the Raspberry PI. An external network adapter is used to connect to a network for internet access. The camera is used to stream what the robot sees back to the screen. The raspberry pi isn’t a very powerful device the the frame rate is quite slow. It uses the connection cables to connect the breadboard to the pin headers on the Raspberry PI. 220 kb resistors are then used to wire the LEDs to a ground current. They are then programmed to ﬂash to simulate motor movement using python and the GPIO library available. Finally we use the myo armband to control the robots movement. If a ﬁst pose is made the robot moves forward, if a stop pose is made it stops. If the hand is left or right it turns. A problem occurred that the Myo wouldn’t connect to the Raspberry PI. Myo doesn’t have Linux support so we had to ﬁnd a custom made package. [PyoConnect](www.fernandocosentino.net/pyoconnect/) was used, it is a python made library that reﬂects the original LUA library. It can be found at www.fernandocosentino.net/pyoconnect/. The operating system we use is Raspbian which is a Debian based system and this library is made for Debian operating systems however it wouldn’t connect. It did connect to an Ubuntu system on one of the developers laptops so we wrote the script on this to show how it would of worked if there wasn’t a hardware compatibility issue.

# Scripts
The main scripts are contained in the [pi-scripts](pi-scripts/) folder of this repository. Unfortunately the project was not a complete success and it is explained within the [report](report.pdf) file in this repo. [Camera.py](pi-scripts/camera.py) uses the openCV library to create a run and constant stream from the raspberry pi and display on the Xming desktop of the connecting machine. [pibot.py](pi-scripts/pibot.py) is used to control the LEDS, how fast they flash and how long they flash. The [controller.py](pi-scripts/controller.py) script was written for use in the [Myo4linux](https://github.com/Ramir0/Myo4Linux) library, however we could not get this working due to the fact that it would compromise the other developers work and be know longer useful to use if we re-program it to our needs. Finally the [pyoconnect.py](pi-scripts/pyoconnect.py) script was used for the PyoConnect library, noted above. This library has some hardware compatability problems with our Raspberry PI resulting in a connection not being made.