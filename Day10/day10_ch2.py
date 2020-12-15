import argparse


def main():
    '''
    Main execution
    '''
    with open(ARGS.input, 'r') as fp:
        lines = fp.readlines()
    lines = sorted([int(x.rstrip()) for x in lines])
    lines.insert(0, 0)
    lines.append(lines[-1] + 3)

    nodes = {line: 0 for line in lines}
    nodes[0] = 1

    for i, num in enumerate(lines):
        for nxt in lines[i+1:i+4]:
            if nxt - lines[i] < 4:
                nodes[nxt] += nodes[num]
    
    return nodes[lines[-1]]

# --------------------------------------------------------------------------- //
if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('-i', '--input', required=True, help='input file')
    ARGS = PARSER.parse_args()

    print(main())
