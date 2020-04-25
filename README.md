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

For the hardware setup, you first assemble the raspberry with power and cover.

Then you prepare the periphery with the breadboard, the LEDs, the buttons and the jumper wires. You need as many buttons as you have groups + satisfication levels. The number of LEDs is the number of groups (depicting which group is selected) + a status LED.<br>
You connect the buttons with the jumpers to different raspberry GPIOs, supplied with 5 V and a resistor in the curcuit.

$R=\frac{U}{I}=\frac{5 V}{0.015 A} \approx 330 Ω$

The LEDs you put into a curcuit between switchable GPIO and GND with a current limiting resistor.

$R=\frac{U}{I}=\frac{5 V-2 V}{0.015 A} \approx 220 Ω$

GPIO-Pinout:

![gpio3](./img/gpio3.png)

In the end it can look like this:

![periphery](./img/periphery.jpg)

## Software

### Requirements

- Latest Raspbian image
- Imager

### Setup

For the software setup, you first [initialize](https://www.raspberrypi.org/documentation/installation/installing-images/README.md) the raspberry with the latest raspbian version.