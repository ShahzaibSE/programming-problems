def compareTriplets(a, b):
    comp_points = []
    alice_point = 0
    bob_point = 0
    if(len(a) == len(b)):
        for i in range(0,len(a)):
            if ((a[i] >= 1 and a[i] <= 100) and (b[i] >= 1 and b[i] <= 100)):
                if (a[i] > b[i]):
                    alice_point = alice_point + 1
                if (b[i] > a[i]):
                    bob_point = bob_point + 1
                else:
                    continue 
    comp_points.append(alice_point)
    comp_points.append(bob_point)
    return comp_points

print(compareTriplets([17,28, 30], [99,16,8]))