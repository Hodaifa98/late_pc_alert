""" This is a script to warn the user when they bypass a certain hour """
import sys
import time
import winsound
from datetime import datetime, timedelta
from tkinter import messagebox as mb

# Variables.
(TITLE, MESSAGE) = ("ALERT", "You have passed enough time using your PC!")
ALERT_FREQUENCY = 1000
ALERT_DURATION = 500
ALERT_COUNT = 10 # How many times to alert the user.
ALERT_DELAY = 5 # How much time to wait after each alert

# Time to show the warning. (24h format, may or may not account for 24h format)
LATE_TIME = "00:00"

def has_time_passed(input_time):
    """
        Check if the input time has been passed or not.

        Args:
            input_time: The time to check
        Returns:
            True if the input time has passed, False otherwise
    """
    # Get current time and parse it.
    now = datetime.now()
    input_time_dt = datetime.strptime(input_time, "%H:%M").time()
    input_dt = datetime.combine(now.date(), input_time_dt)

    # Check if the input time is considered to be on the next day.
    if now.time() < datetime.strptime("06:00", "%H:%M").time():
        if input_time_dt > datetime.strptime("06:00", "%H:%M").time():
            input_dt -= timedelta(days=1)

    # Compare the times.
    return now >= input_dt


def show_late_alert():
    """Triggers a sound and visual alert."""
    winsound.Beep(ALERT_FREQUENCY, ALERT_DURATION)
    mb.showerror(TITLE, MESSAGE)

try:
    print("Program has started.")
    while True:
        if has_time_passed(LATE_TIME) is True:
            print("Late time has passed!")
            for _ in range(ALERT_COUNT):
                show_late_alert()
                time.sleep(ALERT_DELAY)
            break
        time.sleep(1)
except Exception as e:
    print("An error occured: ", e)
finally:
    sys.exit()
