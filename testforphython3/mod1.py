# mod1.py
def add(a, b):
    return a + b

def sub(a, b):
    return a-b

if __name__ == "__main__":
    print(add(1, 4))
    print(sub(4, 2))
#
# 파이썬의 __name__ 변수는 파이썬이 내부적으로 사용하는 특별한 변수명이다. 만약 C:\doit>python mod1.py처럼 직접 mod1.py 파일을 실행시킬 경우 mod1.py의 __name__ 변수에는 __main__ 이라는 값이 저장된다. 하지만 파이썬 쉘이나 다른 파이썬 모듈에서 mod1을 import 할 경우에는 mod1.py의 __name__ 변수에는 "mod1"이라는 mod1.py의 모듈이름 값이 저장된다.