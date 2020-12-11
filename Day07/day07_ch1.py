import argparse


'''
    light red:      [bright white, muted yellow]
    dark orange:    [bright white, muted yellow]
    bright white:   [shiny gold]
    muted yellow:   [shiny gold, faded blue]
    shiny gold:     [dark olive, vibrant plum]
    dark olive:     [faded blue, dotted black]
    vibrant plum:   [faded blue, dotted black]
    faded blue:     []
    dotted black:   []

    -- INVERTED --

    bright white:   [light red, dark orange]
    muted yellow:   [light red, dark orange]
    shiny gold:     [bright white, muted yellow]
    faded blue:     [muted yellow, dark olive, vibrant plum]
    dark olive:     [shiny gold]
    vibrant plum:   [shiny gold]
    dotted black:   [dark olive, vibrant plum]

                 <-- CONTAINS

    Q = [bright white, muted yellow, light red, dark orange]
    count = 2
'''


def main():
    '''
    Main execution
    '''
    with open(ARGS.input, 'r') as fp:
        lines = fp.readlines()
    lines = [x.rstrip() for x in lines]

    bags = {}
    queue = []

    for line in lines:
        splits = line.split(' bags contain ')

        val = splits[0]
        keys = [' '.join(key.split()[1:-1]) for key in splits[1].split(',')]

        for key in keys:
            if key not in bags:
                bags[key] = [val]
            else:
                bags[key].append(val)

    queue.extend(bags['shiny gold'])
    count = len(queue)

    for item in queue:
        if item not in bags:
            pass
        else:
            for bag in bags[item]:
                if bag not in queue:
                    queue.append(bag)
                    count += 1

    return count


# --------------------------------------------------------------------------- //
if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('-i', '--input', required=True, help='input file')
    ARGS = PARSER.parse_args()

    print(main())
