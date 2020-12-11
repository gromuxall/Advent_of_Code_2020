import argparse


class BagOfHolding():

    def __init__(self, lines):
        self.bags = {}
        self.lines = lines
        self.fill_dict()

    def fill_dict(self):
        for line in self.lines:
            splits = line.split(' bags contain ')

            key = splits[0]
            vals = [(' '.join(val.split()[1:-1]), val.split()[0])
                    for val in splits[1].split(',')]

            for val in vals:
                if key not in self.bags:
                    self.bags[key] = [val]
                else:
                    self.bags[key].append(val)

    def bag_count(self, bag):
        if bag[1] == 'no':
            return 0
        return int(bag[1]) + int(bag[1]) * sum(self.bag_count(x) for x in
                                               self.bags[bag[0]])


# --------------------------------------------------------------------------- //
def main():
    with open(ARGS.input, 'r') as fp:
        lines = fp.readlines()
    lines = [x.rstrip() for x in lines]

    bag = BagOfHolding(lines)

    return sum(bag.bag_count(x) for x in bag.bags['shiny gold'])


# --------------------------------------------------------------------------- //
if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('-i', '--input', required=True, help='input file')
    ARGS = PARSER.parse_args()

    print(main())
