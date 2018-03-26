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
import math
import subprocess
import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#######################################
# #             Variables           # #
#######################################
RST = 24  # Raspberry Pi pin de configuracion
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)


#######################################
# #             Funciones           # #
#######################################


def inicializar():
    disp.begin()


def limpiar():
    disp.clear()
    disp.display()


def sanear(limpiame):
    """
    Recibe algo y lo intenta transformar a string limpiando carácteres
    no deseados que pueda contener y devuelve un String limpio.
    """

    x = str(limpiame).replace('b\'', '').replace('\\n\'', '')
    x = str(x).replace('b\"', "").replace('\n\"', '')

    # Reemplazo todas las comillas dobles, simples y otras que puedan quedar
    x = str(x).replace('\'', '').replace('\"', '').replace('\'´', '')

    return x


def animacion(letras):
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


def informacion():
    # Creo constantes
    width = disp.width
    height = disp.height
    padding = -2
    top = padding
    bottom = height-padding
    x = 0  # Registra la posición actual

    # Creo una imagen vacía con un 1 bit de color
    image = Image.new('1', (width, height))

    # Creo objeto sobre el que dibujar a partir de la imagen vacía
    draw = ImageDraw.Draw(image)

    # Cargo la fuente
    font = ImageFont.load_default()
    # font = ImageFont.truetype('mifuente.ttf', 8)

    # Obtengo información del sistema
    cmd = "hostname -I | cut -d \' \' -f1"
    IP = subprocess.check_output(cmd, shell=True)

    cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
    CPU = subprocess.check_output(cmd, shell=True)

    cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'"
    RAM = subprocess.check_output(cmd, shell=True)

    cmd = "df -h | awk '$NF==\"/\"{printf \"HDD: %d/%dGB %s\", $3,$2,$5}'"
    HDD = subprocess.check_output(cmd, shell=True)

    cmd = 'vcgencmd measure_temp'
    TMP = str(subprocess.check_output(cmd, shell=True)).replace('temp=', '')
    TMP = str(TMP).replace('\'C', '')

    # Crear el dibujo renderizando el texto
    draw.text((x, top),    'IP: ' + sanear(IP),  font=font, fill=255)
    draw.text((x, top+8),  sanear(CPU), font=font, fill=255)
    draw.text((x, top+16), sanear(RAM),  font=font, fill=255)
    draw.text((x, top+24), sanear(HDD),  font=font, fill=255)
    draw.text((x, top+32), 'Temperatura: ' + sanear(TMP),  font=font, fill=255)

    # Mostrar imagen tras limpiar pantalla
    limpiar()
    disp.image(image)
    disp.display()


inicializar()
limpiar()
animacion('Prueba')
imagen('prueba.png')
informacion()
