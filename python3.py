inFile=None
inList=[]

inFile=open("C:/Users/1105k/Desktop/난생처음 파이썬을 공부합니다..txt","r",
            encoding="UTF-8")

inList=inFile.readlines()
print(inList)

inFile.close()
