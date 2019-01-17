# [문제2] 숫자의 총합
#
# 사용자로부터 다음과 같은 숫자들의 입력을 받아 입력받은 숫자들의 총합을 구하는 프로그램을 작성하시오. (단, 숫자들은 콤마로 구분하여 입력한다.)
#
# 65,45,2,3,45,8

# [풀이2] 숫자의 총합
#
# user_input = input("숫자를 입력하세요:")
# numbers = user_input.split(",")
# total = 0
# for n in numbers:
#     total += int(n)  # 입력은 문자열이므로 숫자로 변환해야 한다.
# print(total)
#
# [풀이3] 문자열 출력
#
# >>> print("you" "need" "python")
# youneedpython
# >>> print("you"+"need"+"python")
# youneedpython
# >>> print("you", "need", "python")  # 콤마가 있는 경우 공백이 삽입되어 더해진다.
# you need python
# >>> print("".join(["you", "need", "python"]))
# youneedpython

f = open("새파일.txt", 'w')
f.close()
#
f = open("C:/새파일.txt", 'w')
f.close()
