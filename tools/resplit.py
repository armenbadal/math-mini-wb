import sys

__MIN_LENGTH = 100
__MAX_LENGTH = 170

__TEX_PROBLEM = '\\textproblem {0}\\answer{{_}}'

def resplit(infile, width=50):
    with open(infile, 'r', encoding='UTF-8') as inf:
        while True:
            text, length = read_one(inf)
            if length == 0:
                break
            if length < __MIN_LENGTH or length > __MAX_LENGTH:
                continue
            splitted = reformat_one(text, width=width)
            print(splitted)
            print()

def reformat_one(text, pattern='{}', width=40):
    splitted = split_with_width(pattern.format(text), width)
    return '\n'.join(splitted)

def read_one(inf):
    block = ''
    while True:
        block = inf.readline()
        if block == '':
            return '', 0
        else:
            block = block.strip()
        if len(block) != 0:
            break

    for line in inf:
        line = line.strip()
        if len(line) == 0:
            break
        block += ' ' + line

    return block, len(block)

def split_with_width(text, width=40):
    head, tail = split_one(text, width)
    result = [head]
    while len(tail) != 0:
        head, tail = split_one(tail, width)
        result.append(head)
    return result

def split_one(text, width=40):
    if len(text) <= width:
        return text, ''

    space = width
    while text[space] != ' ':
        space -= 1
    return text[:space], text[space+1:]


if __name__ == '__main__':
    resplit(sys.argv[1], 50)
