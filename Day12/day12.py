'''
    Steven Madonna
'''
import argparse


class Ship():
    '''Object representing the ship and associated methods'''

    def __init__(self, moves):
        self.moves = moves
        self.chart = [['E', 0], ['S', 0], ['W', 0], ['N', 0]]
        self.compass = {'E': 0, 'S': 1, 'W': 2, 'N': 3}
        self.dir = 0

    def set_sail(self):
        '''Iterates through moves calling take_helm and returns
        the Manhattan distance'''
        for move in self.moves:
            self.take_helm(move)
        return abs(self.chart[0][1] - self.chart[2][1]) +\
               abs(self.chart[1][1] - self.chart[3][1])

    def change_course(self, _dir, dgr):
        '''Calculates index of chart array and sets the
        now current direction'''
        if _dir == 'L':
            self.dir = (self.dir - int(dgr / 90)) % 4
        else:
            self.dir = (self.dir + int(dgr / 90)) % 4

    def take_helm(self, cmd):
        '''Takes command and increases value in chart'''
        if cmd[0] == 'F':
            self.chart[self.dir][1] += cmd[1]
        elif cmd[0] == 'R' or cmd[0] == 'L':
            self.change_course(cmd[0], cmd[1])
        else:
            self.chart[self.compass[cmd[0]]][1] += cmd[1]



# --------------------------------------------------------------------------- //
if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('-i', '--input', required=True, help='input file')
    ARGS = PARSER.parse_args()

    with open(ARGS.input, 'r') as fp:
        lines = fp.readlines()

    print(Ship([(x[0], int(x[1:].rstrip())) for x in lines]).set_sail())
