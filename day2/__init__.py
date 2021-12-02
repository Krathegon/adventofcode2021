from submarine.submarine import Submarine
from helper.filereader import Filereader


def task1(input):
    submarine = Submarine()
    submarine.course = list(map(str.split, input))

    (depth, horizontal) = submarine.navigate()

    print("solution task 1: " + str(depth * horizontal))


def task2(input):
    submarine = Submarine()
    submarine.course = list(map(str.split, input))

    (depth, horizontal) = submarine.navigate_corrected()

    print("solution task 2: " + str(depth * horizontal))


if __name__ == '__main__':
    filereader = Filereader('input.txt')
    file_content = filereader.get_content()
    filereader.close()

    task1(file_content)
    task2(file_content)

