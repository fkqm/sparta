n = input("숫자를 입력하세요:")
n = int(n)
num = range(1, n)
for number in num :
    if number % 2 == 0 :
        print(number)