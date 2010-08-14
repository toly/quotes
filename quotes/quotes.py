# -*- coding: utf-8

import string
import urllib
import re

# грузим базу котировок (с заданным интервалом)
def make_data_quotes(folder, qlist, interval, period):
	df, mf, yf, dt, mt, yt = period
	symbols = get_symbols(qlist)
	i, n  = 0, len(symbols)
	for symb in symbols:
		i += 1
		q = quote(interval, int(symb[0]))
		print 'Загружаем', symb[1], ' (', i, 'из', n, ')'
		q.load_quotes(df, mf, yf, dt, mt, yt)
		q.save(folder + symb[0] + '_' + str(interval) + '.csv')


# определяем наименование акции по ее "финамовскому" номеру
def get_symb_name(symbols, number):
	res = ''
	for symb in symbols:
		if int(symb[0]) == number:
			res = symb[1]
			break
	return res

# загрузка соответствий "финамовский номер" - "название акции"
def get_symbols(fname):
	f = open(fname, 'r')
	txt = f.read()
	f.close()
	symbols = re.findall(r'<a href="/analysis/charts/default.asp\?id=([^"]+)" target=_blank>([^<]+)</a>', txt)
	return symbols

# загрузка котировок
def get_quotes(df, mf, yf, dt, mt, yt, symb, period):
    f = urllib.urlopen('http://195.128.78.52/GAZP_080201_100208.txt?d=d&market=1&em=' +
        str(symb)+'&df='+str(df)+'&mf='+str(mf)+'&yf='+str(yf)+'&dt='+str(dt)+'&mt='
        +str(mt)+'&yt='+str(yt)+'&p='+str(period)
       	+'&f=GAZP_080201_100208&e=.txt&cn=GAZP&dtf=4&tmf=4&MSOR=0&sep=1&sep2=1&datf=5&at=1')
    quot = f.read()
    return string.split(quot, '\n')[1:-1]

# класс quote - котировки
class quote(object):
	# инициализация: по умолчанию грузим газпром часовик
	# обозначения периодов 1 - тики, 2 - минуты, 3 - 5 минут, 7 - 1 час, 8 - день
	def __init__(self, period=7, symb=16842):
		# "сырые" данные которовок - массив строк
		self.raw_data = []
		# развернутые данные - open, high, low, close, volume
		self.op, self.hi, self.lo, self.cl, self.vol = [], [], [], [], []
		# номер торгового инструмента (по финаму)
		self.symb = symb
		# период
		self.period = period
	
	# распаковка "сырых" данных
	def decomp(self):
		self.op, self.hi, self.lo, self.cl, self.vol = [], [], [], [], []
		for line in self.raw_data:
			mix = string.split(line, ',')[2:7]
			self.op.append(float(mix[0]))
			self.hi.append(float(mix[1]))
			self.lo.append(float(mix[2]))
			self.cl.append(float(mix[3]))
			self.vol.append(int(mix[4]))
	
	# грузим котировки из инета
	def load_quotes(self, df, mf, yf, dt, mt, yt):
		self.raw_data = get_quotes(df, mf, yf, dt, mt, yt, self.symb, self.period)
		self.decomp()

	# записываем котировки в файл (сырые)
	def save(self, fname):
		f = open(fname, 'w')
		for line in self.raw_data:
			f.write(line+'\n')
		f.close()

	# грузим "сырые" котировки из файла
	def load(self, fname):
		f = open(fname, 'r')
		quot = f.read()
		f.close()
		self.raw_data = string.split(quot, '\n')[:-1]
		self.decomp()

	
