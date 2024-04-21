""" This is a script to warn the user when they bypass a certain hour """
import sys
import time
import winsound
from datetime import datetime
from tkinter import messagebox as mb

# Variables.
(TITLE, MESSAGE) = ("ALERT", "You have passed enough time using your PC!")
ALERT_FREQUENCY = 1000
ALERT_DURATION = 500
ALERT_COUNT = 20 # How many times to alert the user.
ALERT_DELAY = 5 # How much time to wait after each alert

# Time to show the warning.
LATE_TIME = "01:00"

def check_if_late_time_passed():
    """Check if the late time has been passed."""
    late_time = datetime.strptime(LATE_TIME, "%H:%M").time()
    current_time = datetime.now().time()
    if current_time > late_time:
        return True
    return False


def show_late_alert():
    """Triggers a sound and visual alert."""
    winsound.Beep(ALERT_FREQUENCY, ALERT_DURATION)
    mb.showerror(TITLE, MESSAGE)

while True:
    if check_if_late_time_passed() is True:
        for _ in range(ALERT_COUNT):
            show_late_alert()
            time.sleep(ALERT_DELAY)
        break
    time.sleep(1)

sys.exit()
