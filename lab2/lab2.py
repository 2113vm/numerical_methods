# решить задачу с помощью метода ветвей и границ
# Пока почитайте про метод ветвей и границ и метод мультистарта
# f = 17*x1 + 30*x2 + 75*x3;
# f -> min;
# g1 = 1.5*x1 + 2.5*x2 + 6*x3 <= 20;
# g2 = 1.5*x1 + 2.5*x2 + 6*x3 >= 19;
#
# f = 20*x1 + 25*x2 + 80*x3;
# f -> min;
# g1 = 1.75*x1 + 2.0*x2 + 5.5*x3 <= 20;
# g2 = 1.75*x1 + 2.0*x2 + 5.5*x3 >= 20
#
# f = 17*x1 + 30*x2 + 75*x3;
# f -> min;
# g1 = 1.0*x1 + 2.2*x2 + 4*x3 <= 15;
# g2 = 1.0*x1 + 2.2*x2 + 4*x3 >= 13;
#
# f = 15*x1 + 40*x2 + 65*x3;
# f -> min;
# g1 = 1.0*x1 + 3.0*x2 + 4.5*x3 <= 25;
# g2 = 1.0*x1 + 3.0*x2 + 4.5*x3 >= 23;
#
# f = 12*x1 + 35*x2 + 76*x3;
# f -> min;
# g1 = 0.5*x1 + 1.5*x2 + 2*x3 <= 10;
# g2 = 0.5*x1 + 1.5*x2 + 2*x3 >= 9;
#
# f = 21*x1 + 35*x2 + 50*x3;
# f -> min;
# g1 = 2.5*x1 + 5*x2 + 10*x3 <= 40;
# g2 = 2.5*x1 + 5*x2 + 10*x3 >= 35;

import scipy
from scipy import optimize
import numpy as np


def multistart(func, ranges, niter=100, minimizer_kwargs=None, disp=False,
               niter_success=None, seed=None):
    ranges = np.asarray(ranges)

    # set up the np.random.RandomState generator
    rng = np.random.RandomState(seed)

    if minimizer_kwargs is None:
        minimizer_kwargs = dict()

    if niter_success is None:
        niter_success = niter + 2

    # Generate starting points uniformly within ranges
    samples = rng.rand(niter, len(ranges))
    samples = samples * (ranges[:, 1] - ranges[:, 0]) + ranges[:, 0]

    best_fun = float('inf')
    # TODO: Should initialize best_res with a dummy
    # in case none of the results are Valid

    best_n = None
    best_res = None

    for n, x0 in enumerate(samples):
        res = optimize.minimize(func, x0, **minimizer_kwargs)
        if res.success is not 'InvalidResult' and res.fun < best_fun:
            best_fun = res.fun
            best_res = res
            best_n = n
        if disp:
            print(n, x0, res.fun, best_fun)
        if n - best_n >= niter_success:
            if disp:
                print('No better minima found after', n - best_n,
                      'steps. Halting.')
            break
    if disp:
        print('Best minimum found on trial', best_n)

    return best_res


def fun():
    pass


if __name__ == '__main__':
    multistart()
