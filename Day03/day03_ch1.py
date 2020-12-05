import argparse


def main():
    '''
    Main execution
    '''
    with open(ARGS.input, 'r') as fp:
        lines = fp.readlines()
    lines = [x.rstrip() for x in lines]
    row_len = len(lines[0])
    idx = 0
    trees = 0

    for i in range(1, len(lines)):
        idx += 3
        if lines[i][idx % row_len] == '#':
            trees += 1
    return trees


# --------------------------------------------------------------------------- //
if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('-i', '--input', required=True, help='input file')
    ARGS = PARSER.parse_args()

    print(main())
