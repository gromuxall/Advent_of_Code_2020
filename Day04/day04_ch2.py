import argparse


def validator(field, val):
    '''Takes field of passport and returns True if field is valid'''
    ecl_set = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

    val_func = {
        'byr': lambda x: 1920 <= int(x) <= 2002,
        'iyr': lambda x: 2010 <= int(x) <= 2020,
        'eyr': lambda x: 2020 <= int(x) <= 2030,
        'hgt': lambda x: (x[-2:] == 'cm' and 150 <= int(x[:-2]) <= 193) or
               (x[-2:] == 'in' and 59 <= int(x[:-2]) <= 76),
        'hcl': lambda x: len(x) == 7 and x[0] == '#' and
               all(c.isalnum() for c in x[1:]),
        'ecl': lambda x: x in ecl_set,
        'pid': lambda x: len(x) == 9 and all(num.isdigit() for num in x),
        'cid': lambda x: True
    }

    return val_func[field](val)


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
            entries.append({x.split(':')[0]: x.split(':')[1] for x in temp})
            temp = []

    # clean up last entry
    if temp:
        entries.append({x.split(':')[0]: x.split(':')[1] for x in temp})

    for entry in entries:
        if len(entry) < 7:
            pass
        elif len(entry) == 8 or (len(entry) == 7 and 'cid' not in entry.keys()):
            if all(validator(key, val) for (key, val) in entry.items()):
                valid += 1

    return valid


# --------------------------------------------------------------------------- //
if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('-i', '--input', required=True, help='input file')
    ARGS = PARSER.parse_args()

    print(main())
