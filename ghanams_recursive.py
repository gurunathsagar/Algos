#!/usr/bin/python
import sys, time, ast

def matrixMultRecursive(numbers, i, j):

	global recCount
	n = len(numbers)
	if i == j:
		return 0

	val = sys.maxint

	for k in range(i, j):
		temp = matrixMultRecursive(numbers, i, k) + matrixMultRecursive(numbers, k+1, j) + numbers[i-1]*numbers[k]*numbers[j]
		recCount = recCount + 2
		if temp < val:
			val = temp

	return val

print "Recursive\n"
recCount = 0
numbers = ast.literal_eval(sys.argv[1])	
start = time.time()
print "Total number of calculations ", matrixMultRecursive(numbers, 1, len(numbers)-1)
end = time.time()
print  "Recursive Call count = ", recCount, " Elapsed time = ", (end-start)*1000, "ms"
