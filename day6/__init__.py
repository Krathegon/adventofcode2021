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


# def task2(input):
#     initial_state = list(map(int, content.split(',')))
#
#     days = 18
#     fishes = len(initial_state)
#     for counter in initial_state:
#         new_fishes = (days - counter) % 6

if __name__ == '__main__':
    filereader = Filereader('test.txt')
    content = filereader.readline(0)

    task1(content)
