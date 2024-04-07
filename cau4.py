import numpy
import numpy as np
def y1(a):
    b=a[:,::-1]
    c= b.T
    d = c[:,::-1]
    return d
def find_max(b):
    check = []
    for j in range(b.shape[1]):
        x = max(b[:, j])
        check.append(x)
    return check
if __name__ == "__main__":
    n=int(input("nhap n: "))
    a=numpy.random.choice(range(1,26),n**2).reshape(n,n)
    print(a)
    k = y1(a)
    print(k)
    print(find_max(k))