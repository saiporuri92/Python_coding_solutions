#[0, 100, 0, 0, 10, 1, 1, 10, 1, 0, 1, 1, 0, 100]
def waterArea(heights):
    # Write your code here.
	leftmax = 0
	leftarray = [0 for j in range(len(heights))]
	for i in range(lsen(heights)):
		leftarray[i] = leftmax
		if heights[i] > leftmax:
			leftmax = heights[i]
	
	rightmax = 0
	rightarray = [0 for j in range(len(heights))]
	for i in range(len(heights)-1,-1,-1):
		rightarray[i] = rightmax
		if heights[i] > rightmax:
			rightmax = heights[i]
	
	water = 0
	for pillar in range(1,len(heights)):
		rem = min(leftarray[pillar],rightarray[pillar]) - heights[pillar]
		if rem > 0:
			water += rem
	return water

waterArea([0, 100, 0, 0, 10, 1, 1, 10, 1, 0, 1, 1, 0, 100])