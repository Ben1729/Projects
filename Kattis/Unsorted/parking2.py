prices = input().split()
total = [0] * 100
ans = 0
for i in range(3):
    truck = input().split()
    for j in range(int(truck[0]), int(truck[1])):
        total[j] += 1

for i in total:
    if i != 0:
        ans += int(prices[i - 1]) * i
print(ans)