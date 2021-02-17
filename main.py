
# from machine import Pin, I2C, ADC,
# import ssd1306
# from time import sleep

# # ESP32 Pin assignment 
# i2c = I2C(-1, scl=Pin(22), sda=Pin(21))

# oled_width = 128
# oled_height = 64
# oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# pot = ADC(Pin(33))
# pot.atten(ADC.ATTN_11DB)       #Full range: 3.3v

# while True:
#     oled.fill(0)
#     oled.show()
#     pot_value = pot.read()
#     print(pot_value)
#     pot_value_str = str(pot_value)
#     oled.text(pot_value_str, 0, 10)
#     oled.text("For Science!", 0, 50)
#     oled.show()
    
# Complete project details at https://RandomNerdTutorials.com

from machine import Pin, I2C, ADC
import ssd1306
from time import sleep

i2c = I2C(-1, scl=Pin(22), sda=Pin(21))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

pot = ADC(Pin(33))
pot.atten(ADC.ATTN_11DB)       #Full range: 3.3v

motion = False

def handle_interrupt(pin):
  global motion
  motion = True
  global interrupt_pin
  interrupt_pin = pin 

pir = Pin(33, Pin.IN)

pir.irq(trigger=Pin.3, handler=handle_interrupt)

while True:
  if motion:
    print('Motion detected! Interrupt caused by:', interrupt_pin)
    pot_value = pot.read()
    print(pot_value)
    pot_value_str = str(pot_value)
    oled.text(pot_value_str, 0, 10)
    oled.text("For Science!", 0, 50)
    oled.show()
    sleep(5)
    oled.fill(0)
    oled.show()
    print('Motion stopped!')
    motion = False

