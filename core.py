from files import *
from operations import *
import copy


def countSecondW(w2, stand, y, z, a):
    return difference(w2, AlphMtrx(AlphMtrx(np.transpose(y), z - stand), a))


def covertError(w2, gam):  # Частный случай
    return AlphMtrx(w2, gam)

def transp(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]

########################

def countFirstW(W1, W2, standard, Z, X, Y, alpha):
    per = (formula(MultiMatrx(np.transpose(X), W1)))
    devtos = [[per[i][j] for i in range(len(per))] for j in range(len(per[0]))]

    delW1 = AlphMtrx(MultiMatrx(X, transp(clearMult(np.dot(W2, Z - standard),
                                                    devtos))), alpha)
    a = len(W1[0])
    b = len(W1)
    result = [[W1[i][j] - delW1[i][j] for j in range(a)] for i in range(b)]
    return result


##############################

def FormFunc(X,w1, w2, chainTrain, train, CTM, i, previous, alpha):
    Y = sinArctgFunc(MultiMatrx(np.transpose(X), w1))
    Z = MultiMatrx(Y, w2)
    Z_param = Z[0][0]
    buff = copy.deepcopy(w2)
    w2 = countSecondW(w2, chainTrain[train][CTM + i + previous], Y, Z_param, alpha)
    w1 = countFirstW(w1, buff, chainTrain[train][CTM + i + previous], Z_param, X, Y,
                     alpha)
    arr = [Y, Z, w1, w2, X]
    return arr


def training(p, e, alpha, num, CTM, train, Error): # CTM RTM - row/colum train matrix
    chainTrain = getSequences()

    RTM = len(chainTrain[0]) - CTM - 2
    colum, w1, w2 = gettingData()
    iter = 0

    while errorSum(Error) > e and iter < num:
        Error = []
        MatrixTrain = [[0 for j in range(CTM)] for i in range(RTM)]
        for i in range(RTM):
            for j in range(CTM):
                MatrixTrain[i][j] = [chainTrain[train][i + j]]

        for i in range(len(MatrixTrain)):
            foil = [0]

            chain_tmp = copy.deepcopy(MatrixTrain[i])
            for previous in range(2):
                X = chain_tmp[-1 * CTM:]
                X.append(foil)
                print("--------")

                formFunc = FormFunc(X,w1, w2, chainTrain, train, CTM, i, previous, alpha)
                Y, Z = formFunc[0], formFunc[1]
                w1, w2 = formFunc[2], formFunc[3]
                X = formFunc[4]
                print('X ----->        ' + str(X))

                waiting = str(chainTrain[train][CTM + i + previous])
                print("Ожидание " + waiting)
                reality = str(Z[0][0])
                print('Реальность ' + reality)
                foil = Z[0]
                foil_sec = Z[0][0]
                chain_tmp.append(foil)
                first_alg = (foil_sec - chainTrain[train][CTM + i + previous])
                sec_alg = (foil_sec - chainTrain[train][CTM + i + previous])
                Error.append(first_alg * sec_alg / 2)
        iter += 1
        print("Шаг" + str(iter))
        print('Error  ' + str(errorSum(Error)))

    with open('weigh_2.json', 'w', encoding="utf-8") as w:
        temp_dict = {"colum": CTM, "w1": w1, "w2": w2}
        json.dump(temp_dict, w, indent=2)

    print("Выполнено успешно ")

####################################

def rangeforProgn(n,chain,colum,w1,w2, foil):
    for i in range(n):
        x = chain[-1 * colum:]
        x.append(foil)
        y = sinArctgFunc(MultiMatrx(np.transpose(x), w1))
        Y_cols = len(y[0]) #check
        W_rows = len(w2)
        if Y_cols != W_rows:
            return
        else:
            z = np.matmul(y, w2)
        chain.append(z[0])
        foil = z[0]
        print(z[0][0])
        params = [n,chain,colum,w1,w2, foil]
        return params

def prognosis(chain, n):
    CTM, w1, w2 = gettingData()
    if len(chain) < CTM: return
    foil = [0]
    rangeforProgn(n, chain, CTM, w1, w2, foil)
    print("Выполнено успешно ")
    return
