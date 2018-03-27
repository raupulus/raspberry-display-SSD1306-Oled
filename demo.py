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
import oled128x64 as OLED
import time

OLED.animacion('Esto es un texto de pruebas')
time.sleep(5)
OLED.informacion()
time.sleep(5)
