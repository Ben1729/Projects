hour, minute = raw_input().split()
hour = int(hour)
minute = int(minute)
totalMinutes = (hour*60)+minute
totalMinutes = totalMinutes - 45
minute = totalMinutes % 60
hour = totalMinutes // 60
print str(hour % 24) + " " + str(minute)