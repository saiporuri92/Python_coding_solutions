# Sample input: [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
# Sample output: 19 ([1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1])
def kadanesAlgorithm(array):
    # Write your code here.
	sumtil = 0
	maxum = -float('inf')
	for i in array:
		sumtil = max(i,sumtil + i)
		maxum = max(sumtil,maxum)
	return maxum
kadanesAlgorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4])