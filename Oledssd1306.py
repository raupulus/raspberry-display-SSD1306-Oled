#!/usr/bin/python3
# -*- encoding: utf-8 -*-

# @author     Raúl Caro Pastorino
# @copyright  Copyright © 2018 Raúl Caro Pastorino
# @license    https://wwww.gnu.org/licenses/gpl.txt
# @email      dev@fryntiz.es
# @web        https://fryntiz.es
# @gitlab     https://gitlab.com/fryntiz
# @github     https://github.com/fryntiz
# @twitter    https://twitter.com/fryntiz

# Guía de estilos aplicada: PEP8

#######################################
# #           Descripción           # #
#######################################
# Script de acceso a la librería para la pantalla oled de 128x64 píxeles
# con el controlador SSD1306 facilitando el acceso y el uso al proporcionar
# funciones que nos permitirá trabajar con solo ordenar que quieres ver.
#
# Funciones disponibles:
# animacion() → Recibe el texto para mostrarlo en forma de animación. Puede
#               recibir como parámetros (texto, amplitude, offset, velocity).
# imagen() → Recibe la ruta hacia la imagen que será mostrada.
# informacion() → Muestra información sobre el estado de la raspberry.

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

#######################################
# #             Funciones           # #
#######################################

class Oledssd1306:
    RST = 24  # Pin de configuracion para la Raspberry Pi

    # Creo objeto controlador
    DISPLAY = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
    WIDTH = DISPLAY.width  # Ancho de la pantalla
    HEIGHT = DISPLAY.height  # Alto de la pantalla
    FONT = ImageFont.load_default()  # Cargo la fuente
    #FONT = ImageFont.truetype('mifuente.ttf', 8)

    def __init__(self, RST=24):
        """
        Inicializa la pantalla para comenzar a trabajar
        """
        self.RST = RST

        self.DISPLAY.begin()

    def limpiar(self):
        """
        Limpia la pantalla borrando su contenido
        """
        self.DISPLAY.clear()
        self.DISPLAY.display()

    def sanear(self, limpiar):
        """
        Recibe algo y lo intenta transformar a string limpiando carácteres
        no deseados que pueda contener y devuelve un String limpio.
        """

        x = str(limpiar).replace('b\'', '').replace('\\n\'', '').replace('\\n', '')
        x = str(x).replace('b\"', "").replace('\n', '').replace('\n\"', '')

        # Reemplazo todas las comillas dobles, simples y otras que puedan quedar
        x = str(x).replace('\'', '').replace('\"', '').replace('\'´', '')

        return x

    def animacion(self, texto, amplitude=HEIGHT/4, offset=HEIGHT/2 - 4,
                  velocity=-2):
        """
        Recibe una cadena (o algo que se pueda transformar a cadena) y la muestra
        por la pantalla en forma de animación según los parámetros que pasamos a
        la función.
        """
        width = self.WIDTH
        height = self.HEIGHT
        font = self.FONT

        # Crea una nueva imagen del tamaño de la pantalla con 1 bit de color
        image = Image.new('1', (width, height))

        # Creo objeto sobre el que dibujar a partir de la imagen vacía
        draw = ImageDraw.Draw(image)

        maxwidth, unused = draw.textsize(texto, font=font)

        self.limpiar()

        pos = width

        while True:
            # Borra la pantalla antes de pintar.
            draw.rectangle((0, 0, width, height), outline=0, fill=0)

            x = pos
            for i, c in enumerate(texto):
                # Al llegar al borde de la pantalla parar.
                if x > width:
                    break

                # Calcula el ancho pero no dibuja si excede el ancho de la pantalla
                if x < -10:
                    char_width, char_height = draw.textsize(c, font=font)
                    x += char_width
                    continue

                # Calcular el desplazamiento de la onda sinusoidal.
                y = offset+math.floor(
                    amplitude*math.sin(x/float(width)*2.0*math.pi)
                )

                # Pinta el texto en su lugar.
                draw.text((x, y), c, font=font, fill=255)

                # Incremente la posición x en función del ancho del carácter.
                char_width, char_height = draw.textsize(c, font=font)
                x += char_width

            # Mostrar imagen.
            self.DISPLAY.image(image)
            self.DISPLAY.display()

            # Mueve la posición para la próxima imagen.
            pos += velocity

            # Cuando el texto se desplaza completamente se termina.
            if pos < -maxwidth:
                break

            # Pauso antes de pintar el siguiente frame.
            time.sleep(0.1)

    def imagen(self, ruta):
        """
        Recibe la ruta de la imagen a pintar en pantalla.
        Primero la convertirá a 1bit de color y luego la mostrará por pantalla.
        """

        try:
            image = Image.open(ruta).resize(
                (self.WIDTH, self.HEIGHT),
                Image.ANTIALIAS).convert('1')
        except Exception:
            return False

        # Mostrar imagen tras limpiar pantalla
        self.limpiar()
        self.DISPLAY.image(image)
        self.display()

        return True

    def informacion(self):
        width = self.WIDTH
        height = self.HEIGHT
        sanear = self.sanear
        font = self.FONT

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
        self.limpiar()
        self.DISPLAY.image(image)
        self.DISPLAY.display()

    def pintarLineas(self, array7):
        width = self.WIDTH
        height = self.HEIGHT
        sanear = self.sanear
        font = self.FONT

        # Creo constantes
        padding = -2
        bottom = height - padding


        # Creo una imagen vacía con un 1 bit de color
        image = Image.new('1', (width, height))

        # Creo objeto sobre el que dibujar a partir de la imagen vacía
        draw = ImageDraw.Draw(image)

        top = 0
        left = 0
        for linea in array7:
            draw.text((left, top), sanear(linea), font=font, fill=255)
            top += 8

        # Mostrar imagen tras limpiar pantalla
        self.limpiar()
        self.DISPLAY.image(image)
        self.DISPLAY.display()
