import numpy as np
def y1():
    fo = open("text.txt","r")
    lineA = fo.readline()
    lineB = fo.readline()
    word = lineA.split()
    wordb = lineB.split()
    checkA = []
    checkB = []
    for i in range(int(word[0])):
        checkA.extend(((fo.readline().split())))
    tempA = np.reshape(checkA,(int(word[0]),int(word[1]))).astype(int)
    for i in range(int(wordb[0])):
        checkB.extend(((fo.readline().split())))
    tempB = np.reshape(checkB,(int(wordb[0]),int(wordb[1]))).astype(int)
    fo.close()
    return tempA,tempB
def y2(A,B):
    fo = open("output.txt", "w")
    if A.shape[1] == B.shape[0]:
        C=A.dot(B)
        fo.write(str(C)+'\n')
        fo.close()
    else:
        fo.write('ko thoa man')
    fo.close()
def y3(A,B):
    fo = open("output.txt", "a")
    if A.shape[1] == B.shape[0]:
        C=(A.T).dot(B)
        fo.write(str(C)+'\n')
        fo.close()
    else:
        fo.write('ko thoa man')
    fo.close()
if __name__ == "__main__":
    A, B = y1()
    print(A)
    print(B)
    y2(A,B)
    y3(A,B)
