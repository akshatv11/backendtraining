try:
    print(5/b)
except ZeroDivisionError:
    print('you cant divide by zero')
except:
    print('you cant divide by string')
