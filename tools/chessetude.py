
#    pawn   զինվոր
#    bishop փիղ
#    knight ձի
#    rook   նավակ
#    queen   թագուհի
#    king    արքա

import re
import sys

def read_file(file):
    with open(file, 'r') as f:
        return f.readlines()


def read_etudes(stream):
    beginning = re.compile(r'^etude\s+([a-z\-]+)\s*$')
    placement = re.compile(r'^([a-h])\s+([1-8])\s+(white|black)\s+(pawn|bishop|knight|rook|queen|king)\s*$')

    etudes = []
    name = ''
    pieces = []

    for line in stream:
        if len(line) == 0:
            continue

        m = beginning.match(line)
        if m:
            if name != '' and len(pieces) != 0:
                etudes.append((name, pieces))
                pieces = []
            name = m.group(1)
            continue

        m = placement.match(line)
        if m:
            pieces.append((m.group(1), m.group(2), m.group(3), m.group(4)))
        
    if name != '' and len(pieces) != 0:
        etudes.append((name, pieces))

    return etudes

ROW = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
COLUMN = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
CODES = {
    'pawn': ('P', 'O'),
    'bishop': ('B', 'A'),
    'knight': ('N', 'M'),
    'rook': ('R', 'S'),
    'queen': ('Q', 'L'),
    'king': ('K', 'J')
}

def empty_board():
    board = []
    for r in ['8', '7', '6', '5', '4', '3', '2', '1']:
        line = []
        for c in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
            ix = ROW[r] + COLUMN[c]
            line.append('0' if ix % 2 == 0 else 'Z')
        board.append(line)
        line = []
    return board


def build_etude_board(pieces):
    board = empty_board()
    for column, row, colour, figure in pieces:
        ri, ci = ROW[row], COLUMN[column]
        ix = ri + ci
        code = CODES[figure][ix % 2]
        if colour == 'black':
            code = code.lower()
        board[ri][ci] = code
    return board


def build_one_etude(pieces):
    board = build_etude_board(pieces)

    text = '\\halign{\\vrule#&#&#&#&#&#&#&#\\vrule\\cr\n\\noalign{\\hrule}'
    for row in board:
        text += '&'.join(row) + '\\cr\n'
    text += '\\noalign{\\hrule}}'

    text = '\\centerline{\\vbox{\\chessten\\offinterlineskip\n' + text + '}}'
    return text


def build_etudes(etudes):
    for (name, pieces) in etudes:
        etude_TeX = build_one_etude(pieces)
        with open(name + '.tex', 'w') as f:
            f.write(etude_TeX)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        exit(0)
    
    source = sys.argv[1]
    with open(source, 'r') as s:
        etudes = read_etudes(s)
        build_etudes(etudes)


