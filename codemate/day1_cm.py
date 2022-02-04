print('======도형 목록======'
'\n 1. 원'
'\n 2. 삼각형'
'\n 3. 직사각형'
'\n 4. 정사각형'
'\n====================='
)

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
    question = int(input("도형 목록에서 넓이를 계산할 도형의 번호를 입력해주세요 : "))

    print(type(question))
    if question is 1:
        radius = int(input("원의 반지름을 입력해주세요 : "))
        return cal_circle(radius)
    # elif question 

print(auto_calculator())