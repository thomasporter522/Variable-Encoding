import math

def log_b(n): return math.ceil(math.log(n,2))

def length(n):
	if n == 0: return 1
	if n == 1: return 3
	return 1+n+length(log_b(n+2)-1)

def to_string(s, final = True):
	if s == "": return "0"
	n = '{0:b}'.format(len(s))
	if n != "1"*len(n): n = n[1:]
	prefix = "1"
	if n != "1": prefix = to_string(n, False)
	return prefix + s + str(int(not final))
	
def efficiency():
	for i in range(24):
		print(2**i,length(2**i), length(2**i)/(2**i))
	
def test():
	for i in range(1000):
		if len(to_string("0"*i)) != length(i): 
			print(i,to_string("0"*i), length(i))

efficiency()
