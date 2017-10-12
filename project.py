import inputf
import process 

Data1 =inputf.input_Data()

if Data1 == 0 :
    print("오류가 났습니다. 프로그램을 다시 실행해 주세요.")

Data2 = Data3 = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
col = [{},{},{},{},{},{},{},{},{}]
row = [{},{},{},{},{},{},{},{},{}]
box = [{},{},{},{},{},{},{},{},{}]

Data2 = process.make_Data2(Data2, Data1)
Data3 = process.make_Data3(Data3, Data1)
print(Data3)

col = process.make_stdset(Data1, col)
row = process.make_stdset(Data2, row)
box = process.make_stdset(Data3, box)

answer = process.find_answer(Data1, diffset, col, row, box)

for Line in answer :
    print(Line)
