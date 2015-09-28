import hashlib;
from collections import defaultdict;

class HashChecker:
	# Dictionary for hashes based on list so we can store colliding
	hashes = defaultdict(list);
	SAYLER_LENGTH = 6;

	def getHash(self, str):
		# Use hashlib to generate a hash for a given string
		hasher = hashlib.md5();	
		hasher.update(str)
		hash = hasher.hexdigest()
		return hash;
	
	def getSaylerChars(self, hash):
		# Get first and last n digits n=SAYLER_LENGTH 
		out = hash[0:self.SAYLER_LENGTH]	
		out += hash[-self.SAYLER_LENGTH:32]
		return out;

	def add(self, str):
		# Main function, generates hash, grabs sayler chars, and then appends to list, checking if we have a collision
		hash = self.getHash(str)
		sayler_chars = self.getSaylerChars(hash)
		# Add hash to dictionary, mapping to original string
		self.hashes[sayler_chars].append(str)
		if len(self.hashes[sayler_chars]) > 1:
			print "Found collision - hash %s, printing colliding strings" % sayler_chars
			for s in self.hashes[sayler_chars]:
				print s
		

