import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
from datetime import datetime
from time import sleep

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
    group_states = None
    WRITE_BLOCKAGE = 10  # *500 ms

    def __init__(self, group_button_gpios, group_names, 
                group_led_gpios, mood_gpios, mood_names):
        self.group_button_gpios = group_button_gpios
        self.group_names = group_names
        self.group_led_gpios = group_led_gpios
        self.mood_gpios = mood_gpios
        self.mood_names = mood_names
        self.group_states = [0 for button in self.group_button_gpios]

    def prepare(self):
        """Preparation for GPIO setup
        """
        for gpio in self.group_button_gpios:
            GPIO.setup(gpio, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        for gpio in self.group_led_gpios:
            GPIO.setup(gpio, GPIO.OUT)
            GPIO.output(gpio, GPIO.LOW)
        for gpio in self.mood_gpios:
            GPIO.setup(gpio, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def run(self):
        """Main method for MoodPi runs (500 ms cycle)
        """
        write_block_counter = 0
        while(True):
            if write_block_counter > 0:
                write_block_counter = write_block_counter-1
            for i, (gpio, state) in enumerate(zip(self.group_button_gpios, 
                                                  self.group_states)):
                if state == 0:
                    if GPIO.input(gpio) == GPIO.HIGH:
                        self.group_states = [1 if i == j else 0 for j in 
                                                    range(len(self.group_states))]
                        [GPIO.output(led_gpio, GPIO.HIGH) if i == j else GPIO.output(led_gpio, GPIO.LOW)
                         for j, led_gpio in enumerate(self.group_led_gpios)]
            for gpio, mood in zip(self.mood_gpios, self.mood_names):
                if write_block_counter == 0:
                    [GPIO.output(led_gpio, GPIO.HIGH) if state == 1 else GPIO.output(led_gpio, GPIO.LOW) 
                     for state, led_gpio in zip(self.group_states, self.group_led_gpios)]
                    if GPIO.input(gpio) == GPIO.HIGH:
                        # write to USB storage: datetime, mood, [group for group, state in zip(self.group_names, self.group_states) if state == 1][0]
                        write_block_counter = self.WRITE_BLOCKAGE
                        [GPIO.output(led_gpio, GPIO.HIGH) for led_gpio in self.group_led_gpios]
            sleep(0.5)
