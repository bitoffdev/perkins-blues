from abc import ABC, abstractmethod #, abstract_attribute

class Animation(ABC):

#     __start_time = abstract_attribute()
#     __stop_time = abstract_attribute()
#     __start_pos = abstract_attribute()
#     __stop_pos = abstract_attribute()

    @abstractmethod
    def get_color(self, time, pos):
        """
        get the color of the animation at a given time and 0-1 location on the
        strip

        :param time: seconds since the epoch
        :type time: float
        :param pos: location on strip between 0 and 1
        :type pos: float
        :return: unsigned 32-bit value defining RGB
        :rtype: int
        """
        return 0x000000
    
    def get_start_time(self):
        return self.__start_time

    def set_start_time(self, time):
        self.__start_time = time

    def get_stop_time(self):
        return self.__stop_time

    def set_stop_time(self, time):
        self.__stop_time = time

    def get_start_pos(self):
        return self.__start_pos

    def set_start_pos(self, pos):
        self.__start_pos = pos

    def get_stop_pos(self):
        return self.__stop_pos

    def set_stop_pos(self, pos):
        self.__stop_pos = pos
