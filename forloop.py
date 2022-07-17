# for i in lst:
#     print(i)

# print(range(10))

# two_table = range(2,21,2)
# print(list(two_table))

#a = 'akshat'

a = int(input('enter a number:'))

if a > 1:
    for i in range(2, 0):
        if(a % i == 0):
            print('it is a prime number')
        else:
            print('not a prime number')
else:
    print('not a prime number')
                

