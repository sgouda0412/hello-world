#!/usr/bin/env python3


class T:
    def __init__(self, x):
        self.x = x

    def _x(self):
        return "hello world"


def main():
    """Main function to demonstrate the T class."""
    t = T(1)
    print(t._x())
    return "Hello"


if __name__ == "__main__":
    main()
