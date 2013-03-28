def is_valid(str):
	if (str.count('$') != str.count(';')):
		return '$Q.ERRTRP=1'
	elif (str.count('\'') % 2 != 0):
		return '$Q.ERRTRP=2'
	elif (str.count('\"') % 2 != 0): 
		return '$Q.ERRTRP=3'
	elif ((str.count('$') == 0) or (str.count(';') == 0)):
		return 'invalid string'

test = [''' $A.K='0108';$A.KOID=1;$A.NM='Слесарная';$A.NTD='ИОТ N 43';$A.OBD='БЛ 60188.15512  БЛ 20188.05398';$A.PROF='18466';$A.RNOK='15512';$A.SD=2;$A.SDT='С переходами в маршрутной карте';$A.TO='Безопасные приемы работы согласно инструкции N° 521';$E.VO='2821-0051 Напильник ГОСТ 1465-69   (1)  ';$H.VO='013000 Тара   (1)  ';$N.TOA=2.128;$N.TST=3.328;$N.TWA=1.2; ''',
'''$L.K=99;$L.ST='Бл 0482-4123';$P.KWO='777';$P.TXT='"Форма литья "$L.ST//';$P.WO='Пpоизвольные';''',
''' Форма литья Бл 0482-4123''',
'''$E.IST='ГОСТ 1465-69';$E.NM='Напильник';$E.OB='2821-0051';$E.TXT='2821-0051 Напильник ГОСТ 1465-69 ';$H.NM='Тара';$H.OB='013000';$H.TXT='013000 Тара ';$L.K=99;$L.ST='0,2';$P.KWO='137';$P.TXT='"Запилить и зачистить литье с притуплением острых кромок до " $L.ST//';$P.WO='Запилить';''',
'''$H.NM2='Подкладки';$H.NM='Тиски';$H.OB='БЛ 7201-4008';$H.TXT2='Подкладки ';$H.TXT='БЛ 7201-4008 Тиски ';$L.K=99;$P.KWO='091';$P.TXT='"Установить и снять деталь " $L.ST//';$P.WO='Установить';''']


for x in test:
	print(is_valid(x))