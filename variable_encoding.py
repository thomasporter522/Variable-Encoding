import math

def encode(s, final = True):
	if s == "": return str(int(not final))
	n = '{0:b}'.format(len(s))[1:]
	prefix = encode(n, False)
	return prefix + s + str(int(not final))

def decode(s, l=0):
	assert len(s) > l
	content = s[0:l]
	ended = s[l]
	s = s[l+1:]
	if ended == "0":
		assert len(s) == 0
		return content
	return decode(s, int("1"+content, 2))

def test():
	for i in range(10000):
		m = '{0:b}'.format(i)
		assert m == decode(encode(m))

print(encode(input(">>>")))

