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

def prepare_to_get():
  #put latch down to start data sending
  clockPin.value(0)
  latchPin.value(0)
  clockPin.value(1)

def execute_to_send():
  #put latch up to send data to the outputs   
  clockPin.value(0)
  latchPin.value(1)
  clockPin.value(1)

'''
example to use 
My74hc595.send_num('10101010')
'''    
def send(data):

  prepare_to_get()
  
  for i in range ( len(data)):
    clockPin.value(0)
    dataPin.value(int(data[i]))
    clockPin.value(1)
  
  execute_to_send() 

'''
#example to use, count 0 t0 255
from time import sleep_ms
for a in range (256):
  My74hc595.send_num(a)
  sleep_ms(100)
''' 

def send_num(data):

  data = str(bin(data)[2:])
  num_dif = 8 - len(data)
  print((num_dif*"0")+data)
  new_data = (num_dif*"0")+data

  prepare_to_get()
  
  for i in range (len(new_data)):
    clockPin.value(0)
    dataPin.value(int(new_data[i]))
    clockPin.value(1)
  
  execute_to_send()
  
