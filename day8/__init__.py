from helper.filereader import Filereader

digits = {
    0: [0, 1, 2, 4, 5, 6],
    1: [2, 5],
    2: [0, 2, 3, 4, 6],
    3: [0, 2, 3, 5, 6],
    4: [1, 2, 3, 5],
    5: [0, 1, 3, 5, 6],
    6: [0, 1, 3, 4, 5, 6],
    7: [0, 2, 5],
    8: [0, 1, 2, 3, 4, 5, 6],
    9: [0, 1, 2, 3, 5, 6]
}

digits_count = {
    2: [1],
    3: [7],
    4: [4],
    5: [2, 3, 5],
    6: [0, 6, 9],
}


def task1(input):
    unique = [2, 4, 3, 7]

    count = 0

    for line in input:
        (patterns, values) = line.split(' | ')
        segment_counts = list(map(len, values.split()))
        count += sum(el in unique for el in segment_counts)

    print(count)


def task2(input):
    output = 0

    for line in input:
        (patterns, values) = line.split(' | ')
        segment_counts = list(map(len, patterns.split()))
        print(str(segment_counts))

    print(output)


if __name__ == '__main__':
    filereader = Filereader('test.txt')
    input = filereader.get_content()

    task2(input)
