class father:
    def __init__(self,name,surname):
        self.father_name=name
        self.surname=surname
    def display_father_name(self):
        print(self.father_name)
    def display_surname(self):
        print(self.surname)
class son(father):
    def __init__(self, name, surname,father_name):
        super().__init__(father_name, surname)
        self.name=name
    def display_name(self):
        print(self.name)
obj=son("Abc","B","Cad")
obj.display_father_name()
obj.display_surname()
obj.display_name()