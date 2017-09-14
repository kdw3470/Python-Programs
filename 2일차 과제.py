f = open('data.txt', 'r')
D = {}




for Line in f :
    for i in Line.split() :
        if i in D :
            D[i] += 1
        else :
            D[i] = 1
print(D)
