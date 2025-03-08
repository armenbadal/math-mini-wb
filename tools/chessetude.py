
#    pawn   զինվոր
#    bishop փիղ
#    knight ձի
#    rook   նավակ
#    queen  թագուհի
#    king   արքա

import re
import sys
from copy import deepcopy

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

ROW = {'1': 8, '2': 7, '3': 6, '4': 5, '5': 4, '6': 3, '7': 2, '8': 1}
COLUMN = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
FIGURES = {
    'white': {
        'pawn':   (58373, 57689),
        'knight': (58372, 57688),
        'bishop': (58371, 57687),
        'rook':   (58370, 57686),
        'queen':  (58369, 57685),
        'king':   (58368, 57684)
    },
    'black': {
        'pawn':   (57945, 57695),
        'knight': (57944, 57694),
        'bishop': (57943, 57693),
        'rook':   (57942, 57692),
        'queen':  (57941, 57691),
        'king':   (57945, 57690)
    }
}

BOARD = [
    [58160, 58161, 58161, 58161, 58161, 58161, 58161, 58161, 58161, 58162],
    [58183,     0,     0,     0,     0,     0,     0,     0,     0, 58164],
    [58182,     0,     0,     0,     0,     0,     0,     0,     0, 58164],
    [58181,     0,     0,     0,     0,     0,     0,     0,     0, 58164],
    [58180,     0,     0,     0,     0,     0,     0,     0,     0, 58164],
    [58179,     0,     0,     0,     0,     0,     0,     0,     0, 58164],
    [58178,     0,     0,     0,     0,     0,     0,     0,     0, 58164],
    [58177,     0,     0,     0,     0,     0,     0,     0,     0, 58164],
    [58176,     0,     0,     0,     0,     0,     0,     0,     0, 58164],
    [58165, 58184, 58185, 58186, 58187, 58188, 58189, 58190, 58191, 58167]
]


def empty_board():
    board = deepcopy(BOARD)
    for r in ['8', '7', '6', '5', '4', '3', '2', '1']:
        for c in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
            ri, ci = ROW[r], COLUMN[c]
            board[ri][ci] = 57600 if (ri + ci) % 2 == 1 else 32
    return board


def build_etude_board(pieces):
    board = empty_board()
    for column, row, colour, figure in pieces:
        ri, ci = ROW[row], COLUMN[column]
        board[ri][ci] = FIGURES[colour][figure][(ri + ci) % 2]
    return board


def build_one_etude(pieces):
    board = build_etude_board(pieces)

    text = '\\halign{#&#&#&#&#&#&#&#&#&#\\cr\n'
    for row in board:
        text += '&'.join(map(lambda e: f'\\char{e}', row)) + '\\cr\n'
    text += '}'

    text = '\\centerline{\\vbox{\\symchess\\offinterlineskip\n' + text + '}}'
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


