class Family:
    lastname="김"

a = Family()
print(a.lastname)

b = Family
b.lastname = "박"
print(a.lastname)

class Data:
    def __init__(self, data):
        tmp = data.split("|")
        self.name = tmp[0]
        self.age = tmp[1]
        self.grade = tmp[2]
    def print_age(self):
        print(self.age)
    def print_grade(self):
        print("%s 님의 점수는 %s 입니다" %(self.name,self.grade))

a = Data("이동석|25|A")
print(a.age)
a.print_grade()

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value)  # 10에서 7을 뺀 3을 출력

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value >= 100:
            self.value = 100

cal = MaxLimitCalculator()
cal.add(50)  # 50 더하기
cal.add(60)  # 60 더하기

print(cal.value)  # 100 출력

import mod1
print(mod1.add(3,5))
print(mod1.sub(3000,5))

import sys
print(sys.path)
sys.path.append("C:/")
print(sys.path)
import mod2
print(mod2.add(3,4))

#
# import tensorflow as tf
#
# hello=tf.constant("hello(안녕)")
# print(type(hello))
#
# #세션에 데이터를 담는다. 캡슐화
# sess=tf.Session()
# print(sess.run(hello).decode("utf-8"))

import tensorflow as tf

x_data = [1., 2., 3.]
y_data = [1., 2., 3.]

# try to find values for w and b that compute y_data = W * x_data + b
w = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.random_uniform([1], -1.0, 1.0))

# my hypothesis
hypothesis = w * x_data + b

# Simplified cost function
cost = tf.reduce_mean(tf.square(hypothesis - y_data))

# minimize
a = tf.Variable(0.1)  # learning rate, alpha
optimizer = tf.train.GradientDescentOptimizer(a)
train = optimizer.minimize(cost)

# before starting, initialize the variables
init = tf.initialize_all_variables()

# launch
sess = tf.Session()
sess.run(init)

# fit the line
for step in range(2001):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(cost), sess.run(w), sess.run(b))