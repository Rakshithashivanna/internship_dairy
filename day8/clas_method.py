from abc import ABC,abstractclassmethod

class A(ABC):
    x=10
    @abstractclassmethod
    def method1(self):
        print("Method 1")
    @classmethod
    def increment(self):
        self.x+=1
    #static method
    def dispaly():
        print("add")
    
class B(A):
    def method1(self):
        print("Method of b")

obj=B()
obj.method1()