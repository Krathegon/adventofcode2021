from helper.filereader import Filereader


def task1(content):
    field = [ [0]*1000 for i in range(1000)]

    for line in content:
        (_from, _to) = line.split(' -> ')
        (x1, y1) = tuple(map(int, _from.split(',')))
        (x2, y2) = tuple(map(int, _to.split(',')))

        if x1 == x2:
            if y2 > y1:
                for i in range(y1, y2+1):
                    field[x1][i] += 1
            else:
                for i in range(y2, y1+1):
                    field[x1][i] += 1
        elif y1 == y2:
            if x2 > x1:
                for i in range(x1, x2+1):
                    field[i][y1] += 1
            else:
                for i in range(x2, x1+1):
                    field[i][y1] += 1

    count = 0
    for x in range(len(field)):
        for y in range(len(field[x])):
            if field[x][y] >= 2:
                count += 1

    print(count)


def task2(content):
    field = [ [0]*1000 for i in range(1000)]

    for line in content:
        (_from, _to) = line.split(' -> ')
        (x1, y1) = tuple(map(int, _from.split(',')))
        (x2, y2) = tuple(map(int, _to.split(',')))

        if x1 == x2:
            if y2 > y1:
                for i in range(y1, y2+1):
                    field[x1][i] += 1
            else:
                for i in range(y2, y1+1):
                    field[x1][i] += 1
        elif y1 == y2:
            if x2 > x1:
                for i in range(x1, x2+1):
                    field[i][y1] += 1
            else:
                for i in range(x2, x1+1):
                    field[i][y1] += 1
        elif abs(x1-x2) == abs(y1-y2):
            for i in range(0, abs(x1-x2)+1):
                if x1 > x2 and y1 > y2:
                    field[x1-i][y1-i] += 1
                elif x1 > x2 and y1 < y2:
                    field[x1-i][y1+i] += 1
                elif x1 < x2 and y1 > y2:
                    field[x1+i][y1-i] += 1
                elif x1 < x2 and y1 < y2:
                    field[x1+i][y1+i] += 1

    count = 0
    for x in range(len(field)):
        for y in range(len(field[x])):
            if field[x][y] >= 2:
                count += 1

    print(count)


if __name__ == '__main__':
    filereader = Filereader('input.txt')
    content = filereader.get_content()

    task1(content)
    task2(content)


