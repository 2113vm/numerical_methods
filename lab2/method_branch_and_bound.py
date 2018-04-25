# -*- coding: cp1251 -*-
# импортируем функции PuLP
from pulp import *

# Создаем новую задачу Линейного программирования (LP) с максимизацией целевой функции
prob = LpProblem("Knapsack problem", LpMinimize)

# Переменные оптимизации, целые
x1 = LpVariable("x1", 0, 10, 'Integer')
x2 = LpVariable("x2", 0, 10, 'Integer')
x3 = LpVariable("x3", 0, 10, 'Integer')

prob += 21*x1 + 35*x2 + 50*x3, "obj"
prob += 2.5*x1 + 5*x2 + 10*x3 <= 40
prob += 2.5*x1 + 5*x2 + 10*x3 >= 35

prob.solve()

# Выводим статус задачи
print("Status:", LpStatus[prob.status])

# Выводим получившиеся оптимальные значения переменных
for v in prob.variables():
    print(v.name, "=", v.varValue)

# Выводим оптимальное значение целевой функции
print("objective = %s$" % value(prob.objective))
