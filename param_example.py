def test(a, b=10, c=100, *values):
    # print(a * b * c)
    for value in values:
        print(value*a+b)


# # 기본 형태
# test(10, 20, 30)
# # 키워드 매개변수로 모든 매개변수를 지정한 상태
# test(a=10, b=100, c=200)
# # 키워드 매개변수로 모든 매개변수를 마구잡이로 지정한 형태
# test(c=10, a=100, b=200)
# # 키워드 매개변수로 일부 매개변수만 지정한 형태
# test(10, c=200)
# print()
test(10, "즐거운", "파이썬", "프로그래밍")

