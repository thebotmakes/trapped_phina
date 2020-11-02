# HalloWing Trapped Phina

import time
import array
import math
import board
import displayio
import analogio
import audiocore
import pulseio
import digitalio
import touchio
import audioio
import neopixel

# Setup LED and PIR pins
LED_PIN = board.D13  # Pin number for the board's built in LED.
LIGHT_SENS = board.A7

speaker_enable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speaker_enable.switch_to_output(value=True)
a = audioio.AudioOut(board.A0)

pixel_pin = board.D8
num_pixels = 4
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)
white = (255,255,255)
off = (0,0,0)

pin = analogio.AnalogIn(LIGHT_SENS)
print(pin.value)

# Setup digital output for LED:
led = digitalio.DigitalInOut(LED_PIN)
led.direction = digitalio.Direction.OUTPUT

wavlist = ["mummy.wav","help_me.wav","trapped.wav",
            "mummy2.wav","bulba.wav"]

# Function for playing wav file, releasing servo
def play_wave(wavname):


    data = open(wavname, "rb")
    wav = audiocore.WaveFile(data)


    print("playing")
    a.play(wav)
    while a.playing:
        pass
    print("stopped")


def lightning():
    x = 0
    while x < 3:
        pixels.fill(white)
        pixels.show()
        time.sleep(0.1)
        pixels.fill(off)
        pixels.show()
        time.sleep(0.1)
        x += 1

# display setup
splash = displayio.Group()
board.DISPLAY.show(splash)
max_brightness = 2 ** 15

# Image list
images = ["left.bmp", "right.bmp","blur.bmp",
          "mid_tongue.bmp","mid_cheeky.bmp",
          "mid_open.bmp"]

# Function for displaying images on HalloWing TFT screen
def show_image(filename):
    image_file = open(filename, "rb")
    odb = displayio.OnDiskBitmap(image_file)
    face = displayio.TileGrid(odb, pixel_shader=displayio.ColorConverter())
    splash.append(face)
    # Wait for the image to load.
    board.DISPLAY.refresh(target_frames_per_second=60)

while True:

    print(pin.value)
    if pin.value < 1000:  # light sensor is in dark
        play_wave(wavlist[0])
        time.sleep(2)
        play_wave(wavlist[1])
        time.sleep(2)
    else:
        lightning()
        show_image(images[0])
        splash.pop()
        show_image(images[2])
        splash.pop()
        show_image(images[1])
        splash.pop()
        play_wave(wavlist[2])
        lightning()
        show_image(images[3])
        splash.pop()
        show_image(images[0])
        splash.pop()
        show_image(images[4])
        splash.pop()
        lightning()
        play_wave(wavlist[3])
        show_image(images[1])
        splash.pop()
        show_image(images[5])
        splash.pop()
        play_wave(wavlist[4])