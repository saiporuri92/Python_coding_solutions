# Sample input: "ZXVVYZW", "XKYKZPW"
# Sample output: ["X", "Y", "Z", "W"]
def longestCommonSubsequence(str1, str2):
    # Write your code here.
	matrix = [["" for i in range(len(str2)+1)] for j in range(len(str1)+1)]
	
	for row in range(len(str1)):
		for col in range(len(str2)):
			if str1[row] == str2[col]:
				matrix[row+1][col+1] = matrix[row][col] + str1[row]
			else:
				if len(matrix[row+1][col]) >= len(matrix[row][col+1]):
					matrix[row+1][col+1] = matrix[row+1][col]
				else:
					matrix[row+1][col+1] = matrix[row][col+1]
	return list(matrix[-1][-1])