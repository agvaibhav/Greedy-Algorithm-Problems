def assign_mice_to_holes(pm,ph):
    pm=sorted(pm)
    ph=sorted(ph)
    ans=0
    for i in range(len(pm)):
        if abs(pm[i]-ph[i])>ans:
            ans = abs(pm[i]-ph[i])

    return ans

pm=[-10, -79, -79, 67, 93, -85, -28, -94 ]
ph=[-2, 9, 69, 25, -31, 23, 50, 78 ]

print(assign_mice_to_holes(pm,ph))
