
# coding: utf-8
# this is a prime number detect file
#x is input number, then return the list that contains prime numbers.

def prime_num_detect(x):
    lists = []
    if type(x) == int and int(x) > 0:
        for y in range(1,x+1):
            for i in range(2,y):
                if y % i == 0:
                    break
            else:
                lists.append(y)
        print(lists)
    else:
        print('input number must be integer and more than 0')

x = input()
x = int(x)

prime_num_detect(x)






