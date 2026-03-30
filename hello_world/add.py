import secrets
from collections import Counter, ChainMap, defaultdict, deque, OrderedDict, UserDict, UserList, UserString
from operator import add, itemgetter
from functools import partial, partialmethod, reduce, cache, cached_property, cmp_to_key
import os
import sys
import subprocess
from sys import stdin, stderr, stdout
from concurrent.futures import ThreadPoolExecutor, as_completed
from concurrent.futures import ProcessPoolExecutor
from asyncio import run
import argparse
from enum import Enum
import json
import signal
from contextlib import contextmanager
class Color(Enum):
    pass


def main() -> None:
    nums = [int(x) for x in input().split()]
    return nums


if __name__ == "__main__":
    print(main())
