# Q.2 Create two classes : Person class having attributes name, age and Company class
# having attributes cname , location. The class Employee will inherited from both
# classes having attributes salary, skill. Display all information of the employee.

# Define the Person class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Define the Company class
class Company:
    def __init__(self, Cname, location):
        self.Cname = Cname
        self.location = location

# Define the Employee class inheriting from both Person and Company
class Employee(Person, Company):
    def __init__(self, name, age, Cname, location, salary, skill):
        # Initialize the parent classes
        Person.__init__(self, name, age)
        Company.__init__(self, Cname, location)
        # Initialize Employee-specific attributes
        self.salary = salary
        self.skill = skill

    # Method to display all employee information
    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Company Name: {self.Cname}")
        print(f"Company Location: {self.location}")
        print(f"Skill: {self.skill}")
        print(f"Salary: {self.salary}")

# Example usage
employee = Employee(
    name="Aniket",
    age=20,
    Cname="TCS",
    location="Pune",
    salary=200000,
    skill="Python"
)

# Display the employee's information
employee.display_info()
