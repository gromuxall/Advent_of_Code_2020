import argparse


def main():
    '''
    Main execution
    '''
    nums = {}

    with open(ARGS.input, 'r') as fp:
        lines = fp.readlines()
    lines = list(map(lambda x: int(x), lines))

    i = 1
    for left in lines:
        split_diff = 2020 - left
        for right in range(i, len(lines)):
            right = lines[right]
            diff = split_diff - right

            if right in nums:
                return nums[right] * right * left
            nums[diff] = right
        i += 1

    return None


# --------------------------------------------------------------------------- //
if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('-i', '--input', required=True, help='input file')
    ARGS = PARSER.parse_args()

    print(main())
