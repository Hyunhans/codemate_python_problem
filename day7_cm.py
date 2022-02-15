
def time_x():
    a = int(input("초 단위의 시간을 입력해주세요: "))
    day = a // 86400
    hour = (a % 86400) // 3600
    min = (a % 60) // 60
    sec = a % 60

    print(f"{a}초 = ", end='')

    if day!=0:
        print(f"{day}일", end='')
    if hour!=0:
        print(f"{hour}시간", end='')
    if min!=0:
        print(f"{min}분", end='')
    if sec!=0:
        print(f"{sec}초", end='')

    


time_x()