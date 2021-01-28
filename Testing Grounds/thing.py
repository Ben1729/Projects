accelerationList = [1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 0, 0, 0, 0, 0, 0, 0, 0, -0.833, -4.5, -4.5, -3.667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 0, -0.846, -4, -4, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 0, -2.345, -4.5, -4.5, -2.309, 0, 0, 0, 0, 0, 0, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -0.5, -3.375, -4.5, -4.5, -0.625, 0, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 0, -0.846, -4, -4, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 0, -2.345, -4.5, -4.5, -2.309, 0, 0, 0, 0, 0, 0, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, -0.5, -2.51, -4.5, -4.5, -1.49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, -0.5, -2.51, -4.5, -4.5, -1.49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
speedList = []
currentSpeed = 0
for i in accelerationList:
  currentSpeed += int(i*1000)
  speedList.append(float(currentSpeed/1000))
distanceList = []
currentDistance = 0
counter = 0
for i in speedList:
  counter += 1
  currentDistance += int(i*1000)
  distanceList.append(float(currentDistance/1000)) 

print("Time","Dis","Vel","Acc")
for count,ele in enumerate(distanceList): 
  print (count,ele,speedList[count],accelerationList[count]) 