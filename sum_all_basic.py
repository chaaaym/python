# 두 개의 값을 입력 받아서 첫 번째 값에서 두 번째 값까지의 합계를 구해 봅시다

start = int(input("첫 번째 값을 입력하시오> "))
end = int(input("두 번째 값을 입력하시오> "))
def sum_all(start, end):
    output = 0
    for i in range(start, end + 1):
        output += i
  
    return output

print("합계:", sum_all(start, end))
