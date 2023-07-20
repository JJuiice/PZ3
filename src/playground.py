from z3 import *

# Tie, Shirt = Bools('Tie Shirt')
# s = Solver()
# s.add(Or(Tie, Shirt),
#       Or(Not(Tie), Shirt),
#       Or(Not(Tie), Not(Shirt)))
# print(s.check())
# print(s.model())

# Z = IntSort()
# f = Function('f', Z, Z)
# x, y, z = Ints('x y z')
# A = Array('A', Z, Z)
# fml = Implies(x + 2 == y, f(Store(A, x, 3)[y - 2]) == f(y - x + 1 ))
# solve(Not(fml))

x = BitVec('x', 32)
powers = [ 2**i for i in range(32) ]
fast = And(x != 0, x& (x - 1) == 0)
slow = Or([ x == p for p in powers ])
print(fast)
prove(fast == slow)
print("trying to prove buggy version...")
fast = x & (x - 1) == 0
prove(fast == slow)

