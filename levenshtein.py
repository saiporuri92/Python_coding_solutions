def levenshteinDistance(str1, str2):
    # Write your code here.
    #creating a matrix intializing as 
	matrix = [[i for i in range(len(str2)+1)] for j in range(len(str1)+1)]
	#putting all the column first digits to the order
    for i in range(len(matrix)):
		matrix[i][0] = i
	for row in range(1,len(str1)+1):
		for col in range(1,len(str2)+1):
			if str1[row-1] == str2[col-1]:
				matrix[row][col] = matrix[row-1][col-1]
			else:
				matrix[row][col] = 1 + min(matrix[row-1][col], matrix[row][col-1],
									   		matrix[row-1][col-1])
	return matrix[-1][-1]

print(levenshteinDistance("xabc",'abcx'))