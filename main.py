class Parent:
    def __init__(self,Name,  FatherName):
        self.__Name = Name
        self.FatherName = FatherName
        # print(self.__Name)

p1 = Parent("eshan", "rahaman")

print(p1.__Name)