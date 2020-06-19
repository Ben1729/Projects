total = 0
for x in range(int(raw_input())):
    P = int(raw_input())
    n = P / 10
    p = P % 10
    total += pow(n, p)
print total