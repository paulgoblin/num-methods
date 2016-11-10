from sys import float_info

eps = float_info.epsilon

# calculates slope of f(x) at x = center
def _diff(fn, center, h=1e8*eps):
    dy = fn(center+h) - fn(center-h)
    dx = 2*h
    return dy/dx


def newton_raphson(fn, start, lim=1e8*eps, stepLimit=1e2):
    x = start
    y = fn(x)
    step = 0

    while abs(y) > lim and step < stepLimit:
        print('STEP', step, '(x, y) =', round(x, 3), ',', round(y, 3), '\n')
        dy = _diff(fn, x)
        x = x - y/dy
        y = fn(x)
        step += 1
    if step == stepLimit:
        raise Exception('newton_raphson could not converge')
    print('Found root at', x, 'with error', fn(x))
    return x
