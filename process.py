#def show_Data (Data) :
    #for i in Data :
        #print(i)
Data = [[0, 9, 0, 8, 0, 0, 7, 6, 5], [0, 9, 8, 7, 6, 5, 4, 3, 2], [1, 3, 4, 5, 6, 7, 0, 9, 8], [1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 9, 8, 7, 4, 5, 3, 2, 1], [0, 9, 0, 8, 0, 7, 1, 2, 0], [1, 3, 4, 5, 6, 0, 9, 8, 7], [1, 3, 4, 5, 6, 7, 0, 0, 0], [1, 2, 3, 4, 5, 6, 7, 8, 9]]
Data1 = [[0, 9, 0, 8, 0, 0, 7, 6, 5], [0, 9, 8, 7, 6, 5, 4, 3, 2], [1, 3, 4, 5, 6, 7, 0, 9, 8], [1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 9, 8, 7, 4, 5, 3, 2, 1], [0, 9, 0, 8, 0, 7, 1, 2, 0], [1, 3, 4, 5, 6, 0, 9, 8, 7], [1, 3, 4, 5, 6, 7, 0, 0, 0], [1, 2, 3, 4, 5, 6, 7, 8, 9]]
Data2 = Data3 = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
Result = [[0, 9, 0, 8, 0, 0, 7, 6, 5], [0, 9, 8, 7, 6, 5, 4, 3, 2], [1, 3, 4, 5, 6, 7, 0, 9, 8], [1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 9, 8, 7, 4, 5, 3, 2, 1], [0, 9, 0, 8, 0, 7, 1, 2, 0], [1, 3, 4, 5, 6, 0, 9, 8, 7], [1, 3, 4, 5, 6, 7, 0, 0, 0], [1, 2, 3, 4, 5, 6, 7, 8, 9]]
col = [{},{},{},{},{},{},{},{},{}]
row = [{},{},{},{},{},{},{},{},{}]
box = [{},{},{},{},{},{},{},{},{}]

def make_stdset(D, SD) :
    a = 0
    for r in D :
        z = r.count(0)
        print(z)
        S = set(r)
        if z > 0 :
            r.remove(0)
        SD[a] = S
        a += 1
    return SD



def make_Data2(Data2, Data1) :
    for i in range(0, 9) :
        for j in range(0, 9) :
            Data2[i][j] = Data1[j][i]
    return Data2


def make_Data3(Data3, Data1) :
    
    for a in range(0,3) :
        for b in range(0, 3) :
            for c in range(3*a, 3+3*a) :
                for d in range(3*b, 3+3*b) :
                    print(a,b,c,d)


                    if a == 0 :
                        if b == 0 :
                            Data3[0].append(Data1[c][d])
                        elif b == 1 :
                            Data3[1].append(Data1[c][d])
                        elif b == 2 :
                            Data3[2].append(Data1[c][d])

                    if a == 1 :
                        if b == 0 :
                            Data3[3].append(Data1[c][d])
                        elif b == 1 :
                            Data3[4].append(Data1[c][d])
                        elif  b == 2 :
                            Data3[5].append(Data1[c][d])
                    if a == 2 :
                        if b == 0 :
                            Data3[6].append(Data1[c][d])
                        elif b == 1 :
                            Data3[7].append(Data1[c][d])
                        elif b == 2 :
                            Data3[8].append(Data1[c][d])
                        
                         

    return(Data3)






def find_answer(Data, diffset, col, row, box) :

    for a in range(0,3) :
        for b in range(0, 3) :
            for c in range(3*a, 3+3*a) :
                for d in range(3*b, 3+3*b) :
                

                
                    if Data[c][d] != 0 :
                        continue
                    diffSet = {1,2,3,4,5,6,7,8,9}
                    diffSet.difference(col[c])
                    diffSet.difference(row[d])
                    print(diffSet)
                    if a == 0 and b == 0 :
                         diffSet.difference(box[0])

                    if a == 0 and b == 1 :
                         diffSet.difference(box[1])

                    if a == 0 and b == 2 :
                         diffSet.difference(box[2])

                    if a == 1 and b == 0 :
                         diffSet.difference(box[3])

                    if a == 1 and b == 1 :
                         diffSet.difference(box[4])

                    if a == 1 and b == 2 :
                         diffSet.difference(box[5])

                    if a == 2 and b == 0 :
                         diffSet.difference(box[6])

                    if a == 2 and b == 1 :
                         diffSet.difference(box[7])

                    if a == 2 and b == 2 :
                         diffSet.difference(box[8])


                    answer[c][d] = diffSet
    return answer




            





        

