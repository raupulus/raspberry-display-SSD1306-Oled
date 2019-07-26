#!/usr/bin/python3
# -*- encoding: utf-8 -*-

# @author     Raúl Caro Pastorino
# @copyright  Copyright © 2018 Raúl Caro Pastorino
# @license    https://wwww.gnu.org/licenses/gpl.txt
# @email      tecnico@fryntiz.es
# @web        www.fryntiz.es
# @github     https://github.com/fryntiz
# @gitlab     https://gitlab.com/fryntiz
# @twitter    https://twitter.com/fryntiz

# Guía de estilos aplicada: PEP8

#######################################
# #           Descripción           # #
#######################################
# Script con ejemplos para ver el funcionamiento de la pantalla

#######################################
# #       Importar Librerías        # #
#######################################
import Oledssd1306
import time

oled = Oledssd1306.Oledssd1306

oled.animacion('Esto es un texto de pruebas')
time.sleep(2)

oled.pintarLineas([
    'Linea 1',
    'Linea 2',
    'Linea 3',
    'Linea 4',
    'Linea 5',
    'Linea 6',
    'Linea 7',
])

while True:
    oled.informacion()
    time.sleep(5)
