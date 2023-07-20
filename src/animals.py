#!/usr/bin/env python3

from z3 import *

def main():
    dog, cat, mouse = Ints("dog cat mouse")
    solve(dog >= 1, cat >= 1, mouse >= 1, dog + cat + mouse == 100, dog * 1500 + cat * 100 + mouse * 25 == 10000)

if __name__ == "__main__":
    main()
