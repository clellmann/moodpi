# MoodPi

MoodPi is an interactive mood collection system for satisfication analysis. It is based on Raspberry Pi and some peripherical hardware.<br>
It differs among different analysed groups (e.g. departments) and different satisfication levels of persons on a daily basis.

## Hardware 

### Requirements

- Raspberry Pi 3 Model B or newer
- Micro USB power adapter for raspberry supply
- SD card for Raspbian OS
- evtl. Raspberry Cover
- Some LEDs
- Hardware Buttons
- Breadboard
- Jumper wires
- USB stick

### Setup

For the hardware setup, you first assemble the raspberry with power and cover and USB stick.

Then you prepare the periphery with the breadboard, the LEDs, the buttons and the jumper wires. You need as many buttons as you have groups + satisfication levels. The number of LEDs is the number of groups (depicting which group is selected) + a status LED.<br>
You connect the buttons with the jumpers to different raspberry GPIOs, supplied with 5 V and a resistor in the circuit.

<img src="https://render.githubusercontent.com/render/math?math=R=\frac{U}{I}=\frac{5 V}{0.015 A} \approx 330 Ω">

The LEDs you put into a circuit between switchable GPIO and GND with a current limiting resistor.

<img src="https://render.githubusercontent.com/render/math?math=R=\frac{U}{I}=\frac{3.3 V-2 V}{0.006 A} \approx 220 Ω">

GPIO-Pinout:

![gpio3](./img/gpio3.png)

In the end it can look like this:

![hardware](./img/hardware.jpg)

## Software

### Requirements

- Latest Raspbian image
- Imager

### Setup

For the software setup, you first [initialize](https://www.raspberrypi.org/documentation/installation/installing-images/README.md) the raspberry with the latest raspbian version. Then you load the Python files to the raspberry.

In `main.py` change the GPIO globals to your setup and the name globals to your group and mood names stored. Set the USB mount global to your USB path (the best is to mount USB to a fixed path, see: [USB mount](https://www.elektronik-kompendium.de/sites/raspberry-pi/2012181.htm)).<br>
Subsequently, you can use `main.py` to start the MoodPi by typing `python3 main.py` on your raspberry.

The buttons will be evaluated every 250 ms. If a mood is stored, the input is blocked for 5 s for the reason of not storing to many moods with the evaluation cycle.

In case of exception the status LED is iluminated 10 s before automatic restart.

To start the program with raspberry reboot enter `@reboot python3 <path>/main.py` to `crontab -e`.

## Function

When pushing a group button, the corresponding LED iluminates. Then pushing a mood button triggers the storage of mood and group data with datetime to a daily csv file on USB stick. The further input is blocked for 5 s shown by all group LEDs that iluminate to avoid multiple data storings. Subsequently, when all LEDs except for the active group LED are turned off, the group can be changed or another mood can be input.

In case of error the status LED is iluminated 10 s before automatic restart.