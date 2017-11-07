def count_letters(word, char):
	lWord = str.lower(word)
	lChar = str.lower(char)
	counter = 0
	for c in lWord:
		if lChar == c:
			counter += 1
	return counter
	

word = str(raw_input("Masukkan Kalimat / Kata : "))
char = str(raw_input("Masukkan Karakter yang ingin dicari : "))

print "Jumlah huruf " + char + " Pada Kalimat " + word + " adalah " + str(count_letters(word, char))
  

