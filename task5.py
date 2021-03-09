#!/usr/bin/env python
size = int(input())

matrix = []
for i in range(size):
    list1 = [int(i) for i in input().split()]
    matrix.append(list1)

line1 = 0
line2 = 0
for i in range(size):
    for k in range(size):
        if i == k:
            line1 += matrix[i][k]
        if i == size - k - 1:
            line2 += matrix[i][k]

print(abs(line1 - line2))
