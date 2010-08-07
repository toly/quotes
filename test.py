# -*- coding: utf-8
# загружаем модуль quotes
import quotes.quotes as quotes

# каталог для хранения файлов котировок
folder = 'data/'
# файл с сайта "Финам"
qlist = 'quotes/mmvb.txt'
# выгребаем данные с 1.01.2009 по 31.12.2009
#df, mf, yf, dt, mt, yt = 1, 0, 2009, 31, 11, 2009
period = (1, 0, 2009, 31, 11, 2009)
# работаем с днями
interval = 8

# делаем локальную базу котировок
quotes.make_data_quotes(folder, qlist, interval, period)

'''symbols = quotes.get_symbols(qlist)
i, n  = 0, len(symbols)
for symb in symbols:
	i += 1
	q = quotes.quote(period, int(symb[0]))
	print 'Загружаем', symb[1], ' (', i, 'из', n, ')'
	q.load_quotes(df, mf, yf, dt, mt, yt)
	q.save(dir + symb[0] + '_' + str(period) + '.csv')'''



exit()

#------------------------------------------------

# файл сохраненный с сайта "Финам"
fname = 'quotes/mmvb.txt'
# получаем массив инструментов с номерами
symbols = quotes.get_symbols(fname)
# определяем инструмент с номером 16842 - Газпром
print quotes.get_symb_name(symbols, 16842)

#------------------------------------------------

# инициализируем объект класса quotes
# 8 - период сутки, по умолчанию ГАЗПРОМ
q = quotes.quote(8)

# период: с 1.01.2010 по 30.01.2010
# (напомню, нумерация месяцев здесь начинается с 0)
q.load_quotes(1, 0, 2010, 30, 0, 2010)

# выводим "сырые" данные
print q.raw_data

# вывод объемов по дням
print q.volume

# сохраняем котировки в файл
q.save('zzz.txt')

# делаем новый объект класса quotes
q2 = quotes.quote(8)

# загружаем котировки из только что сохраненного файла
q2.load('zzz.txt')

# выводим объемы по дням - все в норме
print q.volume
