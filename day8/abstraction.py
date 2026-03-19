from abc import ABC,abstractclassmethod

class A(ABC):
    @abstractclassmethod
    def method1(self):
        print("Method 1")
    
class B(A):
    def method1(self):
        print("Method of b")

obj=B()
obj.method1()