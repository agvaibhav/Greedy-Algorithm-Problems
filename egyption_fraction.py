def egyptian_fraction(nr,dr):
    # if either numerator or denominator is 0
    if(dr == 0 or nr ==0):
        return

    # if num divides den, then simple division makes the fraction 1/n form
    if (dr%nr == 0):
        print("1/{}".format(int(dr/nr)))
        return

    # if den divides num then it is not a fraction
    if (nr%dr == 0):
        print(nr/dr)
        return

    # if num is more than den
    if (nr>dr):
        print(int(nr//dr),end=" + ")
        egyptian_fraction(nr%dr, dr)
        return

    # if den>num
    
    div=(dr//nr)+1
    print("1/{}".format(div),end=" + ")
    newnr=((nr*div)-dr)
    newdr=(dr*div)
    egyptian_fraction(newnr,newdr)

    
nr=int(input("enter the numerator of your fraction:"))
dr=int(input("enter the denominator of your fraction:"))
egyptian_fraction(nr,dr)
