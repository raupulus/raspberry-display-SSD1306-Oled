#!/usr/bin/python3
# -*- encoding: utf-8 -*-

# @author     Raúl Caro Pastorino
# @copyright  Copyright © 2019 Raúl Caro Pastorino
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
# Este script muestra información sobre el estado de la raspberry como
# temperatura, ip, porcentaje de cpu en uso, memoria y disco duro.

#######################################
# #       Importar Librerías        # #
#######################################
import Oledssd1306
import time

try:
    oled = Oledssd1306.Oledssd1306()
except:
    print('No se ha podido detectar la pantalla por i2c')
    exit(1)

while True:
    try:
        oled.informacion()
    except Exception:
        print(
            'La pantalla cargó pero hay un error al pintar la información',
            Exception
        )

        exit(1)
    time.sleep(5)
