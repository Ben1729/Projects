import math

dans = []
for i in range(int(input())):
	
	message = input()
	dmessage = []
	
	ans = []
	for i in range(0,len(message),math.floor(math.sqrt(len(message)))):
		text = message[i:i + math.floor(math.sqrt(len(message)))]
		ans.append(text[:: - 1])

	for i in range(len(ans)):
		for j in range(len(ans)):
			dmessage.append(ans[j][i])
	dans.append(''.join(dmessage))

for item in dans:
	print(item)