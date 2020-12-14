import argparse


def main():
    '''
    Main execution
    '''
    with open(ARGS.input, 'r') as fp:
        lines = fp.readlines()
    lines = [int(x.rstrip()) for x in lines]
    start = 0
    end = 1
    target = 14360655

    while end < len(lines):
        window = lines[start:end]

        if sum(window) == target:
            return min(window) + max(window)

        if sum(window) > target:
            start += 1
        else:
            end += 1


# --------------------------------------------------------------------------- //
if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('-i', '--input', required=True, help='input file')
    ARGS = PARSER.parse_args()

    print(main())
