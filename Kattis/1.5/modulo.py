nums = []
count = 0


for x in range(10):
    num = int(input())
    if (num % 42) not in nums:
        count += 1
        nums.append(num % 42)
    
print(count)
