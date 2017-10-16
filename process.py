

#리스트 데이터에서 집합을 만들어 현재 행,열,정사각형에 있는 숫자를 구합니다
def make_stdset(D) :
    SD = [{},{},{},{},{},{},{},{},{}]
    a = 0
    for r in D :
        z = r.count(0)
        S = set(r)
        if z > 0 :
            S.remove(int(0))
        SD[a] = S
        a += 1
    return SD

#행정보는 입력과정에서 증복검사를 했지만 열과 정사각형은 안했기 때문에 중복검사를 합니다
def check_Overlap(D):
    Boolean = True
    z = D.count(0)
    if z > 0 :
        count = 0
        while count < z :
            D.remove(0)
            count +=1
    S = set(D)
    l = list(S)
    if len(D) != len(l) :
        Boolean = False
    return Boolean
        
        

#행정보로부터 열정보를 2차원 리스트 형태로 구합니다
def make_Data2(Data1) :
    Data2 = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
    for i in range(0, 9) :
        for j in range(0, 9) :
            Data2[i][j] = Data1[j][i]
    return Data2

#행정보로부터 정사각형정보를 2차원 리스트 형태로 구합니다
def make_Data3(Data1) :
    Data3 = [[],[],[],[],[],[],[],[],[]]
    
    for a in range(0,3) :
        for b in range(0, 3) :
            for c in range(3*a, 3+3*a) :
                for d in range(3*b, 3+3*b) :


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





#퍼즐을 하나씩 일일히 조사하여 확정되는 답을 구합니다
#각 칸에 중복되는 숫자를 col, row, box에서 제외해 남은 숫자를 구합니다
#만약 남은 숫자가 하나면 답으로 확정합니다
def find_answer(Data, col, row, box) :
    setinfo = {}
    setlocation = []
    listlocation = []
    
    for a in range(0,3) :
        for b in range(0, 3) :
            for c in range(3*a, 3+3*a) :
                for d in range(3*b, 3+3*b) :
                

                
                    if Data[c][d] == 0 or type(Data[c][d]) == set:
                                               
                        diffSet = {1,2,3,4,5,6,7,8,9}
                        diffSet =diffSet.difference(col[c])
                        diffSet = diffSet.difference(row[d])
                        if a == 0 and b == 0 :
                             diffSet = diffSet.difference(box[0])

                        if a == 0 and b == 1 :
                             diffSet = diffSet.difference(box[1])

                        if a == 0 and b == 2 :
                             diffSet = diffSet.difference(box[2])

                        if a == 1 and b == 0 :
                             diffSet = diffSet.difference(box[3])

                        if a == 1 and b == 1 :
                             diffSet = diffSet.difference(box[4])

                        if a == 1 and b == 2 :
                             diffSet = diffSet.difference(box[5])

                        if a == 2 and b == 0 :
                             diffSet = diffSet.difference(box[6])

                        if a == 2 and b == 1 :
                             diffSet = diffSet.difference(box[7])

                        if a == 2 and b == 2 :
                             diffSet = diffSet.difference(box[8])

                        if len(diffSet) == 1 :
                            L = list(diffSet)
                            Data[c][d] = L[0]
                            listlocation.append((c, d))
                        if len(diffSet) > 1 :
                            setlocation.append((c ,d))
                            setinfo[(c, d)] = diffSet

                    
    return Data, setinfo, setlocation, listlocation




            





        

