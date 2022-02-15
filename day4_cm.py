a = input("숫자 두 개를 입력해주세요(ex. '3 5') : ")

b = list(a.split(" "))

for i in b:
    c = int(i)
    print(c)