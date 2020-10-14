import numpy as np

R = np.array(  [[0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 1]])

def hammingDecode(b):
    r = np.array([[int(b[0])],
        [int(b[1])],
        [int(b[2])],
        [int(b[3])],
        [int(b[4])],
        [int(b[5])],
        [int(b[6])]])

    p = np.matmul(R, r)
    print(p)
    return ''.join([str(x) for x in [p[0][0] % 2, p[1][0] % 2, p[2][0] % 2, p[3][0] % 2]])

if __name__ == "__main__":
    rArr = ['1000011', '1111111']
    for r in rArr:
        print(hammingDecode(r))