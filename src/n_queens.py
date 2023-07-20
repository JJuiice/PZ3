#!/usr/bin/env python3

from z3 import *

def queens(n):
    # Since we know each queen must be in a different row, we'll see it as a given and only identify each queen by a column position
    Q = [Int('Q_%i' % (i + 1)) for i in range(n)]

    # Constrain each queen to a column number
    val = [And(1 <= Q[i], Q[i] <= n) for i in range(n)]
    # Make sure there is only 1 queen per column
    col = [Distinct(Q)]
    # Diagonal constraint
    diag = [If(i == j, 
               True, 
               And(Q[i] - Q[j] != i - j, Q[i] - Q[j] != j - i)) 
            for i in range(n) for j in range(i)]

    # Init solver and add all constraints
    sol = Solver()
    sol.add(val + col + diag)

    # Initialize the number of solutions to 0 and keep checking solver while model is satisfiable
    # If it is satisfiable, get the model for the last check and get the solutions for each queen
    # Print each solution set 
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
