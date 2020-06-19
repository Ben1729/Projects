n, h, v = input().split()

n = int(n)
h = int(h)
v = int(v)

nums = [n - h, h, n - v, v]

nums = sorted(nums)

print(nums[2]*nums[3]*4)