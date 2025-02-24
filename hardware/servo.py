# vein_finder/hardware/servo.py
import RPi.GPIO as GPIO
import time

SERVO_PIN = 18  # GPIO pin for servo signal


def setup():
    """Set up PWM for the servo motor."""
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(SERVO_PIN, GPIO.OUT)
        pwm = GPIO.PWM(SERVO_PIN, 50)  # 50 Hz for typical servo
        pwm.start(0)  # Start with no signal
        print("Servo PWM setup complete")
        return pwm
    except Exception as e:
        print(f"Error setting up servo: {str(e)}")
        raise


def set_angle(pwm, angle):
    """Set the servo to a specific angle (0-180 degrees)."""
    try:
        duty = angle / 18 + 2  # Map 0-180 degrees to 2-12% duty cycle
        pwm.ChangeDutyCycle(duty)
        time.sleep(0.5)  # Allow servo to move
        pwm.ChangeDutyCycle(0)  # Stop signal to reduce jitter
        print(f"Servo moved to {angle} degrees")
    except Exception as e:
        print(f"Error setting servo angle: {str(e)}")
        raise


def point_laser(pwm, x_coord, image_width, physical_width):
    """
    Point the laser based on image x-coordinate.

    Args:
        pwm: PWM object for servo control.
        x_coord (int): X-coordinate of the vein in the image.
        image_width (int): Width of the image in pixels (e.g., 640).
        physical_width (float): Physical width of the scan area in cm.
    """
    try:
        # Map image x-coordinate to physical position and then to servo angle
        physical_pos = (x_coord / image_width) * physical_width
        angle = (physical_pos / physical_width) * 180  # Scale to 0-180 degrees
        set_angle(pwm, angle)
        print(f"Laser pointed at x={x_coord} (angle={angle:.1f}°)")
    except Exception as e:
        print(f"Error pointing laser: {str(e)}")
        raise


def cleanup(pwm):
    """Clean up servo PWM and GPIO resources."""
    try:
        pwm.stop()
        GPIO.cleanup(SERVO_PIN)
        print("Servo cleanup complete")
    except Exception as e:
        print(f"Error cleaning up servo: {str(e)}")
        raise
