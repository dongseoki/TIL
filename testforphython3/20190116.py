# f = open("C:/새파일.txt",'w')
# for i in range(1,11):
#     data = "%d번째 줄입니다.\n"%i
#     f.write(data)
# f.close()
#
# f = open("C:/새파일.txt",'r')
# while True:
#     line = f.readline()
#     if not line: break
#     print(line)
# f.close()

f = open("foo.txt", 'w')
f.write("Life is too short, you need python")
f.close()

#sys1.py
import sys
args =sys.argv[1:]
for i in args:
    print(i.upper(), end=' ')
