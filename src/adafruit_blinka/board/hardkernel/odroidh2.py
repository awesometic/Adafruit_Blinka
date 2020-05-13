"""Pin definitions for the Odroid H2."""

class Pin:
    def __init__(self, pin_id):
        self.id = pin_id

# Dummy pins to use I2C
# pin_id represents the physical pin number on Odroid-H2 board
I2C6_SDA = Pin(20)
I2C6_SCL = Pin(18)
I2C7_SDA = Pin(15)
I2C7_SCL = Pin(13)

i2cPorts = (
    (6, I2C6_SDA, I2C6_SCL),
    (7, I2C7_SDA, I2C7_SCL),
)
