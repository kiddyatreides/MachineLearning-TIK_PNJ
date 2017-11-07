import math
import numpy as np
import pandas as pd
import quandl
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression

#import matplotlib dan stylenya
import datetime
import arrow
import matplotlib.pyplot as plt
from matplotlib import style

'''def minggu1():
	df = quandl.get("WIKI/GOOGL")
	df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
	df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Close']
	df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
	df = df[['Adj. Close', 'HL_PCT', 'Adj. Volume']]
	 
	print('nilai df awal:*')
	print()
	print(df.head())'''
	


def minggu2():

	"""
	Dibagian ini kita akan memanggil fungsi quandl untuk mengambil data saham dari GOOGLE. lalu data tersebut 
	akan diambil sesuai label yang ada di line 35. Lalu data tersebut dibuatkan label baru yaitu HL PCT dan dicari isinya sesuai rumusnya dalam pencariana data bredasarkan closing harga
	PCT Change berfungsi dalam perubahan data perhari.
	lalu akan di print sesuai keinginan yaitu adj close, hl pct dan adj volume.
	di print menggunakan df head karena hanya 5 data yang keluar agar ga kebanyakan
	"""
	df = quandl.get("WIKI/GOOGL")
	df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
	df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Close']
	df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
	df = df[['Adj. Close', 'HL_PCT', 'Adj. Volume', 'PCT_change']]
	


	print('nilai df awal yang ditampilkan dari Adj Close, HL PCT, ADJ Volume adalah:')
	print ""
	print(df.head())
	
	'''
	Disini kita akan mencoba meramal tentang saham, dibuat dulu atribut forecast col yang berisi data adj.close.
	Lalu dfffillna diisi value -9999 agar dapat menangani data yang kosong sehingga tidak crash.
	buat forecast out adalah rumus (gue juga gatau kenapa gini, dari sononya).
	'''
	
	forecast_col = 'Adj. Close'
	df.fillna(value=-999, inplace = True)
	forecast_out = int(math.ceil(0.01 * len(df)))
	
	
	'''
	Untuk ngelabelin harga, kita kasih dengan nama label. fungsinya untuk ngeramalin harga saham dari 100 hari (BACA PDF nya)
	dff dropna berarti ngilangin not a number (data yang missing)
	kalo udha x nya dibuat di pre proses pengskalaan.
	'''
	df ['label'] = df[forecast_col].shift(-forecast_out)
	df.dropna(inplace = True)
	X = np.array(df.drop(['label'], 1)) #di drop dulu label yang bernama label dan parameternya 1, karena data tersebut ada di axis satu (kalo digati pasti error, bawaan rumus)
	y = np.array(df['label'])
	X = preprocessing.scale(X)
	y = np.array(df['label'])
	
	'''
	disini dibuat banyak attribut. penglabelan diatas dilakukan validasi silang dan datanya di test dengan cara dipisah. Berapa banyak data yang ditest tergantung parameter test size
	'''
	X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)
	
	
	'''
	disini pengetesan dengan algoritma SVM SVR (GUE JG GATAU INI ALGORITMA APAAN)
	abis itu datanya yang akan di training di aktifkan (fit)
	abis itu buat ngeliat skor dari training akan digunakan hal sbg berikut (dprint)
	'''
	clf = svm.SVR()
	clf.fit(X_train, y_train)
	confidence = clf.score(X_test, y_test)
	print ""
	print "Nilai dari algoritma SVR"
	print(confidence) #0.806069791913
	print ""
	
	
	'''
	disini pengetesan dengan algoritma regresi linear
	abis itu datanya yang akan di training di aktifkan (fit)
	abis itu buat ngeliat skor dari training akan digunakan hal sbg berikut (dprint)
	'''
	'''clf = LinearRegression()
	clf.fit(X_train, y_train)
	confidence = clf.score(X_test, y_test)
	print "Nilai algoritma Linear Regression"
	print(confidence) #0.974549590614
	print ""'''
	
	
	'''
	disini pengetesan dengan algoritma regresi linear tapi dites pake berbagai method kaya linear, poly, rbf, sigmoid.
	abis itu datanya yang akan di training di aktifkan (fit)
	abis itu buat ngeliat skor dari training akan digunakan hal sbg berikut (dprint)
	'''
	clf = LinearRegression(n_jobs=-1)
	for k in ['linear','poly','rbf','sigmoid']:
		clf = svm.SVR(kernel=k)
		clf.fit(X_train, y_train)
		confidence = clf.score(X_test, y_test)
		print(k,confidence)
		
	print ""
	'''
	disini dites data yang belom ada targetnya.
	kenapa kaya gini? ini udah bawaan sananya jadi jangan tanya gue kenapa bisa begini.
	'''
	
	X = np.array(df.drop(['label'], 1))
	X = preprocessing.scale(X)
	X_lately = X[-forecast_out:]
	X = X[:-forecast_out]
	df.dropna(inplace=True)
	y = np.array(df['label'])
	
	#X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)
	
	
	'''
	dari data yang belom ada targetnya di tes lagi dan ditraining lagi
	'''
	'''clf = LinearRegression(n_jobs=-1)
	clf.fit(X_train, y_train)
	confidence = clf.score(X_test, y_test)
	print "Nilai dari algoritma linear regresi untuk data yang tidak ada target"
	print(confidence)
	print ""'''
	
	'''
	disini dari data saham tadi diprediksi berdasarkan X yang terakhir.
	'''
	
	clf = svm.SVR()
	clf.fit(X_train, y_train)
	confidence = clf.score(X_test, y_test)
	print ""
	print "Nilai dari algoritma SVR"
	print(confidence) #0.806069791913
	print ""
	
	forecast_set = clf.predict(X_lately)
	print "Data Prediksi saham:"
	print(forecast_set, confidence, forecast_out)
	print ""
	#print(df.head())
	
	
	'''
	supaya bisa nampilin grafik, kita pake fungsi plot dengan style ggplot (belom nyoba lagi style yang lain)
	'''
	style.use('ggplot') #style yang dipake yaitu ggplot (bawaan sononya)
	df['Forecast'] = np.nan #ini jelas untuk nambahin kolom baru dengan data not a number
	last_date = df.iloc[-1].name
	last_unix = (last_date - datetime.datetime(1970,1,1)).total_seconds() #waktu terakhir pas mau dibaca
	#last_unix = last_date.timestamp()
	one_day = 86400 #24 jam x 60 menit x 60 detik
	next_unix = last_unix + one_day #data yang akan diramal yaitu waktu terakhir + hari esok
	
	#ngelakuin looping supaya dapetin data seterusnya.
	for i in forecast_set:
		next_date = datetime.datetime.fromtimestamp(next_unix)
		next_unix += 86400
		df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)]+[i]
	
	'''
	yang di plot (tampilkan bentuk grafik) yaitu adj close sama forecast yang ditambahin kolom baru diatas.
	yang akan ditampilkan yaitu adj.close & forecast
	'''
	df['Adj. Close'].plot()
	df['Forecast'].plot()
	#df['label'].plot()
	#df['Adj. Volume'].plot()
	plt.legend(loc=4) #ngatur posisi legenda penulisan. 4 berarti dipinggir kanan
	plt.xlabel('Date') #x nya waktu
	plt.ylabel('Price') #y nya harga saham
	plt.show()	#tampilin
	

minggu2() #jalanin fungsi