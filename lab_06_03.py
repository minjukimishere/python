#주사위 3개를 동시에 던져 동일한 숫자 나오기
#주사위 3개를 동시에 던져 모두 동일한 숫자가 나와야만 반복문을 탈출할 수 있는 게임을
#만들어봅시다. 몇 번을 던져야 3개의 주사위에서 동일한 숫자가 나올까요?
#몇 번을 던져야 3개의 주사위가 동시에 같은 수가 나오는지 알 수가 없으므로, 일단은
#무한 루프로 주사위를 던지겠습니다. 그리고 무한 루프 안에서 조건문으로 3개의 주사위가
#같은 숫자면 무한 루프를 빠져나가도록 하겠습니다.

import random
 
count=0 #주사위를 던진 횟수
dice1,dice2,dice3=0,0,0 #주사위 3개

while True:
    count+=1
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice3=random.randint(1,6)
    if(dice1==dice2) and (dice2==dice3):
        break
print("3개 주사위는 모두",dice1,"입니다.")
print("같은 숫자가 나오기까지",count,"번 던졌습니다.")   
   

