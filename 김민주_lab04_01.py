Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
var1=100
var2=3.14
var4="파이썬"
var3=True
type(var1)
<class 'int'>
var5="""난생처음
파이썬을
열공중입니다."""
print(var5)
난생처음
파이썬을
열공중입니다.
type(var2)
<class 'float'>
type(var3)
<class 'bool'>
type(var4)
<class 'str'>
print('난생\n처음')
난생
처음
print('난생\t처음')
난생	처음
print('난생\b처음')
난생처음
print('난생\'처음')
난생'처음
print('난생\"처음')
난생"처음
print('난생\\처음')
난생\처음
print("\난생처음")
\난생처음
print("\\난생처음")
\난생처음
print("\")
      
SyntaxError: incomplete input
print("\ ")
      
\ 
print("난생"-"처음")
      
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print("난생"-"처음")
TypeError: unsupported operand type(s) for -: 'str' and 'str'
print("난생"*"처음")
      
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print("난생"*"처음")
TypeError: can't multiply sequence by non-int of type 'str'
print("난생"/"처음")
      
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print("난생"/"처음")
TypeError: unsupported operand type(s) for /: 'str' and 'str'
print("난생"*3)
      
난생난생난생
print(" ")
      
 
print('난생')
      
난생
print("난생"+"처음")
      
난생처음
print("난생"+"처음") //주석인가요?
      
SyntaxError: incomplete input
ss="First Python을 저녁 10시까지 열공 중!"
      
var1=ss.upper()
      
print(var1)
      
FIRST PYTHON을 저녁 10시까지 열공 중!
var2=ss.lower()
      
print(var2)
      
first python을 저녁 10시까지 열공 중!
ss="트와이스"
      
print(ss[3],end='')
      
스
print(ss[2],end='')
      
이
print(ss[1],end='')
      
와
print(ss[0],end='')
      
트
print(ss[3],end=''); print(ss[2],end=''); print(ss[1],end=''); print(ss[0],end='')
      
스이와트
import turtle
turtle.shape("turtle")
turtle.penup()
while True:
    x=int(input("x위치-->"))
    y=int(input("y위치-->"))
    text=input("쓰고 싶은 글자-->")

    
x위치-->while True:
    x=int(input("x위치-->"))
    y=int(input("y위치-->"))
...     text=input("쓰고 싶은 글자-->")
Traceback (most recent call last):
  File "<pyshell#48>", line 2, in <module>
    x=int(input("x위치-->"))
ValueError: invalid literal for int() with base 10: 'while True:'
>>> while True:
...     x=int(input("x위치-->"))
...     y=int(input("y위치-->"))
...     text=input("쓰고 싶은 글자-->"); turtle.goto(x,y); turtle.write(text,font=("Arial",30))
... 
...     
x위치-->Traceback (most recent call last):
  File "<pyshell#50>", line 2, in <module>
    x=int(input("x위치-->"))
ValueError: invalid literal for int() with base 10: '    x=int(input("x위치-->"))'
>>> while True:
...     x=int(input("x위치-->"))
...     y=int(input("y위치-->"))
...     text=input("쓰고 싶은 글자-->"); turtle.goto(x,y); turtle.write(text,font=("Arial",30))
... 
...     
x위치-->Traceback (most recent call last):
  File "<pyshell#52>", line 2, in <module>
    x=int(input("x위치-->"))
ValueError: invalid literal for int() with base 10: '    y=int(input("y위치-->"))'
>>> while True:
...     x=int(input("x위치-->"))
...     y=int(input("y위치-->"))
...     text=input("쓰고 싶은 글자-->")
... 
...     
x위치-->Traceback (most recent call last):
  File "<pyshell#54>", line 2, in <module>
    x=int(input("x위치-->"))
ValueError: invalid literal for int() with base 10: '    text=input("쓰고 싶은 글자-->")'
>>> ss="Python"
>>> print("원본 문자열->",ss)
원본 문자열-> Python
>>> ss2=""
>>> ss2+=ss[0].lower()
>>> ss2+=ss[1].upper()
>>> ss2+=ss[3].upper()
>>> ss2+=ss[4].upper()
>>> ss2+=ss[5].upper()
>>> ss2
'pYHON'
