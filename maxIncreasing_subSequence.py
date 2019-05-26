#get the maximum subarray sequence that gives the maximum sum
def maxSumIncreasingSubsequence(array):
    # Write your code here.
	maxi = -float('inf')
	mindex = 0
	mapp = {}
	for i,v in enumerates(array):
		mapp[i] = [v,[v]]
	for i in range(1,len(array)):
		j = i-1
		while(j >= 0):
		    if array[j] < array[i]:
				if mapp[j][0] + array[i] > mapp[i][0]:
			   		mapp[i][0] = mapp[j][0] + array[i]
			   		mapp[i][1] = mapp[j][1] + [array[i]]
				if mapp[i][0] > maxi:
					maxi = mapp[i][0]
					mindex = i
			j -= 1
	return mapp[mindex]
