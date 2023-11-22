inFile2=None #입력파일
inStr2="" #읽어온 문자열

inFile2=open("C:/Users/1105k/Desktop/난생처음 파이썬을 공부합니다..txt","r",
            encoding="UTF-8")

inStr2=inFile2.readline()
print(inStr2,end='')

inStr2=inFile2.readline()
print(inStr2,end='')

inStr2=inFile2.readline()
print(inStr2,end='')

inFile2.close()
