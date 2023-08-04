# На Java делал задачу по расстановке ферзей, чтобы они не били друг друга)
# https://github.com/PavelVolchenko/JavaHomework/blob/main/src/hw05/task03.java

from itertools import permutations

SIDE = 8
COLS = 'abcdefgh'
ROWS = '12345678'


def check_queens(arr):
    for i in range(len(arr)):
        row_prev, col_prev = arr[i]
        for j in range(i + 1, len(arr)):
            row_next, col_next = arr[j]
            if (
                row_prev == row_next or
                col_prev == col_next or
                abs(row_prev - row_next) == abs(col_prev - col_next)
            ):
                return False
    print(arr)
    return True


def play_another():
    win_combs = set()
    coord_pack = []
    for comb in permutations(COLS):
        coord_pack.append([(COLS.find(pair[0]), ROWS.find(pair[1])) for pair in zip(comb, ROWS)])
    for pack in coord_pack:
        if check_queens(pack):
            win_combs.add(tuple(pack))
    return win_combs


def board_printer(board):
    print('  ' + ''.join(f'{i:^3}' for i in COLS))
    for r_num, row in enumerate(board, start=1):
        print(r_num, ''.join(f'{i:^3}' if i else f'{".":^3}' for i in row))
    print(f'\n{"=" * 30}')


if __name__ == '__main__':
    win_placements = play_another()
    print(len(win_placements))