def d30 (x):
    return True if x < 30  else False

def d3 (y):
    return True if y % 3 == 0 else False

lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]

for i in lst: 
    if d30 (i)  and d3 (i):
        print(i)