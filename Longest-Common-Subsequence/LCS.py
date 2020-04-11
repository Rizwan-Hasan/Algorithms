#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time


def LCS_Length(X: str, Y: str):
    m, n = len(X), len(Y)
    L, B = list(), list()
    for i in range(m + 1):
        L.append([0] * (n + 1))
        B.append([0] * (n + 1))

    upArrow: str = '↑'
    leftArrow: str = '←'
    leftCornerArrow: str = '↖'
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                continue
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
                B[i][j] = leftCornerArrow
            else:
                L[i][j]: int = max(L[i - 1][j], L[i][j - 1])
                if L[i - 1][j] > L[i][j - 1]:
                    B[i][j] = upArrow
                if L[i - 1][j] < L[i][j - 1]:
                    B[i][j] = leftArrow
                else:
                    B[i][j] = upArrow

    result: dict = {
        'MN': [m, n],
        'LCS': L,
        'Backtrack': B
    }
    return result


def Print_LCS(B: list, X: str, i: int, j: int):
    upArrow: str = '↑'
    leftArrow: str = '←'
    leftCornerArrow: str = '↖'

    if i == 0 or j == 0:
        return
    if B[i][j] == leftCornerArrow:
        Print_LCS(B, X, i - 1, j - 1)
        print(X[i - 1], end='')
    elif B[i][j] == upArrow:
        Print_LCS(B, X, i - 1, j)
    else:
        Print_LCS(B, X, i, j - 1)


def main():
    s1: str = input('First word: ').strip().upper()
    s2: str = input('Second Word: ').strip().upper()
    result: dict = LCS_Length(s1, s2)
    print()
    print('LCS Table:')
    for i in result['LCS']:
        print('\t', end='')
        print(i)
    print()
    print('Backtrack Table:')
    for i in result['Backtrack']:
        print('\t', end='')
        print(i)
    print()
    print('LCS Length: %d' % result['LCS'][result['MN'][0]][result['MN'][1]])
    print('Longest Common Subsequence: ', end='')
    Print_LCS(result['Backtrack'], s1, result['MN'][0], result['MN'][1])
    print()


if __name__ == '__main__':
    HELLO_WORLD = True
    if HELLO_WORLD is True:
        start_time = time.time()
        main()
        print("--- %.5s seconds ---" % (time.time() - start_time))
    else:
        main()
