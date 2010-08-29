# -*- coding: utf-8
import time
# подгружаем библиотеки
from quotes.ekonom import * 
#import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from pylab import *

# начальные параметры
folder = 'data/'
qlist = 'quotes/mmvb.txt'
interval = 8

# финамовский номер газпрома
fnum = 16842

# загружаем котировки Газпрома из локальной базы
q = quote(interval,  fnum)
q.load(folder + str(q.symb) + '_' + str(interval) + '.csv')

# цены закрытия
x = q.cl

# функция вычисления СКО
# на вход подаются два массива одинаковой длинны
def RMS(a, b):
    s = 0.
    for i in xrange(len(a)):
        s += (a[i] - b[i]) ** 2
    return (s/len(a)) ** 0.5

param, err = [], []
# меняем коэффициент сглаживания от 0 до 1 с шагом 0.02
for i in xrange(50):
    a = float(i)/50.
    y = q.EMA(a)
    param.append(a)
    err.append(RMS(x, y))

# строим график
plt.plot(param, err)
plt.show()
