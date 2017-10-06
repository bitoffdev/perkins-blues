import pprint
import sys

import spotipy
import spotipy.util as util

import time

from neopixel import *

import lights

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

class BeatLight(object):
    def __init__(self):
	# Create NeoPixel object with appropriate configuration.
	self.strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ,
                LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	# Intialize the library (must be called once before other functions).
	self.strip.begin()

        self.colors = [Color(127,0,0), Color(0,127,0), Color(0,0,127)]
        self.i = 0

    def beat(self):
        for led in range( self.strip.numPixels() ):
            self.strip.setPixelColor(led, self.colors[self.i])
        self.strip.show()
        self.i += 1
        if self.i >= len(self.colors): self.i = 0



# if len(sys.argv) > 1:
#     username = sys.argv[1]
# else:
#     print "Usage: %s username ..." % (sys.argv[0],)
#     sys.exit()

username = "elliospizzaman"

scope = 'user-read-playback-state user-read-currently-playing'
token = util.prompt_for_user_token(username, scope,
    client_id='95acf39e73ce4425ac9743edb89ab9be',
    client_secret='71a013e9ee0d481887baa8e8f95bc6a9',
    redirect_uri='http://localhost/callback')

if not token:
    print "Can't get token for", username
    raise SystemExit

sp = spotipy.Spotify(auth=token)

playing = sp._get("https://api.spotify.com/v1/me/player/currently-playing")
playing_id = playing["item"]["id"]
playing_start = playing["timestamp"] # milliseconds since start
playing_progress = playing["progress_ms"]
playing_name = playing["item"]["name"]

analysis = sp.audio_analysis(playing_id)
beats = analysis["beats"]

# print playing_name
# print analysis["beats"]

progress = playing_progress
beat_index = 0

print "====="

cols = ["#cc0000", "#00cc00", "#770077", "#0000cc", "#995511", "#007733"]
coli = 0
light = lights.BeatLight()

while True:
    progress = time.time() - playing_start * 0.001

    if beat_index >= len(beats):
        break

    if progress > beats[beat_index]["start"]:
        # Our beat index is lagging behind
        beat_index += 1
        continue

    if progress >= beats[beat_index]["start"] - beats[beat_index]["duration"] * 0.3:
        # The beat index is right on
        if coli %2 == 0:
            light.set_hex(cols[coli], beats[beat_index]["duration"] * 0.4, 0, 28)
        else:
            light.set_hex(cols[coli], beats[beat_index]["duration"] * 0.4, 28, None)
        coli = (coli + 1) % len(cols)
        beat_index += 1
    else:
        time.sleep(beats[beat_index]["duration"] * 0.2)
