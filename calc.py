#!/usr/bin/python

arr = [5,2,4,7,3,9,7,8,6,3,7,5,5]

#arr = [1,2,3,4,5]

s = 0

while len(arr) >= 3:
	s = s + (arr[0]*arr[1]*arr[2])
	arr = arr[:1] + arr[2:]

print s