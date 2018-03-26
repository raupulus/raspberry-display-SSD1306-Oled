# Librería Display-Oled-SSD1306

Librería para trabajar con pantallas Oled de 128x64 píxeles que tengan el controlador SSD 1306 instalando y usando las librerías: Adafruit_SSD1306, Adafruit_GPIO, Pillow y RPIO para python3

## Objetivos

Preparar el sistema y facilitar el manejo del chip SSD1306 para que pueda usarse de forma modular en otros programas:
-   Instalarán libreras para python3 **Adafruit_SSD1306, Adafruit_GPIO, Pillow y RPi**

## Requisitos

Se necesitan las siguientes herramientas (pero no se limita a ellas):

-   Raspbian stable
-   Python 3.5 o superior (otras versiones de python3 podrían funcionar)
-   Gestor de paquetes pip instalado para python3
-   Raspberry PI
-   Pantalla Oled de 0,96 pulgadas, con 128x64 píxeles y el controladorr SSD 1306
-   I2C Habilitado
-   4 cables conectados a 3.3v, GND, SDA1I2c y SCL1I2C

## Obtener este Repositorio

Para poder clonar el repositorio en su dispositivo Raspberry PI necesita tener
git instalado en el equipo, eso se hace con:

```bash
    sudo apt install git
```

También es posible descargar directamente el zip desde la interfaz web.

Para  clonar este repositorio una vez disponemos de **git** en el sistema:

```bash
    git clone https://github.com/fryntiz/Display-Oled-SSD1306.git $HOME/Display-Oled-SSD1306
```

Este comando dejará en el directorio personal del usuario que lo ejecute la librería descargada, ya solo tenemos que acceder a ella y ejecutarla.

## Instalador automático

En el repositorio se incluye el script **instalador.sh** el cual dejará en un
sistema **Raspbian** configurado e instalado correctamente python y todas las
dependencias necesarias.

Para ejecutarlo entramos al directorio y escribimos:

```bash
    ./instalador.sh
```

Si prefieres hacerlo manualmente continúa con los pasos manuales.

## Instalar Dependencias Manualmente

A continuación se describe como instalar las
dependencias.

Instalamos Git para poder clonar repositorio y además instalamos el gestor de paquetes pip y la librería de acceso a GPIO para python3

```bash
  sudo apt install git python3-rpi.gpio python3-pip
```

Ahora instalamos los paquetes para controlar la pantalla y manipular imágenes:

```bash
  pip3 install Adafruit_SSD1306 Adafruit_GPIO Pillow RPi
```

## Librerías originales utilizadas

Se utiliza librería de acceso original y directamente de adafruit adaptada para esta resolución en concreto, obtenida desde:
<https://github.com/adafruit/Adafruit_Python_SSD1306>

Además, si necesitas la librería en C puedes acceder desde aquí:
<https://github.com/adafruit/Adafruit_SSD1306>
