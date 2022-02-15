# def solution(a, b):
#     c = sorted(a)
#     d = sorted(b)
#     print(c)
#     print(d)
#     if c != d:
#         for i in range(len(b)):
#             print(c[i], d[i])
#             if c[i] != d[i]:
#                 print(c[i])

def solution(a, b):
    for i in b:
        if i in a:
            a.remove(i)
    return a

        
print(solution(['곰','문','금비','나무','별'],['별','나무']))