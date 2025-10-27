import sys

__MIN_LENGTH = 100
__MAX_LENGTH = 170

__TEX_PROBLEM = '\\textproblem {0}\\answer{{_}}'

def resplit(infile, outfile, pattern='{}', width=50):
    problems = read_and_process(infile, pattern, width)
    with open(outfile, 'w', encoding='utf-8') as outf:
        for problem in problems:
            text, index, grade = problem
            outf.write(grade)
            outf.write('\n')
            outf.write(text)
            outf.write('\n\n')


def read_and_process(infile, pattern='{}', width=50):
    problemcount = 0
    problems = []
    with open(infile, 'r', encoding='UTF-8') as inf:
        while True:
            text, length = read_one(inf)
            if length == 0:
                break

            grade = grade_by_size(length)
            splitted = reformat_one(text, pattern='{}', width=width)
            problemcount += 1
            problems.append((splitted, problemcount, grade))
    return problems

def grade_by_size(length):
    if length < __MIN_LENGTH:
        return f'%% small ({length})'

    if length > __MAX_LENGTH:
        return f'%% big ({length})'

    return f'%% normal ({length})'

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
    resplit(sys.argv[1], sys.argv[2], width=50)
