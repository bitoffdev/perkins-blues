import sys, time
from neopixel import *

# LED strip configuration:
LED_COUNT      = 55      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering


class Light(object):

    def __init__(self):
        # Create NeoPixel object with appropriate configuration.
        self.strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ,
                LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
        # Intialize the library (must be called once before other functions).
        self.strip.begin()
        # self.reset()

    def length(self, val):
        if val[-1] == '%':
            val = val[:-1]
            val = int(int(val)/100 * self.strip.numPixels())
        return val

    def reset(self):
        col = Color(0,0,0)
        for led in range( self.strip.numPixels() ):
            self.strip.setPixelColor(led, col)
        self.strip.show()

    def set_hex(self, l0, l1, code):
        l0 = self.length(l0)
        l1 = self.length(l1)

        [r1,g1,b1] = hexTo256(code)

        for led in range (l0, l1):
            self.strip.setPixelColor(led, Color(r1, g1, b1))
        self.strip.show()

    def fade(self, l0, l1, code, ms):
        l0 = self.length(l0)
        l1 = self.length(l1)

        [r1,g1,b1] = hexTo256(code)
        col0 = self.strip.getPixelColor(l0)
        r0 = (col0 >> 16) % 256
        g0 = (col0 >> 8) % 256
        b0 = (col0 % 256)

        start = time.time()
        while True:
            completion = min((time.time() - start) / (float(ms)/1000), 1.)
            c3 = completion #  ** 3
            lerp = Color(int(r0+(r1-r0)*c3), int(g0+(g1-g0)*c3), int(b0+(b1-b0)*c3))
            for led in range( l0, l1 ):
                self.strip.setPixelColor(led, lerp)
            self.strip.show()
            if completion >= 1: return


def hexTo256(code):

    h = "0123456789abcdef"
    code = code.lstrip("#").lower()
    colorArray = []

    print(code)
    if len(code) == 3:
        colorArray.append( h.index(code[0]) * 16 )
        colorArray.append( h.index(code[1]) * 16 )
        colorArray.append( h.index(code[2]) * 16 )

    elif len(code) == 6:
        colorArray.append( h.index(code[0]) * h.index(code[1]) )
        colorArray.append( h.index(code[2]) * h.index(code[3]) )
        colorArray.append( h.index(code[4]) * h.index(code[5]) )

    else:
        raise Exception("Invalid hex!")

    return colorArray


if __name__=="__main__":
    if len(sys.argv) < 2:
        raise SystemExit
    l = BeatLight()
    l.reset()
    for arg in sys.argv[1:]:
        l.set_hex(arg)
