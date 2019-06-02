from machine import Pin, PWM
import time
import math

CYCLES=5
STEP_DELAY_MS=40

FREQ=1000
DUTY=500

def pulse(led_red, led_green, led_blue, t):
     for i in range(0, 60):
          led_red.duty(int(math.sin(i / 30 * math.pi) * DUTY + DUTY))
          led_green.duty(int(math.sin((i+20) / 30 * math.pi) * DUTY + DUTY))
          led_blue.duty(int(math.sin((i+40) / 30 * math.pi) * DUTY + DUTY))
          time.sleep_ms(t)


led_red = PWM(Pin(23), freq=FREQ, duty=0)
led_green = PWM(Pin(22), freq=FREQ, duty=0)
led_blue = PWM(Pin(21), freq=FREQ, duty=0)

for i in range(CYCLES):
     pulse(led_red, led_green, led_blue, STEP_DELAY_MS)

led_red.deinit()
led_green.deinit()
led_blue.deinit()
