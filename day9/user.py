class User:

    def __new__(cls, *args, **kwargs):
        print("Object is being created")
        print(cls)
        return super().__new__(cls)   

    def __init__(self, name):
        print("Object is initialized")
        self.name = name



u1 = User("Rakshitha")
u2=User("Nish")
