ROW_BITS = 7
COLUMN_BITS = 3

ROWS = 2 ** ROW_BITS
COLUMNS = 2 ** COLUMN_BITS

with open('data.txt') as f:
    data = f.read().splitlines()

class Plane:
    def __init__(self):
        self.rows = []
        for r in range(ROWS):
            row = []
            for c in range(COLUMNS):
                row.append('.')
            self.rows.append(row)

    def set_taken(self, row, column):
        self.rows[row][column] = '#'

    def print(self):
        for row_number in range(len(self.rows)):
            row = self.rows[row_number]
            row_text = ''
            for seat in row:
                row_text = row_text + str(seat)
            print("{0}:  \t{1}".format(row_number, row_text))

    def seat_id(self, row, column):
        return row*8 + column


max_seat_id = 0

for boarding_pass in data:
    #assert (len(boarding_pass) == 10)
    if len(boarding_pass) > 10:
        assert (False)
    row = boarding_pass[:7]
    row = row.replace('F', '0')
    row = row.replace('B', '1')
    row = int(row, 2)
    column = boarding_pass[7:]
    column = column.replace('L', '0')
    column = column.replace('R', '1')
    column = int(column, 2)

    plane.set_taken(row, column)

    seat_id = row * 8 + column
    if seat_id > max_seat_id:
        print('max increased: {0}'.format(seat_id))
        max_seat_id = seat_id


plane.print()

