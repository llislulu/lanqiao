import os
import sys


def test(n, m) -> bool:
    x = 1
    y = m
    for i in range(m):
        if n % x == n % y:
            return True
        if y == x:
            return False
        x += 1
        y -= 1


t = int(input())
for i in range(t):
    n, m = input().split()
    if test(int(n), int(m)):
        print("Yes")
    else:
        print("No")
