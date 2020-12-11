import argparse


def main():
    '''
    Main execution
    '''
    with open(ARGS.input, 'r') as fp:
        lines = fp.readlines()
    lines = [x.rstrip() for x in lines]

    temp = set()
    count = 0

    for line in lines:
        if line:
            temp.update(c for c in line)
        else:
            count += len(temp)
            temp.clear()

    if temp:
        count += len(temp)

    return count


# --------------------------------------------------------------------------- //
if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('-i', '--input', required=True, help='input file')
    ARGS = PARSER.parse_args()

    print(main())
