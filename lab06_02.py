#lab 구구단 계산기 만들기
#2단부터 9단까지 구구단을 출력하는 구구단 계산기를 만들어 봅시다.
#2단~9단까지 for문을 사용해야 합니다. 그런데 2단에서 곱하는 숫자가 1부터 9로 변경
#되기 때문에 곱하는 숫자는 for문을 사용해야 합니다.
#결국 바깥 for문은 단을, 안쪽 for문을 1,2,3 등의 곱하는 숫자를 사용해야 합니다.
#즉, 중첩 for문을 사용해서 코드를 작성해야 합니다.

i=0
k=0

for i in range(2,10,1):
    for k in range(1,10,1):
        print(i,"x",k,"=",i*k)
    print("")