import time
import random

from data import flights, peoples

"""
Планирование путешествия группы людей, которые, отправляясь из разных мест, 
должны прибыть в одно и то же место.

Люди эти живут в разных концах страны и хотят встретиться в определенном месте.
Все они должны вылететь в один день и в один день улететь и при этом в 
целях экономии хотели бы уехать из аэропорта
и приехать в него на одной арендованной машине.
Ежедневно, в город места назначения, из мест проживания этих людей отправляются десятки рейсов,
все в разное время.

Цена билета и время в пути для каждого рейса разные.

Даны расписания рейсов из каждого искомого города до общего места назначения.
Необходимо расчитать минимальную общую цену с помощью алгоритма случайного поиска

Программа уже написана(я же обещал упростить условия))). Нужно распараллелить алгоритм с 
помощью питоновских библиотек(гугл в помощь) и сравнить с однопоточной версией
"""


# место назначения
destination = 'LGA'


def random_optimize(domain, costf):
    best = 999999999
    bestr = None

    for i in range(0, 1000):
        # Выбрать случаиное решение
        r = [random.randint(0, domain[i]) for i in range(len(domain))]

        # Get the cost
        cost = costf(r)

        # Сравнить со стоимостью наилучшего наиденного к этому моменту решения
        if cost < best:
            best = cost
            bestr = r
    return r, best


def get_minutes(t):
    x = time.strptime(t, '%H:%M')
    return x[3] * 60 + x[4]


def schedule_cost(sol):
    totalprice = 0
    latestarrival = 0
    earliestdep = 24 * 60

    for d in range(int(len(sol) / 2)):
        # Получить список прибывающих и убывающих реисов
        origin = peoples[d][1]
        outbound = flights[(origin, destination)][int(sol[d])]
        returnf = flights[(destination, origin)][int(sol[d + 1])]

        # Полная цена равна сумме цен на билет туда и обратно
        totalprice += outbound[2]
        totalprice += returnf[2]

        # Находим самыи позднии прилет и самыи раннии вылет
        if latestarrival < get_minutes(outbound[1]): latestarrival = get_minutes(outbound[1])
        if earliestdep > get_minutes(returnf[0]): earliestdep = get_minutes(returnf[0])

    # Все должны ждать в аэропорту прибытия последнего участника группы.
    # Обратно все прибывают одновременно и должны ждать свои реисы.
    totalwait = 0
    for d in range(int(len(sol) / 2)):
        origin = peoples[d][1]
        outbound = flights[(origin, destination)][int(sol[d])]
        returnf = flights[(destination, origin)][int(sol[d + 1])]
        totalwait += latestarrival - get_minutes(outbound[1])
        totalwait += get_minutes(returnf[0]) - earliestdep

        # Для этого решения требуется оплачивать дополнительныи день аренды?
    # Если да, это обоидется в лишние $50!
    if latestarrival > earliestdep:
        totalprice += 50

    return totalprice + totalwait


domain = []
for people in peoples:
    domain.append(len(flights[(people[1], destination)]) - 1)
    domain.append(len(flights[(destination, people[1])]) - 1)
print(domain)

result, score = random_optimize(domain, schedule_cost)
print(result, score)
