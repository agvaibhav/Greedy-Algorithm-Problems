#empty space on wall should be min
#larger shelf costs less

def fit_shelves(w,m,n):

    #initialize result variables

    num_m=0
    num_n=0
    rem=w

    #p and q are no of shelves of length m and n respectively

    p=0
    q=0
    r=0

    while(w>=n):
        q += 1
        w -= n
        p = w//m
        r = w%m
        if r<=rem:
            num_m=p
            num_n=q
            rem=r

    print(num_m, num_n, rem)

w=24
m=3
n=5
fit_shelves(w,m,n)
