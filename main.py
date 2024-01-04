from machine import ADC, Pin
import time
import math

# ADC setup
adc = ADC(0)  # create ADC object on ADC pin
series_resistor = 10000  # Resistance of the fixed resistor in Ohms

def read_temperature():
    adc_value = adc.read()  # read value using ADC
    if adc_value == 0:
        return None  # Return None if ADC value is 0 to prevent division by zero

    resistance = series_resistor / ((1023.0 / adc_value) - 1.0)

    # Steinhart-Hart equation coefficients (replace with your thermistor's values)
    A = 1.009249522e-03
    B = 2.378405444e-04
    C = 2.019202697e-07

    temperature = 1.0 / (A + B * math.log(resistance) + C * math.log(resistance)**3)
    temperature = temperature - 273.15  # Convert Kelvin to Celsius
    return temperature

while True:
    temp = read_temperature()
    if temp is not None:
        print("Temperature: {:.2f} C".format(temp))
    else:
        print("Error: ADC value is 0. Check thermistor connections.")
    time.sleep(1)  # Wait for 1 second
