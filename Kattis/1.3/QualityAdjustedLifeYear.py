totalQuality = 0
for ageRange in range(int(raw_input())):
    quality, years = raw_input().split()
    totalQuality += float(quality) * float(years)
print totalQuality



