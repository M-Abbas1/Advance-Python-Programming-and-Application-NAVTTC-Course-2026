from person_package import Person

class Teacher(Person):
    def __init__(self, name, age, email, subject, salary):
        super().__init__(name, age, email)
        self.subject = subject
        self.__salary = salary

    def get_role(self):
        return "Teacher"
    
    def get_summary(self):
        return f"Name : {self.name} | Age : {self.age} | Email : {self.email} | Subject : {self.subject}"
    
    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, value):
        if isinstance(value, (int, float)):
            self.__salary = value
            print("Salary Updated")
        else:
            print("Provide a valid salary input")
        



