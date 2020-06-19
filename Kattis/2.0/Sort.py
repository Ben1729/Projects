from collections import Counter

n, c  = input().split()

nums = input().split()

l = []
numFreqArr = [0]*(int(c)+1)
for num in nums:
    if num not in l:
    numFreqArr[int(num)] += 1
    print(numFreqArr[int(num)])

sorted(numFreqArr)
s = ""
g = 0
for num in range(1,int(c)+1):
    for x in range(numFreqArr[num]):
        s = s + str(num)
    
print(s)
