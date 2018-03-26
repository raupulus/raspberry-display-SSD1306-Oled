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
# #            Constantes           # #
#######################################
RST = 24  # Pin de configuracion para la Raspberry Pi
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)  # Creo objeto controlador
width = disp.width    # Ancho de la pantalla
height = disp.height  # Alto de la pantalla

font = ImageFont.load_default()  # Cargo la fuente
# font = ImageFont.truetype('mifuente.ttf', 8)


#######################################
# #             Variables           # #
#######################################


#######################################
# #             Funciones           # #
#######################################


def inicializar():
    disp.begin()


def limpiar():
    disp.clear()
    disp.display()


def sanear(limpiar):
    """
    Recibe algo y lo intenta transformar a string limpiando carácteres
    no deseados que pueda contener y devuelve un String limpio.
    """

    x = str(limpiar).replace('b\'', '').replace('\\n\'', '').replace('\\n', '')
    x = str(x).replace('b\"', "").replace('\n', '').replace('\n\"', '')

    # Reemplazo todas las comillas dobles, simples y otras que puedan quedar
    x = str(x).replace('\'', '').replace('\"', '').replace('\'´', '')

    return x


def animacion(texto):
    """
    Recibe una cadena (o algo que se pueda transformar a cadena) y la muestra
    por la pantalla en forma de animación según los parámetros que pasamos a
    la función.
    """

    # Crea una nueva imagen del tamaño de la pantalla con 1 bit de color
    image = Image.new('1', (width, height))

    # Creo objeto sobre el que dibujar a partir de la imagen vacía
    draw = ImageDraw.Draw(image)

    maxwidth, unused = draw.textsize(texto, font=font)

    # Parámetros para definir el tipo de animación
    amplitude = height/4
    offset = height/2 - 4
    velocity = -2

    limpiar()

    pos = width

    while True:
        # Borra la pantalla antes de pintar.
        draw.rectangle((0,0,width,height), outline=0, fill=0)

        x = width
        for i, c in enumerate(texto):
            # Al llegar al borde de la pantalla parar.
            if x > width:
                break

            # Calcula el ancho pero no dibuja si excede el ancho de la pantalla.
            if x < -10:
                char_width, char_height = draw.textsize(c, font=font)
                x += char_width
                continue

            # Calcular el desplazamiento de la onda sinusoidal.
            y = offset+math.floor(amplitude*math.sin(x/float(width)*2.0*math.pi))

            # Pinta el texto en su lugar.
            draw.text((x, y), c, font=font, fill=255)

            # Incremente la posición x en función del ancho del carácter.
            char_width, char_height = draw.textsize(c, font=font)
            x += char_width

        # Mostrar imagen.
        disp.image(image)
        disp.display()

        # Mueve la posición para la próxima imagen.
        pos += velocity

        # Cuando el texto se desplaza completamente se termina.
        if pos < -maxwidth:
            break

        # Pauso antes de pintar el siguiente frame.
        time.sleep(0.1)


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
            (width, height),
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
    padding = -2
    top = padding
    bottom = height-padding
    x = 0  # Registra la posición actual

    # Creo una imagen vacía con un 1 bit de color
    image = Image.new('1', (width, height))

    # Creo objeto sobre el que dibujar a partir de la imagen vacía
    draw = ImageDraw.Draw(image)

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
    draw.text(
        (x, top+32),
        'Temperatura: ' + sanear(TMP) + 'ºC',
        font=font, fill=255
    )

    # Mostrar imagen tras limpiar pantalla
    limpiar()
    disp.image(image)
    disp.display()


inicializar()
limpiar()
animacion('Prueba')
#imagen('prueba.png')
#informacion()
