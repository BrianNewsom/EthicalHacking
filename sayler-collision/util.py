import string
import random;

def randomStr(n):
	# see http://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python
	return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))	
