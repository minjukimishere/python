import random
n=random.randint(1,30) #1~30 사이에 있는 임의의 수를 뽑습니다.
while True: #영원히 반복합니다.
    x=input("맞혀봐")
    g=int(x)
    if g==n:
        print("정답")
        break #정답을 맞추면 break문으로 반복문을 빠져나갑니다.
    if g<n:
        print("너무작아요")
    if g>n:
        print("너무 커요")
