first_name = 'hello'
last_name = 'world'

# if(first_name=='hello' and last_name=='world'):
#     print('true')
# else:
#     print('false')

# if(fname=='hello' and not last_name=='wrld'):
#     print('true using not operator')  
# else:
#     print('false')

# if(first_name=='hell' or last_name=='world'):
#     print('any one is correct')
# else:
#     print('incorrect')

# if 'akshat' in ['a','b','c']:
#     print('akshat is in the list')
# elif 'p' in 'akshat':
#     print('akshat has p in spelling')
# elif 'k' in 'aakashat':
#     print('aakashat ha k in spelling')
# else:
#     print('nothing is there')


# s = input("ENter a string value ")

# for i in s:
#     if(ord(i)%2==0):
#         print(i ,' is in even ascii')

# for i in range(len(s)):
#     if(ord(s[i])%2==0):
#         print(s[i] ,' is in even ascii')

# n = int(input('enter number '))
# lst1 = []
# for i in range(n):
#      num = input('enter a number ')
#      lst1.append(num)
    
# print(lst1)
# print(type(lst1))

# for i in range(n):
#     print(lst1[i])

a = int(input('enter number '))
map_ = {
    'str' : [],
    'int' : [],
    'float' : []
    }

for i in range(a):
    datatype = input("Enter a datatype ")
    value = input("input a value ")
    if datatype == 'str':
        map_['str'].append(value)

    elif datatype == 'int':
        map_['int'].append(value)
    
    elif datatype == 'float':
        map_['float'].append(value)
    
   
print(map_)