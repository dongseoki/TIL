for i in range(2,10):
    for j in range(1,10):
        print(i*j, end =" ")
    print(' ')


# 리스트 내포! list comprehension
#[표현식 for 항목 in 반복가능객체 if 조건문]

a= [1,2,3,4]
result = [num *3 for num in a if num>=2]
print(result)

result =[x * y for x in range(2,10)
        for y in range(1,10)]
print(result)

# problem 3.
numbers =[1,2,3,4,5]
result =[n*2 for n in numbers if n%2 ==1]
print( "answer:",result)
# def add(a, b):  # a, b는 매개변수
#     return a+b
#
# print(add(3, 4))  # 3, 4는 인수

def add(a,b):
    print(a+b);

a= add(3,4)
print(a)
# add는 리턴값으로 a 변수에 None을 돌려준다. 이것을 가지고 결과값이 있다고 생각하면 곤란하다.
#매개변수를 지정하면 다음과 같이 순서에 상관없이 사용할 수 있다는 장점이 있다.

result = add(b=5, a=3)  # b에 5, a에 3을 전달
print(result)
#입력값이 몇 개가 될지 모를 때는 어떻게 해야 할까?

def add_many(*args):
    result =0
    for i in args:
        result = result +i
    return result

result = add_many(1,2,3,4,5,6,7)
print(result)

def add_mul(choice, *args):
    if choice == "add":
        result =0
        for i in args:
            result = result +i
    elif choice == "mul":
        result =1
        for i in args:
            result *=i
    return result

result = add_mul("mul", 1,2,3,4,5,6)
print(result)

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name='foo', age=3)

def add_mul(a,b):
    return a+b, a*b

result = add_mul(3,4)
print(result)

def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")


say_myself("dongseok", 10,False)
# SyntaxError: non-default argument follows default argument
# 위의 오류 메시지는 초깃값을 설정해 놓은 매개변수 뒤에 초깃값을 설정해 놓지 않은 매개변수는 사용할 수 없다는 말이다. 즉, 매개변수로 (name, old, man=True)는 되지만 (name, man=True, old)는 안 된다는 것이다. 초기화시키고 싶은 매개변수들을 항상 뒤쪽에 위치시키는 것을 잊지 말자.

a=1
def vartest():
    global a
    a= a+1
vartest()
print(a)

def aver(*args):
    sum=0
    count =0
    for i in args:
        sum+=i
    print(sum /len(args))

print("hi")
aver(1,2,3,4,5)

def add_many2(*args):
    result =0
    for i in args:
        print(type(i))
        result = result + i
    return result

num = 10
print(type(10))

result = add_many(1,2,3,4,5,6,7)
print(result)

# str = input("값을 입력하세요:")
# lis1 =str.split(",")
# result =add_many2(lis1)
# print(result)


str = input("값을 입력하세요:")
total = 0
lis1 =str.split(",")
for n in lis1:
    total += int(n)
print(total)