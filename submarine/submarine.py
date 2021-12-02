import logging


class Submarine:
    def __init__(self):
        self._measurements = []
        self._course = []

    @property
    def measurements(self):
        return self._measurements

    @measurements.setter
    def measurements(self, measurements):
        self._measurements = measurements

    @property
    def course(self):
        return self._course

    @course.setter
    def course(self, course):
        self._course = course

    def get_increases(self):
        increases = 0

        if not self._measurements:
            return increases

        for i in range(len(self._measurements)):
            if i == 0:
                continue
            if int(self._measurements[i]) > int(self._measurements[i-1]):
                increases += 1

        return increases

    def get_window_increases(self):
        increases = 0

        if not self._measurements:
            return increases

        for i in range(len(self._measurements)-2):
            if i == 0:
                continue

            cur_window = sum(self._measurements[i:i + 3])
            prev_window = sum(self._measurements[i-1:i+2])

            if cur_window > prev_window:
                increases += 1

        return increases

    def navigate(self):
        depth = 0
        horizontal = 0

        for (direction, distance) in self._course:
            if direction == 'forward':
                horizontal += int(distance)
            elif direction == 'down':
                depth += int(distance)
            elif direction == 'up':
                depth -= int(distance)
            else:
                logging.warning("unknown direction: " + direction)

        return depth, horizontal

    def navigate_corrected(self):
        depth = 0
        horizontal = 0
        aim = 0

        for (direction, distance) in self._course:
            if direction == 'forward':
                horizontal += int(distance)
                depth += aim * int(distance)
            elif direction == 'down':
                aim += int(distance)
            elif direction == 'up':
                aim -= int(distance)
            else:
                logging.warning("unknown direction: " + direction)

        return depth, horizontal
