import argparse


def main():
    '''
    Main execution
    '''
    with open(ARGS.input, 'r') as fp:
        lines = fp.readlines()
    lines = [[x.split()[0], int(x.split()[1].rstrip()), False] for x in lines]

    acc = 0
    sp = 0

    while 1:
        if lines[sp][2]:
            return acc

        lines[sp][2] = True

        if lines[sp][0] == 'nop':
            sp += 1
        elif lines[sp][0] == 'acc':
            acc += lines[sp][1]
            sp += 1
        else:
            sp += lines[sp][1]

    return acc


# --------------------------------------------------------------------------- //
if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('-i', '--input', required=True, help='input file')
    ARGS = PARSER.parse_args()

    print(main())
