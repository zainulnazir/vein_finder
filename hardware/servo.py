pwm = _gpio.PWM(18, 50)
pwm.start(0)
set_angle(pwm, angle)  # Map x-coordinate to 0-180 degrees
