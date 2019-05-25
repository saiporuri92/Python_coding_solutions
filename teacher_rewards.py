# Imagine that you're a teacher who's just 
# graded the final exam in a class. You have a
#  list of student scores on the final exam in a particular order 
# (not necessarily sorted), and you want to reward your students. 
# You decide to do so fairly by giving them arbitrary rewards following two rules: 
# first, all students must receive at least one reward; 
# second, any given student must receive strictly more rewards than an adjacent student 
# (a student immediately to the left or to the right) with a lower score and must receive 
# strictly fewer rewards than an adjacent student with a higher score.
#  Assume that all students have different scores; in other words, the scores are all unique.
#  Write a function that takes in a list of scores and returns the minimum 
# number of rewards that you must give out to students, all the while satisfying the two rules.
def minRewards(scores):
    # Write your code here.
	result = [1] * len(scores)
	for i,v in enumerate(scores):
		if i == 0:
			continue
		if v > scores[i-1]:
			result[i] = result[i-1] + 1
	for j in range(len(scores)-2,-1,-1):
		if scores[j] > scores[j + 1]:
			result[j] = max(result[j],result[j+1]+1)
	return sum(result)