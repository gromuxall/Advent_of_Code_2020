import argparse


def main():
    '''
    Main execution
    '''
    with open(ARGS.input, 'r') as fp:
        lines = fp.readlines()
    valid = 0

    for line in lines:
        splits = line.split()
        _min = int(splits[0].split('-')[0])
        _max = int(splits[0].split('-')[1])
        _char = splits[1].split(':')[0]
        password = splits[2]

        if (password[_min-1] == _char) ^ (password[_max-1] == _char):
            valid += 1
    return valid


# --------------------------------------------------------------------------- //
if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('-i', '--input', required=True, help='input file')
    ARGS = PARSER.parse_args()

    print(main())
