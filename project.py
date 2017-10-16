
def find_sdokou_answer(Data1) :
    Data2 = process.make_Data2(Data1)
    Data3 = process.make_Data3(Data1)
    col = process.make_stdset(Data1)
    row = process.make_stdset(Data2)
    box = process.make_stdset(Data3)
    answer, setinfo, setlocation, listlocation = process.find_answer(Data1, col, row, box)
    return answer, setinfo, setlocation, listlocation


import inputf
ask = input("sdokou.txt로 스도쿠퍼즐을 입력하길 원하면 아무 문자나 입력해주세요.\n직접 입력하려면 엔터를 누르세요.\n")
if ask != "" :
    Data1, Boolean =inputf.inputf_Data()
else :
    Data1, Boolean = inputf.input_Data()

if Boolean == False :
    print("오류가 났습니다. 프로그램을 다시 실행해 주세요.")
if Boolean == True :
    import printf
    printf.print_inputed_Data(Data1)
    import process

    Data2 = process.make_Data2(Data1)
    Data3 = process.make_Data3(Data1)

    flag = True
    for i in range(0,8) :
        a = process.check_Overlap(Data2[i])
        b =process.check_Overlap(Data3[i])
        if a == False :
            print("%d열에 중복되는 숫자가 있으면 안됩니다.\n" %(i+1))
            print("오류가 났습니다. 프로그램을 다시 실행해 주세요.")
        
        
            flag = False
        if b == False :
            print("%d번째 정사각형에 중복되는 숫자가 있으면 안됩니다.\n" %(i+1))
            print("오류가 났습니다. 프로그램을 다시 실행해 주세요.")
            flag = False

          
    if flag == True :
    
        col = process.make_stdset(Data1)
        row = process.make_stdset(Data2)
        box = process.make_stdset(Data3)



        answer, setinfo, setlocation, listlocation = process.find_answer(Data1, col, row, box)



        ask = printf.print_calculate_result(answer, setinfo, setlocation, listlocation, ask)
        while ask != "" :
            answer, setinfo, setlocation, listlocation = find_sdokou_answer(answer)
            ask = printf.print_calculate_result(answer, setinfo, setlocation, listlocation, ask)


