class Student:
    def __init__(self,id,fName):
        # print('hello')
        self.fName = fName
        self.id = id

    def StudentInfo(self):
        print(self.id, self.fName)
    
    # fName = 'akshat'

# constructor= (memory allocate karna=> object)
# object
#object = className()


s1 = Student('john',1)
s1.StudentInfo()
# print(s1.fName, s1.id)

s2 = Student('utkarsh',2)
# print(s2.fName,s1.id)
s2.StudentInfo()


