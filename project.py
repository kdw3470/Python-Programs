#답을 구하는 순서
def find_sdokou_answer(Data1) :
    Data2 = process.make_Data2(Data1)
    Data3 = process.make_Data3(Data1)
    col = process.make_stdset(Data1)
    row = process.make_stdset(Data2)
    box = process.make_stdset(Data3)
    answer, setinfo, setlocation, listlocation = process.find_answer(Data1, col, row, box)
    return answer, setinfo, setlocation, listlocation

#입력부분
#변수 Boolean은 오류를 츨력하기 위해 설정
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


    #처리 부분
    #flag도 오류처리를 위해 설정
    import process
    #열,사각형 정보를 2차원 리스트형태로 변환
    Data2 = process.make_Data2(Data1)
    Data3 = process.make_Data3(Data1)

    #열과 사각형의 중복을 검사
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
        #각각의 행, 열, 사각형의  중복 숫자에 대한 정보를 집합을 원소로 하는 리스트로 변환    
        col = process.make_stdset(Data1)
        row = process.make_stdset(Data2)
        box = process.make_stdset(Data3)


        #변수 answer은 Data1에다가 빈칸에 확정된 답을 넣은 2차원 리스트
        #setinfo, setlocation, listlocation은 출력에 관한 데이터
        answer, setinfo, setlocation, listlocation = process.find_answer(Data1, col, row, box)


        #사용자가 원하면 답을 계속 구할 수 있음
        ask_loop = input("한번에 답을 구하길 원하면 아무 문자나 입력해주세요.\n차례대로 답을 구하길 원하면 엔터를 누르세요.")
        if ask_loop == "" :
            ask = printf.print_calculate_result(answer, setinfo, setlocation, listlocation, ask)
            while ask == "" :
                answer, setinfo, setlocation, listlocation = find_sdokou_answer(answer)
                ask = printf.print_calculate_result(answer, setinfo, setlocation, listlocation, ask)
        else :
            while len(setlocation) > 0:
                print(setinfo)
                answer, setinfo, setlocation, listlocation = find_sdokou_answer(answer)
            printf.print_final_result(answer)




            

