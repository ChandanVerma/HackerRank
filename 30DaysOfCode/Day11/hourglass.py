#!/bin/python3

import math
import os
import random
import re
import sys

def _get_hourglass_sum(matrix, row, col):
    sum = 0
    sum += matrix[row-1][col-1]
    sum += matrix[row-1][col]
    sum += matrix[row-1][col+1]
    sum += matrix[row][col]
    sum += matrix[row+1][col-1]
    sum += matrix[row+1][col]
    sum += matrix[row+1][col+1]
    return sum


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    max_hour_glass_sum = -63
    for i in range(1, 5):
        for j in range(1, 5):
            hour_glass_sum = _get_hourglass_sum(arr, i, j)
            if hour_glass_sum > max_hour_glass_sum:
                max_hour_glass_sum = hour_glass_sum

print(max_hour_glass_sum)