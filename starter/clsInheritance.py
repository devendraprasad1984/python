class schoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Initialise school member: ", self.name)

    def tell(self):
        print("Name:", self.name, "Age:", str(self.age))


class teacher:
    def __init__(self, name, age, salary):
        schoolMember.__init__(self, name, age)
        self.salary = salary

    def tell(self):
        schoolMember.tell(self)
        print("Salary:", str(self.salary))


class student:
    def __init__(self, name, age, marks):
        schoolMember.__init__(self, name, age)
        self.marks = marks

    def tell(self):
        schoolMember.tell(self)
        print("Marks:", str(self.marks))


# end



t = teacher("Vishal", 36, 352353)
s = student("Devendra", 31, 224)
members = [t, s]
for mem in members:
    mem.tell()
