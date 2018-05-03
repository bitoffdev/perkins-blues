import animation, colorsys

class SplashAnimation(animation.Animation):
    """
    Does a drip like animation from an epoch point to reach a new color
    """

    def __init__(self, start_time, stop_time, start_pos, stop_pos, epoch_pos, start_color, stop_color):
        """
        :param start_time: seconds since the epoch to start animation
        :param stop_time: seconds since the epoch to stop animation
        :param start_pos: number from 0 to 1 indicating start on strip
        :param epoch_pos: where the splash will start from
        :param stop_pos: number from 0 to 1 indicating stop on strip
        :param start_color: initial 24-bit integer RGB color
        :param stop_color: final 24-bit integer RGB color
        """
        self.set_start_time(start_time)
        self.set_stop_time(stop_time)
        self.set_start_pos(start_pos)
        self.set_stop_pos(stop_pos)
        
    def get_color(self, time, pos):
        """
        :param time: current time as seconds since the epoch
        :param pos: position from 0 to 1 to get color for
        :return: 24-bit integer RGB color
        """
        lerp = (time - self.get_start_time()) \
                / (self.get_stop_time() - self.get_start_time())
        lerp = max(0, min(1, lerp))
        weight = ( abs(pos - epoch_pos)) ** (lerp * 3) 
        if (weight > .1):
            return start_color
        else:
            return stop_color

if __name__ == "__main__":
    import sys
    sys.stderr.write("Do not call this script!\n")
