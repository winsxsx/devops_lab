#!/usr/bin/env python
N = int(input())

if 0 <= N <= 9:
    print(N + 10)
else:
    numbers = list()
    for i in range(9, 1, -1):
        while N % i == 0:
            numbers.append(i)
            N = N // i
    if N != 1:
        print("-1")
    else:
        Q = 0
        while len(numbers) != 0:
            Q = Q * 10 + numbers[-1]
            numbers.pop()
        print(Q)
