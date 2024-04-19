# Archivo: My74hc595.py
# Autor: Bartolomé Vich Lozano
# Fecha: 19 de Abril de 2024
# Probado en un SP8266 con MicroPython
# DescripciOn: Este cOdigo sirve para encender 8 leds o barra de leds de 8
# Recibe una representaciOn de 8bits  
# Y segUn lo que recibe enciende los leds
from machine import Pin
#define PINs
dataPin = 13
latchPin= 12
clockPin = 14

#set pins to output 
dataPin=Pin(dataPin, Pin.OUT)
latchPin=Pin(latchPin, Pin.OUT)
clockPin=Pin(clockPin, Pin.OUT)

def send(data_bin):
  #put latch down to start data sending
  clockPin.value(0)
  latchPin.value(0)
  clockPin.value(1)
  
  for i in range ( len(data_bin)):
    clockPin.value(0)
    dataPin.value(int(data_bin[i]))
    clockPin.value(1)
    
  #put latch up to send data to the outputs   
  clockPin.value(0)
  latchPin.value(1)
  clockPin.value(1)
