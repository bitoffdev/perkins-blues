# Example of low-level Python wrapper for rpi_ws281x library.
# Author: Tony DiCola (tony@tonydicola.com), Jeremy Garff (jer@jers.net)
#
# This is an example of how to use the SWIG-generated _rpi_ws281x module.
# You probably don't want to use this unless you are building your own library,
# because the SWIG generated module is clunky and verbose.  Instead look at the
# high level Python port of Adafruit's NeoPixel Arduino library in strandtest.py.
#
# This code will animate a number of WS281x LEDs displaying rainbow colors.
import os, sys, time
import _rpi_ws281x as ws
from threading import Lock

# checks
assert os.access("/dev/mem", os.W_OK)
assert sys.version_info >= (3,0)

# LED configuration.
LED_CHANNEL    = 0
LED_COUNT      = 68         # How many LEDs to light.
LED_FREQ_HZ    = 800000     # Frequency of the LED signal.  Should be 800khz or 400khz.
LED_DMA_NUM    = 10         # DMA channel to use, can be 0-14.
LED_GPIO       = 18         # GPIO connected to the LED signal line.  Must support PWM!
LED_BRIGHTNESS = 255        # Set to 0 for darkest and 255 for brightest
LED_INVERT     = 0          # Set to 1 to invert the LED signal, good if using NPN
                            # transistor as a 3.3V->5V level converter.  Keep
                            # at 0 for a normal/non-inverted signal.

# Options: ws.WS2811_STRIP_RGB, ws.SK6812_STRIP_RGBW, ws.SK6812W_STRIP
LED_STRIP      = ws.WS2811_STRIP_BRG # 2811 is the 12v strip

class Controller:
    """
    .. note:: animations are placed into 1 second buckets based on start time
    """

    def __init__(self):
        self.__animations = {}
        # active is a list of the animations that are currently running
        self.__active = []
        self.__lock = Lock()


    def add_animation(self, _animation):
        bucket_index = int(_animation.get_start_time())
        if not bucket_index in self.__animations:
            self.__animations[bucket_index] = []
        self.__animations[bucket_index].append(_animation)
        print("Animations:", self.__animations)

    def get_animations(self, time):
        result = []
        t = int(time)
        if t in self.__animations:
            result = self.__animations.pop(t)
            print("Animations:", self.__animations)
        return result

    def spin_once(self, leds, ws, channel):
        self.__lock.acquire()
        now = time.time()

        # Add animations
        self.__active.extend(self.get_animations(now))

        # Call each active animation
        i = 0
        while i < len(self.__active):
            a = self.__active[i]
            if a.get_stop_time() < time.time():
                self.__active.pop(i)
            else:
                for i in range(int(a.get_start_pos()*LED_COUNT),
                        int(a.get_stop_pos()*LED_COUNT)):
                    col = a.get_color(now, i * 1. / LED_COUNT)
                    ws.ws2811_led_set(channel, i, col)
                i += 1

        # Send the LED color data to the hardware.
        resp = ws.ws2811_render(leds)
        if resp != ws.WS2811_SUCCESS:
            message = ws.ws2811_get_return_t_str(resp)
            raise RuntimeError('ws2811_render failed with code {0} ({1})' \
                    .format(resp, message))
        self.__lock.release()

    def spin(self):
        """
        loop forever
        """
        # Create a ws2811_t structure from the LED configuration.
        # Note that this structure will be created on the heap so you need to be careful
        # that you delete its memory by calling delete_ws2811_t when it's not needed.
        leds = ws.new_ws2811_t()

        # Initialize all channels to off
        for channum in range(2):
            channel = ws.ws2811_channel_get(leds, channum)
            ws.ws2811_channel_t_count_set(channel, 0)
            ws.ws2811_channel_t_gpionum_set(channel, 0)
            ws.ws2811_channel_t_invert_set(channel, 0)
            ws.ws2811_channel_t_brightness_set(channel, 0)

        channel = ws.ws2811_channel_get(leds, LED_CHANNEL)
        
        ws.ws2811_channel_t_count_set(channel, LED_COUNT)
        ws.ws2811_channel_t_gpionum_set(channel, LED_GPIO)
        ws.ws2811_channel_t_invert_set(channel, LED_INVERT)
        ws.ws2811_channel_t_brightness_set(channel, LED_BRIGHTNESS)
        ws.ws2811_channel_t_strip_type_set(channel, LED_STRIP)
        
        ws.ws2811_t_freq_set(leds, LED_FREQ_HZ)
        ws.ws2811_t_dmanum_set(leds, LED_DMA_NUM)
        
        # Initialize library with LED configuration.
        resp = ws.ws2811_init(leds)
        if resp != ws.WS2811_SUCCESS:
            message = ws.ws2811_get_return_t_str(resp)
            raise RuntimeError('ws2811_init failed with code {0} ({1})' \
                    .format(resp, message))
        
        # Wrap following code in a try/finally to ensure cleanup functions are called
        # after library is initialized.
        try:
            while True:
                self.spin_once(leds, ws, channel)
                # Delay for a small period of time.
                time.sleep(0.05)
        
        finally:
            print("We got out")
            # Ensure ws2811_fini is called before the program quits.
            ws.ws2811_fini(leds)
            # clean up structure memory
            ws.delete_ws2811_t(leds)

