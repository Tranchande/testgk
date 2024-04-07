if __name__ == "__main__":
    A = [9,3,2,5,4,7,8,7]
    dic = {}
    for i in A:
        if i in dic:
            dic[i]+=1
        else:
            dic[i] = 1
    temp = sorted(dic.items(),reverse=True)
    C =[0]*len(A)
    for i in range(len(A)):
        for j in range(len(temp)):
            if A[i] == temp[j][0]:
                C[i] = j+1
    print(C)
    print(temp)