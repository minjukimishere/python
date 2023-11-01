# 컴퓨터와 인간의 숫자 맞히기 대결
# 컴퓨터가 1~5까지 숫자 중 한 가지를 생각하면, 사람이 그 숫자를 맞히는 게임입니다.
#단 10번 안에는 맞혀야 합니다.
import random

computer,user=0,0

for i in range(1,11,1):
    computer=random.randint(1,5)
    print("게임",i,"회:",end='')
    user=int(input("컴퓨터가 생각한 숫자는?"))

0    if computer==user:
        print("맞혔네요. 축하합니다!!")
    else:
        print("아까워요.",computer,"였는데요.다시해보세요.ㅠ")
        continue
    print("게임을 마칩니다.")
