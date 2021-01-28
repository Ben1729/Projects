import numpy as np

X = np.fromfile("signal.ham",dtype=np.float16)

votes = {}

print("Proccessing input file....\n")

codewords = []

count = 0

Xlen = len(X)/17

for i in range(0,len(X),17):
    chunk = [0 if x < 0 else 1 for x in X[i:i+17]]
    codewords.append(chunk[:16])

    D = "".join(map(str,chunk[:11]))
    P = "".join(map(str,chunk[:11:16]))

    if sum(chunk[:11]) == 1:
        if D not in votes:
            votes[D] = {P:1}
        elif P not in votes[D]:
            votes[D][P] = 1
        else:
            votes[D][P] +=1

    count += 1

    print("\rProccessed %d / %d symbols in file." % (count, Xlen), end="")

H = []
G = []

print("\n\n")
for idx in votes:
    print(votes[idx])

print("\n\n--- Extracted Codewords (Generator Matrix) ---\n")

for i in range(1,12):
    idx = ("1" + ("0" * (11-i))).zfill(11)
    chunk_votes = sorted(votes[idx].items(), key=lambda x: x[1], reverse=True)
    print(idx,chunk_votes[0][0])

    best_code = [0 if x=="0" else 1 for x in chunk_votes[0][0]]

    H.append(best_code)
    G.append([0 if x=="0" else 1 for x in idx]+best_code)