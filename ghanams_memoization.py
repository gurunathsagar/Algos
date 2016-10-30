#!/usr/bin/python
import sys, time, ast

def matrixMultMemoization(numbers, i, j, matrix):

	global recCount
	n = len(numbers)

	if i == j:
		return 0

	if matrix[i][j] < sys.maxint:
		return matrix[i][j]

	val = sys.maxint

	for k in range(i, j):
		temp = matrixMultMemoization(numbers, i, k, matrix) + matrixMultMemoization(numbers, k+1, j, matrix) + numbers[i-1]*numbers[k]*numbers[j]
		recCount = recCount + 2
		if temp < val:
			val = temp
			matrix[i][j] = temp

	return val

print "Memoization\n"
recCount = 0
numbers = ast.literal_eval(sys.argv[1])
n = len(numbers)
matrix = [[sys.maxint for y in range(n)] for x in range(n)]
start = time.time()
print "Total number of calculations ", matrixMultMemoization(numbers, 1, len(numbers)-1, matrix)
end = time.time()
print  "Recursive Call count = ", recCount, " Elapsed time = ", (end-start)*1000, "ms"
