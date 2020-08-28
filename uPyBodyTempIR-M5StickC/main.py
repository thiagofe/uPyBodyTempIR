"""
MicroPython for M5StickC
Version: 0.1 @ 08-11/04/2020
Authors: Thiago Ferreira Santos, Pedro Henrique Robadel
E-mail: thiago_fisica@outlook.com, ph.robadel@gmail.com
"""

from m5stack import lcd
from m5ui import M5TextBox, M5Title, setScreenColor
from uiflow import wait_ms
from time import sleep_ms
import MLX90615
import statistics

MIN_TEMPERATURE_ACCEPTABLE = 3400   # (34.00 C)
MAX_TEMPERATURE_ACCEPTABLE = 4200   # (42.00 C)
TIME_MS_BETWEEN_TEMPERATURE_MEASUREMENTS = 500 # 0.5 s
NUM_TEMPERATURE_MEASUREMENTS = 8
TIME_MS_AFTER_TEMPERATURE_MEASUREMENTS = 7000   # 7 s;

""" 
Verificar o método de leituras dos sensores Tof Unit e ADC Hat, onde:
tof = unit.get(unit.TOF, unit.PORTA) e adc = hat.get(hat.ADC). Será necessário adaptar tal método.
"""



# Algoritmo uPyBodyTempIR https://gitlab.com/rcolistete/computacaofisica-privado/-/tree/master/uPyBodyTempIR#vers%C3%A3o-sem-apds-9960
print("mensagem de boas-vindas na tela com nome, versão e curta descrição do software")
flag_exit = False

while(not flag_exit):
    tObject = 0
    tAmbient = 0
    listTObject = []
    listTAmbient = []
    meanTObjecto = 0
    meanTAmbient = 0
    stadevTObjecto = 0
    stadevTAmbient = 0

    print("mensagem curta com explicação para se aproximar a testa a 3 cm do sensor, mas sem tocar, ficar parado por tantos segundos")
    measurements = 0
    while(measurements < NUM_TEMPERATURE_MEASUREMENTS and not flag_exit):
        tObject, tAmbient = MLX90615.Read_MLX90615_Temperatures()
        sleep_ms(TIME_MS_BETWEEN_TEMPERATURE_MEASUREMENTS)
        if(tObject < MAX_TEMPERATURE_ACCEPTABLE and tObject > MIN_TEMPERATURE_ACCEPTABLE):
            measurements += 1
            listTObject.append(tObject)
            listTAmbient.append(tAmbient)
            print("Medindo, fique parado")
        
        
    if(measurements == NUM_TEMPERATURE_MEASUREMENTS):
        meanTObjecto = statistics.mean(listTObject) 
        meanTAmbient = statistics.mean(listTAmbient) 
        
        stadevTObjecto = statistics.pstdev(listTObject)
        stadevTAmbient = statistics.pstdev(listTAmbient)

        #if( (max(listTObject) < meanTObjecto+0.5) and (min(listTObject) > meanTObjecto-0.5)):
        if(stadevTObjecto > 5):
            print("Tente de novo, fique parado a 3 cm")
        else:
            print("Media da temperatura = {} °C".format(meanTObjecto / 100)) # incerteza ???
            if(meanTObjecto > 3700):
                print("FEBRE - procurar o sistema de saúde")
            
            # Saida no M5StickC
            lcd.clear()
            lcd.setRotation(3)
            tempfield = M5TextBox(40, 20, "35.23", lcd.FONT_DejaVu40, 0xfee203)
            clabel = M5TextBox(54, 64, "+/- 0.5 Celsius", lcd.FONT_Default, 0xfee203)
            titlelabel = M5TextBox(0, 0, "M5StickC MLX90615", lcd.FONT_Small, 0xFFFFFF)

            tempfield.setText(str(meanTObjecto))
            clabel.setText("+/- " + str(stadevTObjecto) + " Celsius")
            print('(' + str(meanTObjecto) + " +/- " + str(stadevTObjecto) + ") Celsius")
        
        sleep_ms(TIME_MS_AFTER_TEMPERATURE_MEASUREMENTS)
        print("mensagem para se afastar do medidor, tal que a temperatura do objeto volte a ser próxima da temperatura ambiente")

ts.closeConnection()
deepsleep(30)
