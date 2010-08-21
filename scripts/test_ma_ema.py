# -*- coding: utf-8

# подгружаем библиотеки
from quotes.ekonom import * 
import matplotlib.pyplot as plt

# начальные параметры
folder = 'data/'
qlist = 'quotes/mmvb.txt'
interval = 8

# финамовский номер газпрома
fnum = 16842

# загружаем котировки Газпрома из локальной базы
q = quote(interval,  fnum)
q.load(folder + str(q.symb) + '_' + str(interval) + '.csv')

# формируем массивы цен закрытия,
# скользящих средних и экспоненциальных 
cl = q.hi[:100]
#ma7 = q.MA()
ema01 = q.MA()[:100]
ema03 = q.MA(14)[:100]
ema05 = q.MA(21)[:100]


# выводим на график
plt.plot(cl, label = 'Close price')
#plt.plot(ma7, label = 'MA, T=7')
plt.plot(ema01, label='MA, T=7')
plt.plot(ema03, label='MA, T=14')
plt.plot(ema05, label='MA, T=21')

plt.legend(loc='upper left')
plt.show()
