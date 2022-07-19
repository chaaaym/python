# 리스트를 선언합니다.
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for number in numbers:
    if number % 2 == 0:
        print(number, "는 짝수입니다")
    else:
        print(number, "는 홀수입니다")