# -*- coding: utf-8

import string
import urllib

# загрузка котировок
def get_quotes(df, mf, yf, dt, mt, yt, simb, period):
    f = urllib.urlopen('http://195.128.78.52/GAZP_080201_100208.txt?d=d&market=1&em=' +
        str(simb)+'&df='+str(df)+'&mf='+str(mf)+'&yf='+str(yf)+'&dt='+str(dt)+'&mt='
        +str(mt)+'&yt='+str(yt)+'&p='+str(period)
       	+'&f=GAZP_080201_100208&e=.txt&cn=GAZP&dtf=4&tmf=4&MSOR=0&sep=1&sep2=1&datf=5&at=1')
    quot = f.read()
    return string.split(quot, '\n')[1:-1]

# класс quote - котировки
class quote(object):
	# инициализация: по умолчанию грузим газпром часовик
	# обозначения периодов 1 - тики, 2 - минуты, 3 - 5 минут, 7 - 1 час, 8 - день
	def __init__(self, period=7, simb=16842):
		# "сырые" данные которовок - массив строк
		self.raw_data = []
		# развернутые данные - open, high, low, close, volume
		self.open, self.high, self.low, self.close, self.volume = [], [], [], [], []
		# номер торгового инструмента (по финаму)
		self.simb = simb
		# период
		self.period = period
	
	# распаковка "сырых" данных
	def decomp(self):
		self.open, self.hight, self.low, self.close, self.volume = [], [], [], [], []
		for line in self.raw_data:
			mix = string.split(line, ',')[2:7]
			self.open.append(float(mix[0]))
			self.high.append(float(mix[1]))
			self.low.append(float(mix[2]))
			self.close.append(float(mix[3]))
			self.volume.append(int(mix[4]))
	
	# грузим котировки из инета
	def load_quotes(self, df, mf, yf, dt, mt, yt):
		self.raw_data = get_quotes(df, mf, yf, dt, mt, yt, self.simb, self.period)
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

	
