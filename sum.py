total = 0
for i in range(0,101):
    octal = "{:o}".format(i)
    if octal.count("0") == 1:
        print(i, octal)
        total += i
print("합계 :", total)

total = 0
# print([i for i in range(0, 101) if "{:o}".format(i).count("0") == 1])


