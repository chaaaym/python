total = 0
for i in range(1,101):
    binary = "{:b}".format(i)
    if binary.count("0") == 1:
        print(i, ":", binary)
        total += i
print("합계:", total)

total = 0
for i in range(1,101):
    binary = "{:b}".format(i)
    if binary.count("0") == 1:
        print(i, ":", binary)
        total += i
print("합계:", total)

output = [i for i in range(0, 101) if "{:b}".format(i).count("0") == 1]
for i in output:
    print("{} : {}".format(i, "{:b}".format(i)))
print("합계:", sum(output))