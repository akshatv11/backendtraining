# def greet():
#     print('hello world')
# greet()
# var = greet()
# print(var)




# factorial using function
# def factorial(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact = fact * i
#     return fact

# fact_5 = factorial(5)
# fact_6 = factorial(6)

# print(fact_5)
# print(fact_6)


# def table(n):
#     t = 1
#     for i in range(1,11):
#         t = n * i
#         print(t)

# table_10 = table(10)
# print('#' * 10)
# table_11 = table(11)






# def list():
#     a = ['a', 'b', 'c']
#     return a

# x = list()
# print(x)





# def check(a):
#     if a.isupper():
#         return 'true'
#     else:
#         return 'false'


# a = check('AKSHAT')
# print(a)






# def ascii(k):
#     s = int(0)
#     for i in k:
#         s = s + ord(i)
#     return s

# a = ascii('AKSHAT')
# print(a)

# def ascii(input_string):                    another approach
#     return ascii(map(ord,input_string))




# def generate(username, password):
#     return(username[0:4] + password[-4::])

# k = generate('akshat', '23456')
# print(k)



# def count_next_char(input_string):
#     total = 0
#     for i in range(len(input_string)-1):
#         if(ord(input_string[i]) == ord(input_string[i+1])+1):
#             total += 1
#     return total




# print(count_next_char('abba'))




    
def a(lst):
    for i in lst:
        if i % 2 == 0:
            print(i)

lst = [100,57,56,44,12,13]

print(a(lst))












