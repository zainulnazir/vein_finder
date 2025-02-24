import RPi.GPIO as _gpio
_gpio.setmode(_gpio.BCM)
_gpio.setup(17, _gpio.OUT)
_gpio.output(17, _gpio.HIGH)  # Turn on
