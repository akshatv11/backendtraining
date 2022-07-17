# for i in lst:
#     print(i)

# print(range(10))

# two_table = range(2,21,2)
# print(list(two_table))

#a = 'akshat'

a = int(input('enter a number:'))

for i in range(2,a):
    if a % i == 0:
        print('not prime')
        break
else:
    print("it is a prime number")
    

