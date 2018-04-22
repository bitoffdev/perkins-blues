import animation, math

class PongAnimation(animation.Animation):
    """
    animation fades relevant section of light strip solid between two colors
    for the duration of the animation
    """

    def __init__(self, start_time, stop_time, start_pos, stop_pos, color1, color2):
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
        
        self.__color1 = color1
        self.__color2 = color2

    def get_color(self, time, pos):
        """
        :param time: current time as seconds since the epoch
        :param pos: position from 0 to 1 to get color for
        :return: 24-bit integer RGB color
        """
        lerp = (time % 2) - 1
        if lerp < 0:
            lerp = -lerp
        # lerp = (math.sin(time) + 1) / 2
        if lerp - 0.1 < pos < lerp + 0.1:
            return self.__color1
        return self.__color2
