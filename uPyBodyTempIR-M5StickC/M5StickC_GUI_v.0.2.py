"""
MicroPython for M5StickC - GUI via Brockly + MicroPython
Version: 0.2
Author: Thiago Ferreira Santos
E-mail: thiago_fisica@outlook.com
"""

from m5stack import lcd
from m5ui import M5TextBox, M5Title, setScreenColor
from uiflow import wait_ms
import time
import mlx90615

lcd.clear()
lcd.setRotation(3)
tempfield = M5TextBox(40, 20, "0", lcd.FONT_DejaVu40, 0xfee203)
clabel = M5TextBox(54, 64, "+/- 0.5 Celsius", lcd.FONT_Default, 0xfee203)
titlelabel = M5TextBox(0, 0, "M5StickC MLX90615", lcd.FONT_Small, 0xFFFFFF)


mlx90615 = MLX90615.Read_MLX90615_Temperatures()

while True:
    tempfield.setText(str(mlx90615.temperature))
    delta_mlx90615 = (mlx90615.temperature/100)
    clabel.setText("+/- " + str(delta_mlx90615) + " C")
    print('(' + str(mlx90615.temperature) + " +/- " + str(delta_mlx90615) + ") C")
    wait_ms(60)
