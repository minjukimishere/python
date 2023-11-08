print("홍길동 선수 경기 끝났습니다~~ 짝짝짝")

score=[]
for i in range(5):
    jumsu=int(input("평가점수==>"))
    score.append(jumsu)

hap=0
for i in range(5):
    hap+=score[i]

avg=hap/5
print("심사위원 평균 점수:",avg)
