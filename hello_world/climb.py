from collections import Counter, ChainMap, defaultdict, deque
import os


def climb_stairs(n):
    ways = [0] * (n + 1)
    ways[0] = 1
    ways[1] = 1
    for i in range(2, n+1):
        ways[i] = ways[i - 1] + ways[i - 2]
    return ways[n]


if __name__ == "__main__":
    res = climb_stairs(4)
    print(res)
