import sys, time
from controller_proxy import Controller
from solid_animation import SolidAnimation
from fade_animation import FadeAnimation
from wipe_animation import WipeAnimation
from pong_animation import PongAnimation

control = Controller(sys.argv[1], int(sys.argv[2]))

start = time.time()

control.add_animation(PongAnimation(start + 1, start + 6,
    0.0, 1.0, 0xff0000, 0x000000, size=0.01))

control.add_animation(FadeAnimation(start + 6, start + 9,
        0.0, 0.5, 0x00ff00, 0x0000ff))

control.add_animation(FadeAnimation(start + 9, start + 12,
        0.0, 0.5, 0xff0000, 0x00ffff))

control.add_animation(FadeAnimation(start + 6, start + 12,
        0.5, 1.0, 0xff0000, 0x00ffff))
