s1 = set([1,2,3])
print(s1)

l1 = list(s1)

t1 = tuple(s1)

print(l1)
print(t1)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 & s2)
print(s1.intersection(s2))
print(s1 | s2) # s1.union(s2)
print(s1 - s2) # s1.difference(s2)
s1.add(10)
print(s1)
s1.update([345,623, 45])
print(s1)
print(type(s1))

##p1

a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
b = set(a)
print(b)

s3 = set()
print(s3)

a = [1, 2, 3]
print(id(a))
b=a

print(a is b)
print(a in b)
print("1" in "123")

#a가 가리키는 리스트와는 다른 리스트를 가리키게 하는 방법1

c = a[:]
print(c)
print(id(c))

from copy import copy
f = copy(a)
print(f)

[a,b] = ['python', 'life']
print(a," 0=========",b)
c, d = ('python', 'life')
print(d," 0=========",d)

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)
# 객체 판별 is. 내용물 판별 ==
a=[1]
a.extend([4, 5]) # id가 안변함
a= a+ [7] # id가 변함

#indentation 들여쓰기 라는 뜻이다.
#and, or, not
#x in s, x not in s
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else:
    print("card!!")

print("Hello")
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket: pass
else: print("카드를 꺼내라")
number =0
notification ="""
1.Add
2.Del
3.List
4.Quit
Enter number: """

while number !=4:
    print(notification)
    number = int(input())

a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)