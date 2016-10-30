#!/usr/bin/python
import sys, time, ast, pprint

def matrixMult(numbers, matrix, dire):

	n = len(numbers)
	for i in range(n-2, 0, -1):
		for j in range(i+1, n):
			if i!=j:
				matrix[i][j] = sys.maxint
				for k in range(i, j):
					temp = matrix[i][k]+matrix[k+1][j]+numbers[i-1]*numbers[k]*numbers[j]
					if temp < matrix[i][j]:
						matrix[i][j] = temp
						dire[i][j] = k

	pprint.pprint(dire)
	return matrix[1][n-1]

print "DP\n"
recCount = 0
numbers = ast.literal_eval(sys.argv[1])
n = len(numbers)
matrix = [[0 for y in range(n)] for x in range(n)]
dire = [[0 for y in range(n)] for x in range(n)]
start = time.time()
print "Total number of calculations = \n", matrixMult(numbers, matrix, dire)
end = time.time()
print "Time elapsed = ", (end-start)*1000, "Recursive Calls = ", 0