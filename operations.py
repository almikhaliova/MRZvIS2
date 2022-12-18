import numpy as np
import math


def weightForMatrix(row, colum):
    Weight = np.random.randint(-1/100, 1/100, (row, colum))
    return Weight


def startMatrix(chain, row, colum):
    result = [[0 for j in range(colum)] for i in range(row)]
    for i in range(row):
        for j in range(colum):
            result[i][j] = [chain[i + j]]
    return result


def errorSum(E):
    rez = []
    for i in range(len(E)):
        rez.append(E[i])
    return sum(rez)


def sinArctgFunc(A):
    return [[math.sin(math.atan(A[i][j])) for j in range(len(A[0]))] for i in range(len(A))]


def difference(m1, m2):
    a = len(m1[0])
    b = len(m1)
    result = [[m1[i][j] - m2[i][j] for j in range(a)] for i in range(b)]
    return result


def AlphMtrx(m, a):
    return np.dot(a, m)


def formula(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            first = (M[i][j]**2)/((M[i][j]+1)**(3/2))
            second = 1/(M[i][j]**2+1)**(1/2)
            M[i][j] = -first + second
    return M


def MultiMatrx(A, B):
    A_cols = len(A[0])
    B_rows = len(B)
    if A_cols != B_rows:
        print("Размер матриц не соответствует")
        return
    else:
        return np.matmul(A, B)


def clearMult(M, M1):
    if M[0] == M1[0] and M == M1:
        print("Размер матриц не соответствует")
        return 0
    else:
        return np.multiply(M, M1)
