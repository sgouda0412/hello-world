import traceback
from multiprocessing import Process, ProcessError
from inspect import signature
from collections import Counter, defaultdict, deque, OrderedDict, UserDict
from itertools import accumulate, chain, combinations, combinations_with_replacement, compress, count, cycle
from functools import partial, cache, cached_property, reduce
import os
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from sys import stdin, stderr, stdout
from io import StringIO, BytesIO
import os
import dis
def connect_to_snowfalke(**kwargs):
    return **kwargs


class T:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def put(self):
        return f"Hello World: {self.x}"


t = T(12, 13)
print(t.put())


def hello_world():
    return "Hello World coool Mr Santosh!!!"


if __name__ == "__main__":
    print(hello_world())
