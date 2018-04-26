"""
решить задачу с помощью метода ветвей и границ
f = 21*x1 + 35*x2 + 50*x3
f -> min
g1 = 2.5*x1 + 5*x2 + 10*x3 <= 40
g2 = 2.5*x1 + 5*x2 + 10*x3 >= 35

"""

from pulp import *

prob = LpProblem("Knapsack problem", LpMinimize)

x1 = LpVariable("x1", 0, 10, 'Integer')
x2 = LpVariable("x2", 0, 10, 'Integer')
x3 = LpVariable("x3", 0, 10, 'Integer')

prob += 21*x1 + 35*x2 + 50*x3, "obj"
prob += 2.5*x1 + 5*x2 + 10*x3 <= 40
prob += 2.5*x1 + 5*x2 + 10*x3 >= 35

prob.solve()

print("Status:", LpStatus[prob.status])

for v in prob.variables():
    print(v.name, "=", v.varValue)

print("objective = %s$" % value(prob.objective))
