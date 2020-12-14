import argparse


def main():
    '''
    Main execution
    '''
    with open(ARGS.input, 'r') as fp:
        lines = fp.readlines()
    lines = [int(x.rstrip()) for x in lines]
    start = 0

    for i in range(25, len(lines)):
        preamble = set(lines[start:i])
        if all(lines[i] - num not in preamble for num in preamble):
            return lines[i]
        start += 1


# --------------------------------------------------------------------------- //
if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('-i', '--input', required=True, help='input file')
    ARGS = PARSER.parse_args()

    print(main())
