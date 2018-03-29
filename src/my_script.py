import wiringpi

print("Starting script...")

# Set up GPIO pin numbering
wiringpi.wiringPiSetupGpio()

# Read pin 6
pin_value = wiringpi.digitalRead(6)

print("Pin 6: " + str(pin_value))