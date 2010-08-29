def RMS(x, y):
    """ среднеквадратическая ошибка"""
    # если на вход даны массивы разной длины
    if len(x) != len(y):
        # ошибка
        return 0
    s = 0.
    for i in xrange(len(x)):
        s += (x[i] - y[i]) ** 2
    return (s/len(x)) ** 0.5
