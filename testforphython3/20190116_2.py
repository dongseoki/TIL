# f1 = open("test.txt", 'w')
# # f1.write("Life is too short")
# # f1.close()
# # f2 = open("test.txt", 'r')
# # print(f2.readline())

# f1 = open("test.txt", 'a')
# str= input("저장할 내용을 입력하세요.:") #, end=' '
# f1.write(str)
# f1.write("\n")
# f1.close()

#
# f = open("새파일.txt", 'r')
# while True:
#     line = f.readline()
#     if not line: break
#     print(line)
# f.close()

# f = open('새파일.txt', 'r')
# body = f.read()
# f.close()
# print(body)
#
# body = body.replace('java', 'python')
# print(body)
# f = open('test.txt', 'w')
# f.write(body)
# f.close()

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))
# 클래스에의해 생성된 객체들은 서로에게 전혀 영향을 주지 않는다.
# # ※ pass는 아무것도 수행하지 않는 문법이다. 임시로 코드를 작성할 때 주로 사용한다.
# ※ 메서드의 첫번째 매개변수를 self를 명시적으로 구현해야 하는 것은 파이썬만의 독특한 특징이다. 예를들어 자바같은 언어는 첫번째 매개변수인 self가 필요없다.
# ※ 객체변수는 속성, 멤버변수 또는 인스턴스 변수라고도 표현한다.


class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

class MoreFourCal(FourCal):
    pass

a= MoreFourCal(4,2)
print(a.add())
print(a.mul())

# a = FourCal(4,0)
# a.div()

class SafeFourCal(FourCal):
    def div(self):
        if self.second ==0:
            return 0
        else:
            return self.first / self.second


a= SafeFourCal(4,0)
print(a.div())