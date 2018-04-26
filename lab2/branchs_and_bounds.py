"""
решить задачу с помощью метода ветвей и границ
# f = 17*x1 + 30*x2 + 75*x3;
# f -> min;
# g1 = 1.0*x1 + 2.2*x2 + 4*x3 <= 15;
# g2 = 1.0*x1 + 2.2*x2 + 4*x3 >= 13;
"""

from pulp import *

prob = LpProblem("Knapsack problem", LpMinimize)

x1 = LpVariable("x1", 0, 10, 'Integer')
x2 = LpVariable("x2", 0, 10, 'Integer')
x3 = LpVariable("x3", 0, 10, 'Integer')

prob += 17*x1 + 30*x2 + 75*x3, 'obj'
prob += 1.0*x1 + 2.2*x2 + 4*x3 <= 15
prob += 1.0*x1 + 2.2*x2 + 4*x3 >= 13
prob.solve()

print("Status:", LpStatus[prob.status])

for v in prob.variables():
    print(v.name, "=", v.varValue)

print("objective = %s$" % value(prob.objective))
