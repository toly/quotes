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

# изменяем параметры от 0.2 до 1 с шагом 0.005
da, db = 0.005, 0.005
a = arange(.2, 1.0, da)
b = arange(.2, 1.0, db)
A, B = meshgrid(a, b)

# функция вычисления ошибки при заданных параметрах
def err(a, b):
    global x, q
    y = q.halt(a, b)
    return RMS(x, y)

# вычисляем ошибки для всех комбинаций параметров
E = err(A, B)

# рисуем
axis([0.2, 1., 0.2, 1.])
pcolor(A, B, E)
colorbar()
show()
