c = raw_input()

for i in range(0,int(c)):
	d,n = raw_input().split(' ')
	input = raw_input().split(' ')
	count = 0
	for k in range(0, int(n)):
		sum = 0
		skipk = 0
		for j in input:
			if (skipk >= k):
				sum = sum + int(j)
				if sum % int(d) == 0:
					count = count+1
			skipk = skipk + 1
	print count