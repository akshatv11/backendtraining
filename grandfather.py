class grandfather:
    def __init__(self,name):
        self.name = name

    def same(self):
        print(self.name)

class father(grandfather):
    def __init__(self, name):
        super().__init__(name)

    def same(self):
        print(self.name)

class boy(father):
    def __init__(self, name):
        super().__init__(name)
       

d = boy('akshat')
d.same()
