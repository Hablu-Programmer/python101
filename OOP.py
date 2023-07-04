# class ClassName:
#     def InstanceMethod(self):
#         print("hello Instance Method")
#
#     @classmethod
#     def ClassMethod(cls):
#         print("This Is Class Method")
#
#     @staticmethod
#     def staticMethod():
#         print("This Is staticmethod")
#
# v1 = ClassName()
# v1.InstanceMethod()
#
# ClassName.ClassMethod()
#
# ClassName.staticMethod()



#Polymorphism

class Vehicle:
    def __init__(self,Model, Brand, Component, ):
        self.Model = Model #instance Var  #public
        self.Brand = Brand
        self.Component = Component



class Plane(Vehicle):
    pass

class Car(Vehicle):
    pass


class Bike(Vehicle):
    pass

v1 =  Vehicle("hdd", "New Model", "new Component")



#
# p1 = Plane("Hablu420", "Hablu", "All Component")
#
# c1 = Car("BMW", "E221", "Main Component")
#
#
# B1 = Bike("RTR", "001", " Component")
#
# print(p1.Brand, p1.Model, p1.Component)
#
# print(c1.Model, c1.Brand, c1.Component, )
#
# print(B1.Brand, B1.Model, B1.Component)


