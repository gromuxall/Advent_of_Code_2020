import argparse


def main():
    '''
    Main execution
    '''
    nums = {}

    with open(ARGS.input, 'r') as fp:
        lines = fp.readlines()

    for line in lines:
        line = int(line)
        diff = 2020 - line

        if line in nums:
            return nums[line] * line
        nums[diff] = line

    return None


# --------------------------------------------------------------------------- //
if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('-i', '--input', required=True, help='input file')
    ARGS = PARSER.parse_args()

    print(main())
