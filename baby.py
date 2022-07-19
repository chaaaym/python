baby = {"사람" : "아기",
            "개" : "강아지",
            "말" : "망아지",
            "곰" : "능소니",
            "소" : "송아지" }

while (True) :
    animal = input(str(list(baby)) + " 중 좋아하는 동물은? ")
    if animal in baby :
        print("<%s> 의 새끼 이름은 <%s> 입니다." % (animal, baby.get(animal)))
    elif animal == "끝" :
        break
    else :
        print("그런 동물이 없습니다.")