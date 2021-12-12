from helper.filereader import Filereader


def get_adjacents(row, column, input):
    # adjacents = [(1, 7.57), (2, 2.1), (3, 1.2), (4, 2.1), (5, 0.01),
    #      (6, 0.5), (7, 0.2), (8, 0.6)]
    adjacents = []

    if row > 0:
        adjacents.append(((row - 1, column), int(input[row - 1][column]) ))
    if row + 1 < len(input):
        adjacents.append(((row + 1, column), int(input[row + 1][column])))
    if column > 0:
        adjacents.append(((row, column - 1), int(input[row][column - 1])))
    if column + 1 < len(input[row]):
        adjacents.append(((row, column + 1), int(input[row][column + 1])))

    adjacents.sort(key=lambda x: x[1])

    return adjacents


def get_low_points(input):
    low_points = {}
    for row, line in enumerate(input):
        heights = list(line)
        for column, height in enumerate(heights):
            adjacents = get_adjacents(row, column, input)

            # if int(height) < min(adjacents, key = lambda t: t[1]):
            if int(height) < adjacents[0][1]:
                low_points[(row, column)] = 1+int(height)

    return low_points


def extend_basin(basin, coordinates, visited, input):
    row, column = coordinates

    adjacents = get_adjacents(row, column, input)
    for adjacent in adjacents:
        extended = False
        if adjacent[1] < 9 and not adjacent[0] in visited:
            basin.append(adjacent[0])
            extended = True
        visited.append(adjacent[0])

        if extended:
            extend_basin(basin, adjacent[0], visited, input)


def task1(input):
    low_points = get_low_points(input)

    print(sum(low_points.values()))


def task2(input):
    basins = []

    # fuer jeden lowpoint
    for row, column in get_low_points(input).keys():
        basin = [(row, column)]
        visited = [(row, column)]

        extend_basin(basin, (row, column), visited, input)
        basins.append(basin)

    sorted_length = sorted(list(map(len, basins)), reverse=True)

    print(str(sorted_length[0] * sorted_length[1] * sorted_length[2]))


if __name__ == '__main__':
    filereader = Filereader('input.txt')
    input = filereader.get_content()

    task2(input)
