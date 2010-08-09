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
