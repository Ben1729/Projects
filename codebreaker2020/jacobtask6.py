import numpy as np

X = np.fromfile("signal.ham",dtype=np.float16)

votes = {}

print("Processing input file....")

for i in range(0,len(X),17):

    chunk = [0 if x < 0 else 1 for x in X[i:i+17]]

    D = "".join(map(str,chunk[:11]))
    P = "".join(map(str,chunk[11:16]))

    if sum(chunk[:11]) == 1:

        if D not in votes:
            votes[D] = {P:1}
        elif P not in votes[D]:
            votes[D][P] = 1
        else:
            votes[D][P] += 1

H = []

print("--- Extracted Codewords ---\n")

for i in range(1,12):

    idx = ("1" + ("0" * (11-i))).zfill(11)
    chunk_votes = sorted(votes[idx].items(), key=lambda x: x[1], reverse=True)
    print(idx,chunk_votes[0][0])
    H.append([0 if x=="0" else 1 for x in chunk_votes[0][0]])

print("\n\nParity Check Matrix Answer:\n\n")

H = np.uint8(np.hstack([np.array(H).T,np.identity(5)]))
H[4,:] = 1

print(H.tolist())