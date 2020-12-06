import argparse

# 70, 7, 567
# 14, 7, 119,
# 102, 4, 820


def main():
    '''
    Main execution
    '''
    with open(ARGS.input, 'r') as fp:
        lines = fp.readlines()
    lines = [x.rstrip() for x in lines]
    col = range(8)
    rows = range(128)
    
    n = lines[0]

    for i in range(0, 7):
        if n[i] == "B":
            rows = rows[]
        n[:int(row/2)]
    print(row)

    for i in range(7, 10):
        pass



    return None


# --------------------------------------------------------------------------- //
if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('-i', '--input', required=True, help='input file')
    ARGS = PARSER.parse_args()

    print(main())
