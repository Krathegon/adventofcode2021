from helper.filereader import Filereader


class Bingo:
    def __init__(self, bingo_numbers, bingo_fields):
        self.bingo_numbers = bingo_numbers
        self.bingo_fields = bingo_fields

    def play_bingo(self):
        score = {}
        # for each number
        for number in self.bingo_numbers:
            # go through every field
            for index in range(len(self.bingo_fields)):
                if index in score:
                    continue
                field = self.bingo_fields[index]
                crossed = False
                for row in range(len(field)):
                    # only one cross allowed
                    if crossed:
                        break
                    for column in range(len(field[row])):
                        # cross out number if found
                        if field[row][column] == number:
                            field[row][column] = 'x'

                            bingo_found = self.is_bingo(field, row, column)
                            if bingo_found:
                                print('bingo found: ' + str(row) + ' ' + str(column) + ',  field: ' + str(index) + ', score: ' + str(self.get_sum(field) * int(number)))
                                # if bingo: get sum of field and multiply by number
                                score[index] = self.get_sum(field) * int(number)
                            crossed = True
                            break
        return score

    def is_bingo(self, field, row, column):
        if all(item == 'x' for item in field[row]):
            return True
        for i in range(5):
            if field[i][column] != 'x':
                return False
        return True

    def get_sum(self, field):
        val = 0
        for row in range(len(field)):
            for column in range(len(field[row])):
                if field[row][column] != 'x':
                    val += int(field[row][column])
        return val


if __name__ == '__main__':
    filereader = Filereader('input.txt')

    bingo_numbers = filereader.readline(0).split(',')
    bingo_fields = []

    for i in range(2, filereader.get_length(), 6):
        bingo_fields.append(list(map(str.split, filereader.readlines(i, i+5))))

    bingo = Bingo(bingo_numbers, bingo_fields)

    score = bingo.play_bingo()

    print('winner: ' + str(list(score.values())[0]) + ' (field ' + str(list(score.keys())[0]) + ')')
    print('loser: ' + str(list(score.values())[len(score)-1]) + ' (field ' + str(list(score.keys())[len(score)-1]) + ')')

    filereader.close()
