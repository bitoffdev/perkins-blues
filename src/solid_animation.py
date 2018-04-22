import animation

class SolidAnimation(animation.Animation):

    def __init__(self, start_time, stop_time, start_pos, stop_pos, color):
        self.set_start_time(start_time)
        self.set_stop_time(stop_time)
        self.set_start_pos(start_pos)
        self.set_stop_pos(stop_pos)
        
        self.__color = color

    def get_color(self, time, pos):
        return self.__color
