from helper.filereader import Filereader


def task1(crabs):
    max_pos = max(crabs)
    min_pos = min(crabs)

    fuel = {}

    for i in range(min_pos, max_pos):
        fuel[i] = 0
        for crab in crabs:
            fuel[i] += abs(crab-i)

    print(min(fuel.values()))


def task2(crabs):
    max_pos = max(crabs)
    min_pos = min(crabs)

    fuel = {}

    for i in range(min_pos, max_pos):
        fuel[i] = 0
        for crab in crabs:
            fuel[i] += sum(range(abs(crab-i)+1))

    print(min(fuel.values()))


if __name__ == '__main__':
    filereader = Filereader('input.txt')
    crabs = sorted(list(map(int, filereader.readline(0).split(','))))

    task1(crabs)
    task2(crabs)
