def input_Data() :
    Data = [[],[],[],[],[],[],[],[],[]]
    Boolean = True
    
    for col in range(0, 9) :
        if Boolean == False :
            break

        #숫자를 우선 리스트로 받아들임#
        temp = input("스도쿠 퍼즐의 %d번째 행을 띄어쓰기 포함해서 입력해주세요.(빈칸은 0으로 입력): \n" %(col+1))
        L = []
        for i in temp.split() :
            L.append(int(i))

        #숫자를 9개 넣지 않으면 오류#
        if len(L) != 9 :
            print("숫자 9개를 입력해야 합니다.(빈칸은 0으로 입력)\n")
            Boolean = False

        #0을 제외한 중복된 숫자를 넣으면 오류#
        z = L.count(0)
        if z > 0 :
            count = 0
            while count < z :
                L.remove(0)
                count +=1
        S = set(L)
        l = list(S)
        if len(L) != len(l) :
            print("같은 열에 중복되는 숫자가 있으면 안됩니다.\n")
            Boolean = False

        #리스트로 받아들인 숫자들을 다시 2차원 리스트로 변환#
        for j in temp.split() :
            Data[col].append(int(j))

    #오류가 나면 0을 반환함#
    if Boolean == False :
        Data = 0
    return Data



        
        
