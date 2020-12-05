import argparse

class Slope:
    row_len = None

    def __init__(self, right, down):
        self.right = right
        self.down = down
        self.index = 0
        self.trees = 0

    def move(self):
        self.index += self.right
        return self.index % Slope.row_len

    def is_tree(self, row):
        if row[self.move()] == '#':
            self.trees += 1


def main():
    '''
    Main execution
    '''
    with open(ARGS.input, 'r') as fp:
        lines = fp.readlines()
    lines = [x.rstrip() for x in lines]
    row_len = len(lines[0])

    Slope.row_len = row_len
    s1 = Slope(1, 1)
    s2 = Slope(3, 1)
    s3 = Slope(5, 1)
    s4 = Slope(7, 1)
    s5 = Slope(1, 2)


    for i in range(1, len(lines)):
        s1.is_tree(lines[i])
        s2.is_tree(lines[i])
        s3.is_tree(lines[i])
        s4.is_tree(lines[i])

        if i % 2 == 0:
            s5.is_tree(lines[i])

    return s1.trees * s2.trees * s3.trees * s4.trees * s5.trees


# --------------------------------------------------------------------------- //
if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('-i', '--input', required=True, help='input file')
    ARGS = PARSER.parse_args()

    print(main())
