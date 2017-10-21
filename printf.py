#입력받은 스도쿠퍼즐을 보여줍니다
def print_inputed_Data (Data) :
    print("입력받은 스도쿠 퍼즐입니다.\n")
    for i in range(0,9) :
        print(Data[i])
    print("\n\n")



#구해진 답을 반영한 스도쿠퍼즐을 보여줍니다
#확정된 답의 좌표, 빈칸에 들어갈 수 있는 수, 빈칸의 수를 출력합니다
def print_calculate_result(answer, setinfo, setlocation, listlocation, ask) :
    print("-------------------------------------------------------------------------")
    print("연산결과 입니다.\n")
    for i in range(0, 9) :
        print(answer[i])
    print("\n\n")
    for location1 in listlocation :
        print("%d행 %d열의 답은 %d였습니다."%(location1[0]+1, location1[1]+1, answer[location1[0]][location1[1]]))
    print("")
    for location2 in setlocation :
        print("%d행 %d열에 들어갈 수 있는 수: %s"%(location2[0]+1, location2[1]+1, setinfo[location2]))
    print("\n\n")
    if len(setlocation) == 0 :
        print("모든 답을 찾았습니다.")
        ask = ""
    elif len(setlocation) != 0 :
        print("아직 %d개의 빈칸이 남았습니다.\n\n"%len(setlocation))
        ask = input("아직 확정되지 않은 답을 찾고 싶으면 엔터를 입력해주세요.종료하려면 아무 문자나 입력해주세요.\n")
    return ask

    
    
def print_final_result(answer) :
    print("-------------------------------------------------------------------------")
    print("연산결과 입니다.\n\n")
    for i in range(0, 9) :
        print(answer[i])
    
    
              
              
        
