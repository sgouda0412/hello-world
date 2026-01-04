#!/usr/bin/env python3

from numpy import array
import os
import sys
from collections import Counter, defaultdict, deque, UserDict
from datetime import datetime, timedelta, timezone

class T:
    def __init__(self, x):
        self.x = x

    def _x(self):
        return "hello"


def main():
    """Main function to demonstrate the T class."""
    t = T(1)
    print(t._x())
    return "Hello"


if __name__ == "__main__":
    main()
