from day1.submarine import Submarine
from helper.filereader import Filereader


def task1(input):
    submarine = Submarine()
    submarine.measurements = input

    print(submarine.get_increases())


def task2(input):
    submarine = Submarine()
    submarine.measurements = input

    print(submarine.get_window_increases())


if __name__ == '__main__':
    filereader = Filereader('input.txt')
    file_content = filereader.get_content()
    filereader.close()

    int_input = list(map(int, file_content))

    task1(int_input)
    task2(int_input)

