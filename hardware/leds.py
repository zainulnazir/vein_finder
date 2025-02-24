# vein_finder/hardware/leds.py
import RPi.GPIO as GPIO

LED_PIN = 17  # GPIO pin for IR LEDs


def setup():
    """Set up GPIO for IR LEDs."""
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(LED_PIN, GPIO.OUT)
        GPIO.output(LED_PIN, GPIO.LOW)  # Start with LEDs off
        print("LED GPIO setup complete")
    except Exception as e:
        print(f"Error setting up LEDs: {str(e)}")
        raise


def turn_on():
    """Turn on the IR LEDs."""
    try:
        GPIO.output(LED_PIN, GPIO.HIGH)
        print("IR LEDs turned on")
    except Exception as e:
        print(f"Error turning on LEDs: {str(e)}")
        raise


def turn_off():
    """Turn off the IR LEDs."""
    try:
        GPIO.output(LED_PIN, GPIO.LOW)
        print("IR LEDs turned off")
    except Exception as e:
        print(f"Error turning off LEDs: {str(e)}")
        raise


def cleanup():
    """Clean up GPIO resources."""
    try:
        GPIO.cleanup(LED_PIN)
        print("LED GPIO cleanup complete")
    except Exception as e:
        print(f"Error cleaning up LEDs: {str(e)}")
        raise
