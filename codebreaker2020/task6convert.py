import numpy as np
import struct

def synTable(h):

	X = np.identity(16,dtype=np.uint8)

	Y = []

	S = {}

	for i in range(len(X)):
		for j in range(16):
			if i == j:
				continue
			Z = X[i].tolist()
			Z[j] = 1

			if Z not in Y:
				Y.append(Z)

	X = np.vstack([X,Y])

	for row in X:

		s = np.matmul(h,row) % 2

		idx = int("".join(map(str,s)),2)

		if idx not in S:
			#print(row," ",idx)
			S[idx] = row

		output = [[0]*16]

		for i in sorted(S.keys()):
			output.append(S[i].tolist())

		return np.array(output)

X = np.fromfile("signal.ham",dtype=np.float16)

votes = {}

print("Processing input file. . . .\n")

codewords = []

count = 0

Xlen = len(X)/17

for i in range(0,len(X),17):

	chunk = [0 if x < 0 else 1 for x in X[i:i+17]]

	codewords.append(chunk[:16])

	D = "".join(map(str,chunk[:11]))
	P = "".join(map(str,chunk[11:16]))

	if sum(chunk[:11]) == 1: 

		if D not in votes:
			votes[D] = {P:1}
		elif P not in votes[D]:
			votes[D][P] = 1
		else:
			votes[D][P] += 1

	count += 1

	print("\rProcessed %d / %d symbols in file." % (count, Xlen), end="")

H = []
G = []

print("\n\n--- Extracted Codewords (Generator matrix) ---\n")

for i in range (1,12):

	idx = ("1" + ("0" * (11-i))).zfill(11)
	chunk_votes = sorted(votes[idx].items(), key=lambda x: x[1], reverse=True)
	print(idx,chunk_votes[0][0])

	best_code = [0 if x=="0" else 1 for x in chunk_votes[0][0]]

	H.append(best_code)
	G.append([0 if x =="0" else 1 for x in idx]+best_code)

print("\n\nParity Check Matrix Answer:\n\n")

H = np.uint8(np.hstack([np.array(H).T,np.identity(5)]))
H[4,:] = 1

print(H.tolist()) 

print("\n\nDecoding file...\n\n")

output = []

error_count = 0
count = 0

ST = synTable(H)

with open("output.avi","wb") as F:

	for D in codewords:

		#Error syndrome is the parity check matrix dot input mod 2
		S = np.matmul(H,np.uint8(D)) % 2

		#print(S)

		#If there are any bits set them to 1 then there is an error
		if np.any(S):

			idx = int("".join(map(str,S)),2)

			D = (D + ST[idx]) % 2
			error_count += 1
			output += map(str,np.uint8(D[:11]).tolist())

		count +=1

		print("\rProcessed %d / %d codewords in file. (%d Errors)" % (count,len(codewords),error_count),end="")

	for i in range(0,len(output)//8):
		F.write(struct.pack('>B', int("".join(output[(i*8):(i+1)*8]),2)))
F.close()
