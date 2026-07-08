def is_year_leap (y):
    return True if y % 4 == 0 else False

s = int(input("Введите год: "))
f = is_year_leap (s)
print (f)
