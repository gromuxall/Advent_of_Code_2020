import argparse


def main():
    '''
    Main execution
    '''
    with open(ARGS.input, 'r') as fp:
        lines = fp.readlines()
    lines = sorted([int(x.rstrip()) for x in lines])
    lines.insert(0, 0)
    lines.append(lines[-1] + 3)

    threes = 0
    ones = 0

    for i in range(1, len(lines)):
        diff = lines[i] - lines[i-1]

        if diff == 3:
            threes += 1
        if diff == 1:
            ones += 1

    return ones * threes


# --------------------------------------------------------------------------- //
if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('-i', '--input', required=True, help='input file')
    ARGS = PARSER.parse_args()

    print(main())
