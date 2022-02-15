

def cal_circle(r):
    return round(r * r * 3.1415, 2)

def cal_triangle(line_below, height):
    return line_below * height / 2

def cal_rectangle(width, vertical):
    return width * vertical

def cal_square(side):
    return side ** 2

#def requirment():

def auto_calculator():
    question = input("도형 목록에서 넓이를 계산할 도형의 번호를 입력해주세요 : ")

    # print(type(question))

    if question is '1':
        radius = int(input("원의 반지름을 입력해주세요 : "))
        return f"원의 넓이는 : {cal_circle(radius)}"

    elif question is '2':
        below_side = int(input("삼각형의 밑변 길이를 입력해주세요 : "))
        height = int(input("삼각형의 높이를 입력해주세요 : "))
        return f"삼각형의 넓이는 : {cal_triangle(below_side, height)}" 
    
    elif question is '3':
        width = int(input("직사격형의 가로 길이를 입력해주세요 : "))
        vertical = int(input("직사각형의 세로 길이를 입력해주세요 : "))
        return f"직사각형의 넓이 : { cal_rectangle(width, vertical)}"

    elif question is '4':
        side = int(input("정사각형의 한 변의 길이를 입력해주세요 : "))
        return f"정사각형의 넓이는 : {cal_square(side)}"



def total():   
    
    while True:
        print('======도형 목록======'
        '\n 1. 원\n 2. 삼각형\n 3. 직사각형\n 4. 정사각형'
        '\n====================='
        )
        print(auto_calculator())

        again = input("또 하실꺼? y(es) or n(o) : ")
        if again is 'y':
            continue
        elif again is 'n':
            print("Bye bye ~_~ ")
            break

total()
        
