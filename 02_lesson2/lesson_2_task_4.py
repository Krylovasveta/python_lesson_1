def check_num (n, x):
    return True if n % x == 0 else False

def fizz_buzz (n1):
    
    if check_num (n1, 3) :
        if check_num (n1, 5):
            print ('FizzBuzz')
        else:
            print ('Fizz')
    else:
        if check_num (n1, 5):
            print ('Buzz')
        else:
            print (n1)


s = int(input("Введите число: "))

for i in range(1,s+1):
    fizz_buzz (i)
