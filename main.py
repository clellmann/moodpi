STATUS_LED_GPIO = 21
GROUP_BUTTON_GPIOS = [22, 11, 6, 19, 26]  # Ordered by groups
GROUP_NAMES = ["Gruppe 1", "Gruppe 2", "Gruppe 3", "Gruppe 4", "Gruppe 5"]  # Ordered by groups
GROUP_LED_GPIOS = [23, 8, 12, 16, 20]  # Ordered by groups
MOOD_GPIOS = [10, 5, 13]  # Ordered by moods
MOOD_NAMES = ["gut", "mittel", "schlecht"]  # Ordered by moods
USB_MOUNT_PATH = "/media/usb"

from moodpi.moodpi import MoodPi
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
from time import sleep
import os
import subprocess

if __name__ == "__main__":
    GPIO.setup(STATUS_LED_GPIO, GPIO.OUT)
    GPIO.output(STATUS_LED_GPIO, GPIO.LOW)
    try:
        mood_pi = MoodPi(GROUP_BUTTON_GPIOS, GROUP_NAMES, 
                        GROUP_LED_GPIOS, MOOD_GPIOS, MOOD_NAMES,
                        USB_MOUNT_PATH)
        mood_pi.prepare()
        mood_pi.run()
    except KeyboardInterrupt:
        GPIO.cleanup()
        raise
    except:
        GPIO.output(STATUS_LED_GPIO, GPIO.HIGH)
        sleep(10)
        GPIO.cleanup()
        p = subprocess.Popen("main.py")
