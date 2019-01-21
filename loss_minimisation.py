def lossMinimisation(l,t,n):
    job=['-1']*n
    result=['-1']*n

    for i in range(n):
        job[i]=l[i]/t[i]
        result[i]=job[i]
        
    for i in range(n):
        for j in range(n-1-i):
            if job[j] < job[j+1]:
                job[j],job[j+1] = job[j+1],job[j]

    for i in range(n):
        for j in range(n):
            if job[i]==result[j]:
                result[j]='-1'
                print(j+1,end=' ')
                break


l=[1,2,3,5,6]
t=[2,4,1,3,2]
n=len(t)

print('sequence of mimised loss: ')
lossMinimisation(l,t,n)
