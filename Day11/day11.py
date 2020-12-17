'''
    Steven Madonna
'''
import argparse


class Matrix():
    '''Class to contain two matrices'''

    def __init__(self, rows):
        self.occupied = 0
        self.mtx_A = rows
        self.mtx_B = [[] for i in range(len(self.mtx_A))]
        self.neighbors = {(i, j): self.get_neighbors_p2(i, j)
                          for i in range(len(self.mtx_A))
                          for j in range(len(self.mtx_A[0]))}

    def __str__(self):
        return '[A]\n' + '\n'.join(self.mtx_A) + '\n[B]\n' + \
               '\n'.join(self.mtx_B)

    def get_occupied(self):
        '''Call main function to calculate occupied seats
        and return value'''
        self.seat_swap()
        return self.occupied

    def get_neighbors_p1(self, row, col):
        '''Calculates and returns a list of neighbor positions
        for the passed-in coordinates of the origin matrix, not including
        out-of-bounds positions or positions where . is present'''

        return [(i + row, j + col) for i in range(-1, 2) for j in range(-1, 2)
                if 0 <= i + row < len(self.mtx_A)       and
                0 <= j + col < len(self.mtx_A[0])       and
                not (i + row == row and j + col == col) and
                not self.mtx_A[i + row][j + col] == '.']

    def get_neighbors_p2(self, row, col):
        '''Calculates and returns a list of neighbor positions
        for the passed-in coordinates of the origin matrix, not including
        out-of-bounds positions and searches for next nearest neighbor
        for positions where '.' is present'''

        ret = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                _row = i + row
                _col = j + col
                if not (_row == row and _col == col):
                    while 0 <= _row < len(self.mtx_A) and 0 <= _col < len(self.mtx_A[0]):
                        cell = self.mtx_A[_row][_col]
                        if not cell == '.':
                            ret.append((_row, _col))
                            break
                        _row += i
                        _col += j
        return ret

    def seat_swap(self):
        '''Swaps matrix cell following these rules:

            - If a seat is empty (L) and there are no occupied seats
              adjacent to it, the seat becomes occupied.
            - If a seat is occupied (#) and four or more seats adjacent
              to it are also occupied, the seat becomes empty.
            - Otherwise, the seat's state does not change.
        '''
        for idxs, nbrs in self.neighbors.items():
            cell = self.mtx_A[idxs[0]][idxs[1]]

            if cell == '.':
                self.mtx_B[idxs[0]].append('.')
            else:
                if cell == 'L':
                    if all(self.mtx_A[i[0]][i[1]] == 'L' for i in nbrs):
                        self.mtx_B[idxs[0]].append('#')
                    else:
                        self.mtx_B[idxs[0]].append(cell)
                elif cell == '#':
                    if len(list(filter(
                            lambda x: self.mtx_A[x[0]][x[1]] == '#', nbrs))) >= 5:
                        self.mtx_B[idxs[0]].append('L')
                    else:
                        self.mtx_B[idxs[0]].append(cell)
        self.mtx_B = [''.join(row) for row in self.mtx_B]
        self.compare()

    def mtx_swap(self):
        '''Copies mtx_B (the resultant matrix) to mtx_A (the origin matrix)'''
        self.mtx_A = [row[:] for row in self.mtx_B]
        self.mtx_B = [[] for i in range(len(self.mtx_A))]

    def compare(self):
        '''Compares both matrices A and B, returning the count of
        occupied seats if both matrices are the same, swapping the matrices
        and running again if not
        '''
        print(self)
        if self.mtx_B == self.mtx_A:
            self.occupied = sum([row.count('#') for row in self.mtx_A])
        else:
            self.mtx_swap()
            self.seat_swap()


# --------------------------------------------------------------------------- //
if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('-i', '--input', required=True, help='input file')
    ARGS = PARSER.parse_args()

    with open(ARGS.input, 'r') as fp:
        lines = fp.readlines()

    matrix = Matrix([x.rstrip() for x in lines])

    print(matrix.get_occupied())
