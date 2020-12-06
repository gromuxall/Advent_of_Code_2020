import argparse


def main():
    '''
    Main execution
    '''
    with open(ARGS.input, 'r') as fp:
        lines = fp.readlines()
    lines = [x.rstrip() for x in lines]

    temp = []
    entries = []
    valid = 0

    for line in lines:
        if line:
            temp.extend(line.split())
        else:
            entries.append(temp)
            temp = []

    # clean up last entry
    if temp:
        entries.append(temp)

    for entry in entries:
        if len(entry) == 8:
            valid += 1
        elif len(entry) == 7:
            valid += 1
            for item in entry:
                if 'cid' in item:
                    valid -= 1
    return valid


# --------------------------------------------------------------------------- //
if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('-i', '--input', required=True, help='input file')
    ARGS = PARSER.parse_args()

    print(main())
