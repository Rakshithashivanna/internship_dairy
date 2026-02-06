class father:
    def __init__(self,name,surname):
        self.father_name=name
        self.surname=surname
    def display_father_name(self):
        print("The father name is",self.father_name)
    def display_surname(self):
        print("The surname is",self.surname)

class mother:
    def __init__(self,eye_color,mother_name):
        self.eye_color=eye_color
        self.mother_name=mother_name
    def display_eye_color(self):
        print(self.eye_color)
    def display_mother_name(self):
        print("The mother name is",self.mother_name)
class son(father,mother):
    def __init__(self, name, surname,father_name,eye_color,mother_name):
        father.__init__(self,father_name, surname)
        mother.__init__(self,eye_color, mother_name)
        self.name=name
    def display_name(self):
        print("The son name is",self.name)
obj=son("Abc","B","Cad","black","efg")
obj.display_father_name()
obj.display_mother_name()
obj.display_surname()
obj.display_name()