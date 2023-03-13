#!/usr/bin/python3
# -*- encoding: utf-8 -*-

# @author     Raúl Caro Pastorino
# @copyright  Copyright © 2018 Raúl Caro Pastorino
# @license    https://wwww.gnu.org/licenses/gpl.txt
# @email      public@raupulus.dev
# @web        https://raupulus.dev
# @gitlab     https://gitlab.com/raupulus
# @github     https://github.com/raupulus
# @twitter    https://twitter.com/raupulus

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

try:
    oled = Oledssd1306.Oledssd1306()
except:
    print('No se ha podido detectar la pantalla por i2c')

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

time.sleep(10)

while True:
    try:
        oled.informacion()
    except Exception:
        print(
            'La pantalla cargó pero hay un error al pintar la información',
            Exception
        )
    time.sleep(5)
