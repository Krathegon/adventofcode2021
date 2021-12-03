from submarine.submarine import Submarine
from helper.filereader import Filereader


def task1(submarine):
    consumption = submarine.get_power_consumption()

    print("solution task 1: " + str(consumption))


def task2(submarine):
    life_support_rating = submarine.get_life_support_rating()

    print("solution task 2: " + life_support_rating)


if __name__ == '__main__':
    filereader = Filereader('test.txt')
    file_content = filereader.get_content()
    filereader.close()

    submarine = Submarine()
    submarine.diagnostic_report = [list(map(int, x)) for x in file_content]

    task1(submarine)
    task2(submarine)
