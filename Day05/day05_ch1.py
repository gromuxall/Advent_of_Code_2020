import argparse


def main():
    '''
    Main execution
    '''
    with open(ARGS.input, 'r') as fp:
        lines = fp.readlines()
    lines = [x.rstrip() for x in lines]
    high = 0

    for bpass in lines:
        cols = list(range(8))
        rows = list(range(128))

        for letter in bpass:
            if letter == 'F':
                rows = rows[:int(len(rows)/2)]
            elif letter == 'B':
                rows = rows[int(len(rows)/2):]
            elif letter == 'L':
                cols = cols[:int(len(cols)/2)]
            elif letter == 'R':
                cols = cols[int(len(cols)/2):]

        result = rows[0] * 8 + cols[0]
        if result > high:
            high = result

    return high


# --------------------------------------------------------------------------- //
if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('-i', '--input', required=True, help='input file')
    ARGS = PARSER.parse_args()

    print(main())
