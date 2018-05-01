import animation, colorsys

def colorunpack(color):
    color = int(color)
    return ((color >> 16) / 255,
            ((color >> 8) & 255) / 0xff,
            (color & 0xff) / 0xff)
def colorpack(color):
    return sum(int(color[i] * 0xff) << (16 - 8*i) for i in range(3))

class RainbowAnimation(animation.Animation):
    """
    animation fades relevant section of light strip solid between two colors
    for the duration of the animation
    """

    def __init__(self, start_time, stop_time, start_pos, stop_pos, \
            frequency, waves):
        """
        :param start_time: seconds since the epoch to start animation
        :param stop_time: seconds since the epoch to stop animation
        :param start_pos: number from 0 to 1 indicating start on strip
        :param stop_pos: number from 0 to 1 indicating stop on strip
        :param start_color: initial 24-bit integer RGB color
        :param stop_color: final 24-bit integer RGB color
        """
        self.set_start_time(start_time)
        self.set_stop_time(stop_time)
        self.set_start_pos(start_pos)
        self.set_stop_pos(stop_pos)

        self.__period = 1 / frequency
        self.__waves = waves

    def get_color(self, time, pos):
        """
        :param time: current time as seconds since the epoch
        :param pos: position from 0 to 1 to get color for
        :return: 24-bit integer RGB color
        """
        lerp = ((time - self.get_start_time()) / self.__period + pos) \
                * self.__waves % 1

        return colorpack(colorsys.hsv_to_rgb(lerp, 1, 1))

if __name__ == "__main__":
    import sys
    sys.stderr.write("Do not call this script!\n")