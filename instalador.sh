#!/usr/bin/env bash
# -*- ENCODING: UTF-8 -*-
##
## @author     Raúl Caro Pastorino
## @copyright  Copyright © 2018 Raúl Caro Pastorino
## @license    https://wwww.gnu.org/licenses/gpl.txt
## @email      tecnico@raupulus.dev
## @web        raupulus.dev
## @github     https://github.com/raupulus
## @gitlab     https://gitlab.com/raupulus
## @twitter    https://twitter.com/raupulus
##
##             Guía de estilos aplicada:
## @style      https://github.com/raupulus/Bash_Style_Guide

############################
##     INSTRUCCIONES      ##
############################
## Este script tiene como objetivo preparar el sistema operativo instalando
## python y todas sus dependencias.
##
## Una vez instalado pyhton instalará mediante pip las librerías necesarias
## para usar la pantalla Oled de 128x64 píxeles con el chip SSD1306.

############################
##       CONSTANTES       ##
############################
AM="\033[1;33m"  ## Color Amarillo
RO="\033[1;31m"  ## Color Rojo
VE="\033[1;32m"  ## Color Verde
CL="\e[0m"       ## Limpiar colores

VERSION="0.0.1"
WORKSCRIPT=$PWD  ## Directorio principal del script
USER=$(whoami)   ## Usuario que ejecuta el script

############################
##       FUNCIONES        ##
############################
##
## Pinta la versión e información del script
##
version() {
    echo -e "$RO Versión$AM $VERSION$RO del instalador$CL"
    echo -e "$RO Ruta de trabajo:$CL"
    echo -e "$AM $WORKSCRIPT$CL"
}

##
## Instala Python
##
instalarPython() {
    echo -e "$VE Instalando versiones de python$CL"
    sudo apt install python3
    sudo apt install python
}

##
## Instala las dependencias para python
##
dependencias() {
    echo -e "$VE Instalando dependencias para$RO Raspbian$CL"
    sudo apt install git python3-pip python3-rpi.gpio -y
    sudo apt install git python-pip python-rpi.gpio -y
}

##
## Instala las librerías necesarias para trabajar con la pantalla oled
##
librerias() {
    echo -e "$VE Instalando librerías de python mediante$RO pip$CL"
    sudo pip3 install Adafruit_SSD1306 Adafruit_GPIO Pillow RPi
    sudo pip install Adafruit_SSD1306 Adafruit_GPIO Pillow RPi
}

############################
##       EJECUCIÓN        ##
############################
version
instalarPython
dependencias
librerias

exit 0
