import numpy
import numpy as np

def cau3(a,m,n):
    max = 0
    max_index_i = 0
    max_index_j = 0
    for i in range(0,a.shape[0] - m+1):
        for j in range(0,a.shape[1]-m+1):
            temp = (a[i:i+m,j:j+n])
            if np.sum(temp) >= max:
                max = np.sum(temp)
                max_index_i = i
                max_index_j = j
    return a[max_index_i:max_index_i+m,max_index_j:max_index_j+n]
if __name__ == "__main__":
    a = np.array([[1,1,3,4,5],[2,3,3,4,5],[6,4,1,2,3],[1,2,3,4,5],[2,3,4,5,6]])
    print(a)
    print(cau3(a,4,4))
    print(numpy.sum(a))