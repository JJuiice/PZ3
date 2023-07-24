#!/usr/bin/env python3

from z3 import *

def bitvec(sudoku_i):
    # I believe this solution can be further optimized by treatings cells as bitvalues with offsets for access

    # 9x9 BitVecVals matrix
    X = [ [ BitVec("x_%s_%s" % (i+1, j+1), 4) for j in range(9) ] for i in range(9) ]

    # Each cell contains a value between 1 and 9
    cells_c = [ And(ULE(BitVecVal(1, 4), X[i][j]), ULE(X[i][j], BitVecVal(9, 4))) for i in range(9) for j in range(9) ]

    # Row constraint for distinct digits between all cells in row
    rows_c = [ Distinct(X[i]) for i in range(9) ]

    # Column constraint for distinct digits between all cells in column
    cols_c = [ Distinct([ X[i][j] for i in range(9) ]) 
               for j in range(9) ]

    # 3x3 Square constraint for distinct digits between all cells
    sq_c = [ Distinct([ X[3*i0 + i][3*j0 + j] 
                        for i in range(3) for j in range(3) ]) 
                    for i0 in range(3) for j0 in range(3) ]

    # All constraints in DNF
    sudoku_c = cells_c + rows_c + cols_c + sq_c

    # Sudoku instance constraint
    instance_c = [ If(sudoku_i[i][j] == BitVecVal(0, 4),
                    True,
                    X[i][j] == sudoku_i[i][j])
                   for i in range(9) for j in range(9) ]

    s = Solver()
    s.add(sudoku_c + instance_c)
    if s.check() == sat:
        m = s.model()
        r = [ [ m.evaluate(X[i][j]) for j in range(9) ]
              for i in range(9) ]
        print_matrix(r)
    else:
        print("Unsatisfiable")

def ints(sudoku_i):
    # 9x9 Ints matrix
    X = [ [ Int("x_%s_%s" % (i+1, j+1)) for j in range(9) ] for i in range(9) ]

    # Each cell contains a value between 1 and 9
    cells_c = [ And(1 <= X[i][j], X[i][j] <= 9) for i in range(9) for j in range(9) ]

    # Row constraint for distinct digits between all cells in row
    row_c = [ Distinct(X[i]) for i in range(9) ]

    # Column constraint for distinct digits between all cells in column
    cols_c = [ Distinct([ X[i][j] for i in range(9) ]) 
              for j in range(9) ]

    # 3x3 Square constraint for distinct digits between all cells
    sq_c = [ Distinct([ X[3*i0 + i][3*j0 + j] 
                        for i in range(3) for j in range(3) ]) 
                    for i0 in range(3) for j0 in range(3) ]
    
    # All constraints in DNF
    sudoku_c = cells_c + row_c + cols_c + sq_c

    # Sudoku instance constraint
    instance_c = [ If(sudoku_i[i][j] == 0,
                    True,
                    X[i][j] == sudoku_i[i][j])
                   for i in range(9) for j in range(9) ]
                
    s = Solver()
    s.add(sudoku_c + instance_c)
    if s.check() == sat:
        m = s.model()
        r = [ [ m.evaluate(X[i][j]) for j in range(9) ]
              for i in range(9) ]
        print_matrix(r)
    else:
        print("Unsatisfiable")


if __name__ == "__main__":
    # Sudoku instance
    instance_ints = ((0, 2, 6, 0, 0, 0, 8, 1, 0),
                     (3, 0, 0, 7, 0, 8, 0, 0, 6),
                     (4, 0, 0, 0, 5, 0, 0, 0, 7),
                     (0, 5, 0, 1, 0, 7, 0, 9, 0),
                     (0, 0, 3, 9, 0, 5, 1, 0, 0),
                     (0, 4, 0, 3, 0, 2, 0, 5, 0),
                     (1, 0, 0, 0, 3, 0, 0, 0, 2),
                     (5, 0, 0, 2, 0, 4, 0, 0, 9),
                     (0, 3, 8, 0, 0, 0, 4, 6, 0))

    instance_bv = [ [ BitVecVal(instance_ints[i][j], 4) for j in range(9) ] for i in range(9) ]

    print("BitVec Solution: ")
    bitvec(instance_bv)
    print("Ints Solution: ")
    ints(instance_ints)
