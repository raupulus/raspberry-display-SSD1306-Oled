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


#######################################
# #       Importar Librerías        # #
#######################################
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image


#######################################
# #             Variables           # #
#######################################
RST = 24  # Raspberry Pi pin configuration:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)


#######################################
# #             Funciones           # #
#######################################


def inicializar():
    disp.begin()


def limpiar():
    disp.clear()
    disp.display()


def animacion(letras):
    pass


def botones():
    pass


def imagen(ruta):
    """
    Recibe la ruta de la imagen a pintar en pantalla.
    Primero la convertirá a 1bit de color y luego la mostrará por pantalla.
    """

    # TODO → Comprobar si existe la imagen en el sistema de archivos
    existe = True

    # Si existe la imagen se muestra, en caso contrario no hace nada.
    if existe:
        image = Image.open(ruta).resize(
            (disp.width, disp.height),
            Image.ANTIALIAS).convert('1')
    else:
        return False

    # Mostrar imagen tras limpiar pantalla
    limpiar()
    disp.image(image)
    disp.display()

    return True


def shapes():
    pass


def stats():
    pass


inicializar()
limpiar()
animacion()
botones()
imagen()
shapes()
stats()
