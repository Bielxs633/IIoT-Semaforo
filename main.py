from machine import Pin
from utime import sleep

led_verde = Pin(4, Pin.OUT)
led_amarelo = Pin(2, Pin.OUT)
led_vermelho = Pin(0, Pin.OUT)

while True:   

    led_verde.on()    
    print ("Aberto")    
    sleep(20)    
    led_verde.off()

    sleep(0.5)

    led_amarelo.on()    
    print ("Cuidado")    
    sleep(10)    
    led_amarelo.off()

    sleep(0.5)

    led_vermelho.on()    
    print ("Fechado")    
    sleep(7)    
    led_vermelho.off()

    sleep(0.5)