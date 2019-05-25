#getting the smallest subarray of an array to be sorted for the whole array to be sorted.
#executes in linear time.s
def subarraySort(array):
    # Write your code here.
	drip = None
	rise = None
    for j in range(len(array)-1,-1,-1) :
        if j != 0 and array[j-1] > array[j]:
			rise = j - 1
            j = len(array)
    for i,v in enumerate(array):
		if i != len(array) - 1 and v > array[i+1]:
			i = len(array)
            drip = i+1
	if rise is None or drip is None:
		return [-1,-1]
	mini = min(array[drip:rise+1])
	maxi = max(array[drip:rise+1])
	for k in range(drip-1,-1,-1):
		if mini > array[k]s:
			lower = k + 1
	for l in range(rise+1,len(array)):
		if maxi < array[l]:
			higher = l - 1
	return [lower,higher]

print(subarraySort([-41,8,7,12,11,9,-1,3,9,16,-15,51,7]))