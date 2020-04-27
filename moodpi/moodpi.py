import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
from datetime import datetime

class MoodPi():
    """MoodPi class of one satisfication setup.

    Args:
        group_button_gpios (list): List of group button GPIO numbers
        group_names (list): List of group names used for storage
        group_led_gpios (list): List of group led GPIO numbers
        mood_gpios (list): List of mood button GPIO numbers
        mood_names (list): List of mood names used for storage
    """
    group_button_gpios = None
    group_names = None
    group_led_gpios = None
    mood_gpios = None
    mood_names = None

    def __init__(self, group_button_gpios, group_names, 
                group_led_gpios, mood_gpios, mood_names):
        self.group_button_gpios = group_button_gpios
        self.group_names = group_names
        self. group_led_gpios = group_led_gpios
        self.mood_gpios = mood_gpios
        self.mood_names = mood_names

    def run():
        """Main method for MoodPi runs
        """
        while(True):
