import argparse


def main():
    '''
    Main execution
    '''
    with open(ARGS.input, 'r') as fp:
        lines = fp.readlines()
    lines = [x.rstrip() for x in lines]

    sets = []
    count = 0

    for line in lines:
        if line:
            sets.append(set(c for c in line))
        else:
            count += len(sets[0].intersection(*sets))
            sets.clear()

    if sets:
        count += len(sets[0].intersection(*sets))

    return count


# --------------------------------------------------------------------------- //
if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('-i', '--input', required=True, help='input file')
    ARGS = PARSER.parse_args()

    print(main())
