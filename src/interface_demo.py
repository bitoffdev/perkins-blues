import time
from controller_proxy import Controller
from solid_animation import SolidAnimation
from fade_animation import FadeAnimation
from wipe_animation import WipeAnimation
from pong_animation import PongAnimation
from rainbow_animation import RainbowAnimation

control = Controller("localhost", 8000)

start = time.time()

control.add_animation(FadeAnimation(start + 0.5, start + 2,
        0.0, 1.0, 0x000000, 0x00ffff))

control.add_animation(FadeAnimation(start + 2, start + 4,
        0.0, 1.0, 0x00ffff, 0xff0000))

for i in range(4, 10):
    control.add_animation(WipeAnimation(start + i, start +i+1,
        0.0, 1.0, 0x000000, 0xff0000))

control.add_animation(SolidAnimation(start + 10, start + 12,
    0.0, 1.0, 0xffffff))

control.add_animation(PongAnimation(start + 12, start + 20,
        0.0, 1.0, 0xff33ff, 0x000066))

control.add_animation(FadeAnimation(start + 20, start + 22,
    0.0, 1.0, 0x000066, 0xffffff))

control.add_animation(SolidAnimation(start + 22, start + 23,
    0.0, 1.0, 0xffffff))

control.add_animation(SolidAnimation(start + 23, start + 24,
    0.0, 1.0, 0x00ff00))

control.add_animation(SolidAnimation(start + 24, start + 25,
    0.0, 1.0, 0xff0000))

control.add_animation(RainbowAnimation(start + 25, start + 28,
    0.0, 1.0, 10, 6))

control.add_animation(FadeAnimation(start + 28, start + 32,
        0.0, 1.0, 0xff0000, 0x000000))

control.add_animation(SolidAnimation(start + 32, start + 33,
    0.0, 1.0, 0x000000))
