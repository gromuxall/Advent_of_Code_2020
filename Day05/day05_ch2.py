import argparse


def main():
    '''
    Main execution
    '''
    with open(ARGS.input, 'r') as fp:
        lines = fp.readlines()
    lines = [x.rstrip() for x in lines]

    all_seats = {}

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

        if rows[0] not in all_seats:
            all_seats[rows[0]] = []

        all_seats[rows[0]].append(cols[0])

    for seat in all_seats.keys():
        if len(all_seats[seat]) < 8:
            print('{}: {}'.format(seat, sorted(all_seats[seat])))


# --------------------------------------------------------------------------- //
if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('-i', '--input', required=True, help='input file')
    ARGS = PARSER.parse_args()

    main()
