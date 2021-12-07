import logging
import math
from copy import deepcopy

import numpy as numpy


class Submarine:
    def __init__(self):
        self._measurements = []
        self._course = []
        self._diagnostic_report = []

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

    @property
    def diagnostic_report(self):
        return self._diagnostic_report

    @diagnostic_report.setter
    def diagnostic_report(self, diagnostic_report):
        self._diagnostic_report = diagnostic_report

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

        if not self._course:
            return 0, 0

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

        if not self._course:
            return 0, 0

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

    def get_power_consumption(self):
        gamma_binary = self._parse_diagnostic_report(invert=False)
        epsilon_rate = self._invert(gamma_binary)

        return self._binary_to_int(gamma_binary) * self._binary_to_int(epsilon_rate)

    def get_life_support_rating(self):
        oxygen_generator_rating = self._parse_diagnostic_report(invert=False, exclude=True)
        co2_scrubber_rating = self._parse_diagnostic_report(invert=True, exclude=True)

        return self._binary_to_int(oxygen_generator_rating) * self._binary_to_int(co2_scrubber_rating)

    def _parse_diagnostic_report(self, invert=False, exclude=False):
        code = []
        line_length = len(self._diagnostic_report[0])
        report_length = len(self._diagnostic_report)

        for column in range(line_length):
            exclusions = []
            zeros = 0
            ones = 0
            for row in range(report_length):
                if exclude and not numpy.array_equal(code, self._diagnostic_report[row][:len(code)]):
                    exclusions.append(self._diagnostic_report[row])
                    continue
                if int(self._diagnostic_report[row][column]) == 0:
                    zeros += 1
                else:
                    ones += 1

            if exclude and len(exclusions) == report_length - 1:
                return self._diff(self._diagnostic_report, exclusions)

            if invert:
                if zeros > ones:
                    code.append(1)
                else:
                    code.append(0)
            else:
                if zeros > ones:
                    code.append(0)
                else:
                    code.append(1)

        return code

    def _diff(self, li1, li2):
        return list(set(li1) - set(li2)) + list(set(li2) - set(li1))

    def _invert(self, arr):
        ret = []

        for i in range(len(arr)):
            ret.append(1 - arr[i])

        return ret

    def _binary_to_int(self, arr):
        value = 0

        for i in range(len(arr)):
            value += math.pow(2, len(arr)-i-1) * arr[i]

        return value
