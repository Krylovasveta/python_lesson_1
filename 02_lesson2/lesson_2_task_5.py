def month_to_season(m):

    if m in z:
        print("Зима")
    elif m in v:
        print("Весна") 
    elif m in l:
        print("Лето")
    elif m in o:
        print("Осень")
    else:
        print("Такого месяца не существует")

z = [12, 1, 2]
v = [3, 4, 5]
l = [6, 7 ,8]
o = [9, 10, 11]

s = int(input("Введите номер месяца: "))   

s1 = month_to_season(s)