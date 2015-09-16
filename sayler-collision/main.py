from HashChecker import HashChecker
from util import randomStr

NUM_INPUTS=100000000
STR_LEN_MIN=10
STR_LEN_MAX=12

if __name__ == "__main__":

	HC = HashChecker()

	# Random inputs of varying lengths
	for i in range(0, NUM_INPUTS):
		for j in range(STR_LEN_MIN, STR_LEN_MAX):
			HC.add(randomStr(j));
