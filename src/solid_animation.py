import animation

class SolidAnimation(animation.Animation):
    """
    animation keeps relevant section of light strip solid for the duration of
    the animation
    """

    def __init__(self, start_time, stop_time, start_pos, stop_pos, color):
        """
        :param start_time: seconds since the epoch to start animation
        :param stop_time: seconds since the epoch to stop animation
        :param start_pos: number from 0 to 1 indicating start on strip
        :param stop_pos: number from 0 to 1 indicating stop on strip
        :param color: 24-bit integer RGB color
        """
        self.set_start_time(start_time)
        self.set_stop_time(stop_time)
        self.set_start_pos(start_pos)
        self.set_stop_pos(stop_pos)
        self.__color = color

    def get_color(self, time, pos):
        """
        :param time: current time as seconds since the epoch
        :param pos: position from 0 to 1 to get color for
        :return: 24-bit integer RGB color
        """
        return self.__color

if __name__ == "__main__":
    import sys
    sys.stderr.write("Do not call this script!\n")
