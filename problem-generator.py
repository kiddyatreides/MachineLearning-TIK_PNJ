import random

def generator(num):
	points = 0
	N = 1
	while(N <= num):
		print ""
		if(N == num):
			return "---------"
		else:
			x = str(random.randint(N+1,num))
			print "Jarak Kota Ke-" + str(N) + " Ke Kota " + str(x) + " adalah " + str(random.randint(1,10))
			print "Jarak Kota Ke-" + str(x) + " Ke Kota " + str(N) + " adalah " + str(random.randint(1,10))
		N = N + 1		
	return ""

print generator(5)