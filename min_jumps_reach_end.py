def minNumberOfJumps(array):
    # Write your code here.
	booler = [float('inf') for _ in range(len(array))]
	booler[0] = 0
	for i in range(len(array)):
		for j in range(1,array[i]+1):
			l = i + j
			if l < len(booler):
				if booler[l] > booler[i] + 1:
					booler[l] = booler[i] + 1
	return booler[-1]

print(minNumberOfJumps([1,1,1]))