class Employee:
    def __init__(self,name,age,position,salary):
        self.name=name
        self.age=age
        self.position=position
        self.salary=salary
        class Developer(Employee):
            def __init__(self,name,age,position,salary,programming_language):
                super().__init__(name,age,position,salary)
                self.programming_language=programming_language
            def display_info(self):
                print(f"Name: {self.name}, Age: {self.age}, Position: {self.position}, Salary: {self.salary}, Programming Language: {self.programming_language}")
