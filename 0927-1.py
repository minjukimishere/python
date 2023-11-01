Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
num1=100
num2=200
result1=num1+num2

result2=num1-num2
result3=num1*num2
result4=num/num2
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    result4=num/num2
NameError: name 'num' is not defined. Did you mean: 'num1'?
result4=num1/num2
result1
300
>>> result2
-100
>>> result3
20000
>>> result4
0.5
>>> 
============================ RESTART: C:/Users/1105k/Desktop/0927-2.py ===========================
100 + 200 = 300
100 - 200 = -100
100 * 200 = 20000
100 / 200 = 0.5
>>> 333=100Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
... Type "help", "copyright", "credits" or "license()" for more information.
... num1=100
... num2=200
... result1=num1+num2
... 
... result2=num1-num2
... result3=num1*num2
... result4=num/num2
... Traceback (most recent call last):
...   File "<pyshell#5>", line 1, in <module>
...     result4=num/num2
... NameError: name 'num' is not defined. Did you mean: 'num1'?
... result4=num1/num2
... result1
... 300
... result2
... -100
... result3
... 20000
... result4
... 0.5
SyntaxError: invalid decimal literal
>>> 333=100
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> 3abcd=500
SyntaxError: invalid decimal literal
>>> print=100
>>> print=100+200
>>> print("난생처음")
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print("난생처음")
TypeError: 'int' object is not callable
print("난생처음")
print("난생처음")
SyntaxError: invalid decimal literal

print("난생처음")
난생처음
first_num=100
num_inpu=200
inputData=30
num_input=200
input()
100
'100'
num2=input("숫자->")
숫자->100
num2
'100'
num1=input()
10
result1=num1+num2
result1
'10100'
print(result1)
10100
int(input())
100
100
num3=int(input())
100
num4=int(input())
2--
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    num4=int(input())
ValueError: invalid literal for int() with base 10: '2--'
num4=int(input())
200
num3+num4
300
int("100")
100
int(100.12)
100
num1=int(input("숫자1->"))
숫자1->100
num2=int(input("숫자2->"))
숫자2->200
result=num1+num2
print(result)
300

============================ RESTART: C:/Users/1105k/Desktop/0927-3.py ===========================
이름->김민주
전화번호->01065647270
제 이름은 김민주 이고, 연락처는 01065647270 입니다.
>>> 
============================ RESTART: C:/Users/1105k/Desktop/0927-4.py ===========================
##택배를 보내기 위한 정보를 입력하세요.##
받는사람:김민주
주소:원광대
무게(g):1
**받는사람-> 김민주
주소-> 원광대
##배송비-> 5 원
>>> import turtle
>>> turtle.shape
<function shape at 0x0000018308A7B0A0>
>>> trutle.shape('turtle')
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    trutle.shape('turtle')
NameError: name 'trutle' is not defined. Did you mean: 'turtle'?
>>> turtle.shape('turtle')
>>> turtle.forward(200)
>>> turtle.left(90)
>>> turtle.forward(200)
>>> turtle.left(90)
>>> turtle.forward(200)
>>> turtle.left(90)
>>> turtle.forward(200)
>>> 
>>> n1=200; n2=150
>>> n1=200,n2=150
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> a,b,c=3,4,5
>>> print(a+b-c)
2
>>> print(a-c+b)
2
>>> print(-c+a+b)
2
>>> a,b,c,=2,4,6
>>> print(a/b*c)
3.0
>>> print(a*c/b)
3.0
>>> print(c/a*b)
12.0
