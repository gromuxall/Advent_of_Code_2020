import argparse


class BootCode():

    def __init__(self, lines):
        self.code = [
            self.Instruction(
                idx, x.split()[0], int(x.split()[1].rstrip()), False
            ) for idx, x in enumerate(lines)]
        self.sp = 0
        self.acc = 0

    def swap_instr(self, idx):
        '''Swap instruction at passed-in index of boot code'''
        if self.code[idx].instr == 'nop':
            self.code[idx].instr = 'jmp'
        elif self.code[idx].instr == 'jmp':
            self.code[idx].instr = 'nop'

    def reset(self):
        '''Reset stack pointer and accumulator to zero'''
        self.sp = 0
        self.acc = 0

    def visited(self):
        '''Return boolean whether current line in boot code has
        been visited'''
        return self.code[self.sp].visited

    def set_visited(self):
        '''Set current line of instruction to visited'''
        self.code[self.sp].visited = True

    def instr(self, instr):
        '''Return boolean whether current line in boot code is equal
        to passed-in intruction'''
        return self.code[self.sp].instr == instr

    def get_val(self):
        '''Return integer value of current line of instruction'''
        return self.code[self.sp].val


    class Instruction():
        def __init__(self, idx, instr, val, visited):
            self.idx = idx
            self.instr = instr
            self.val = val
            self.visited = visited


# --------------------------------------------------------------------------- //
def main():
    '''
    Main execution
    '''
    with open(ARGS.input, 'r') as fp:
        lines = fp.readlines()
    bc = BootCode(lines)
    idxs = []
    last_idx = 0

    while bc.sp < len(lines):
        if bc.visited():
            if last_idx:
                bc.swap_instr(last_idx)
                idxs.pop(-1)
            bc.sp = idxs[-1]
            last_idx = bc.sp
            bc.swap_instr(bc.sp)

        bc.set_visited()

        if bc.instr('nop'):
            if bc.sp not in idxs:
                idxs.append(bc.sp)
            bc.sp += 1
        elif bc.instr('acc'):
            bc.acc += bc.get_val()
            bc.sp += 1
        else:
            if bc.sp not in idxs:
                idxs.append(bc.sp)
            bc.sp += bc.get_val()

    bc.reset()
    
    # Now run correct boot code
    while bc.sp < len(lines):
        if bc.instr('nop'):
            bc.sp += 1
        elif bc.instr('acc'):
            bc.acc += bc.get_val()
            bc.sp += 1
        else:
            bc.sp += bc.get_val()

    return bc.acc


# --------------------------------------------------------------------------- //
if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('-i', '--input', required=True, help='input file')
    ARGS = PARSER.parse_args()

    print(main())
