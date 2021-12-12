from helper.filereader import Filereader


def task1(input):
    initial_state = list(map(int, input.split(',')))

    for i in range(80):
        new_fishes = 0
        for index, counter in enumerate(initial_state):
            if counter == 0:
                initial_state[index] = 6
                new_fishes += 1
            else:
                initial_state[index] -= 1
        initial_state.extend([8] * new_fishes)

    print(len(initial_state))



def calculate_fishes(days) -> int:
    if days <= 0:
        return 0
    return 1 + calculate_fishes(days-7) + calculate_fishes(days-9)


def task2(input):
    initial_state = list(map(int, content.split(',')))

    days = 256
    fishes = len(initial_state)
    for index, counter in enumerate(initial_state):
        new_fishes = calculate_fishes(days-counter)
        fishes += new_fishes
        index += 1

    print(fishes)


if __name__ == '__main__':
    filereader = Filereader('test.txt')
    content = filereader.readline(0)

    task2(content)
