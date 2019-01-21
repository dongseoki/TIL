# [풀이1] 모듈 사용하기 1
#
# 파이썬 shell에서 mymod.py 라는 모듈을 인식하기 위해서는 다음과 같은 3가지 방법이 있을 수 있다.
#
# 1) sys 모듈 사용하기
#
# 다음과 같이 sys.path 에 c:\doit 이라는 디렉토리를 추가하면 c:\doit 이라는 디렉토리에 있는 mymod 모듈을 사용할 수 있게 된다.
#
# >>> import sys
# >>> sys.path.append("c:/doit")
# >>> import mymod
# 2) PYTHONPATH 환경변수 사용하기
#
# 다음처럼 PYTHONPATH 환경변수에 c:\doit 디렉토리를 지정하면 c:\doit 디렉토리에 있는 mymod 모듈을 사용할 수 있게 된다.
#
# C:\Users\home>set PYTHONPATH=c:\doit
# C:\Users\home>python
# Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 03:03:55)
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import mymod
# 3) 현재 디렉터리 이용하기
#
# 파이썬 shell을 mymod.py 가 있는 위치로 이동하여 실행해도 mymod 모듈을 이용할 수 있게 된다. 왜냐하면 sys.path 에는 현재디렉터리인 . 이 항상 포함되어 있기 때문이다.
#
# C:\Users\home>cd c:\doit
# C:\doit>python
# Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 03:03:55)
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import mymod



# __init__.py 파일은 조금 특이한 용도로 사용되는데, 이것에 대해서는 뒤에서 자세하게 다룰 것이다.
# step1
# import game.sound.echo
# game.sound.echo.echo_test()

#  step 2
# from game.sound import  echo
# echo.echo_test()

# step3
# from game.sound.echo import  echo_test
# # echo_test()

# error
# import game
# game.sound.echo.echo_test()

# 파일을 변경한 후 되더라!!
# from game.sound import *
# echo.echo_test()

from game.graphic.render import render_test
render_test()

# try:
#     4/0
# except ZeroDivisionError as e:
#     print(e)
#
#
# try:
#     a = [1,2]
#     print(a[3])
#     4/0
# except (ZeroDivisionError, IndexError) as e:
#     print(e)

#
# class Bird:
#     def fly(self):
#         raise NotImplementedError
#
# class Eagle(Bird):
#     pass
#
# eagle = Eagle()
# eagle.fly()

class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)