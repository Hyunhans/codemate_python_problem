def check_alias():
    words = input("단어를 입력해주세요 : ")

    for i in range(len(words) // 2 ):
        if words[i] == words[0 - 1 - i]:
            return print(f"{words}는 회문입니다.")

        else:
            return print(f"{words}는 회문이 아닙니다.")

# def regames():
#     check_alias()
#     question = input('한판더 하시겠습니까 ? Y or N : ')
#     while question == 'y':
#         question = input('한판더 하시겠습니까 ? Y or N : ')
#         check_alias()
#         continue

# print(check_alias())

print(regames() )