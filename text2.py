outFile=None
outStr=""

outFile=open("C:/Users/1105k/Desktop/myData3.txt","w")

while True:
    outStr=input("내용입력==>")
    if outStr!="":
            outFile.writelines(outStr+"\n")
    else:
        break
outFile.close()
print("---myData3.txt 파일이 저장됨---")
