inFile=None
inStr=""

inFile=open("C:/Users/1105k/Desktop/난생처음 파이썬을 공부합니다..txt","r",
            encoding="UTF-8")

while True:
    inStr=inFile.readline()
    if inStr=="":
        break
    print(inStr,end='')

inFile.close()
