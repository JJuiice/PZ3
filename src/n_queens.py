#!/usr/bin/env python3

from z3 import *

def queens(n):
    Q = [Int('Q_%i' % (i + 1)) for i in range(n)]

    val = [And(1 <= Q[i], Q[i] <= n) for i in range(n)]
    col = [Distinct(Q)]
    diag = [If(i == j, True, And(Q[i] - Q[j] != i - j, Q[i] - Q[j] != j - i)) for i in range(n) for j in range(i)]

    sol = Solver()
    sol.add(val + col + diag)

    num_solutions = 0
    while sol.check() == sat:
        mod = sol.model()
        ss = [mod.evaluate(Q[i]) for i in range(n)]
        print(ss)
        num_solutions += 1
        sol.add(Or([Q[i] != ss[i] for i in range(n)]))

    print("Number of Solutions: ", num_solutions)

if __name__ == "__main__":
    queens(4)
