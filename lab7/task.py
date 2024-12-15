class Employee():
  def __init__(self, name, id):
    self.name = name
    self.id = id

  def get_info(self):
    return f'Employee name: {self.name}, ID: {self.id}'


class Manager(Employee):
  def __init__(self, name, id, department):
    Employee.__init__(self, name, id)
    self.department = department

  def get_info(self):
    res = super().get_info()
    return res + f', Department: {self.department}'

  def manage_project(self):
    return f'{self.name} is responsible for project management in {self.department} department'


class Technician(Employee):
  def __init__(self, name, id, specialization):
    Employee.__init__(self, name, id)
    self.specialization = specialization

  def get_info(self):
    res = super().get_info()
    return res + f', Specialization: {self.specialization}'

  def perform_maintenance(self):
    return f'{self.name} is responsible for performing maintenance in {self.specialization} specialization'


class TechManager(Manager, Technician):
  def __init__(self, name, id, department, specialization):
    Manager.__init__(self, name, id, department)
    Technician.__init__(self, name, id, specialization)
    self.employees = []

  def skills(self):
    return f'{self.name} is responsible for project management in {self.department} department and performing maintenance in {self.specialization} specialization'

  def add_employee(self, employee):
    self.employees.append(employee)

  def get_team_info(self):
    if len(self.employees) == 0:
      return f'There are no employees in the team'
    return [employee.get_info() for employee in self.employees]

test1 = Employee('Vasiliy', '228')
print(test1.get_info())

test2 = Manager('Alex', '229', 'dep')
print(test2.get_info())
print(test2.manage_project())

test3 = Technician('Nick', '230', 'spec')
print(test3.get_info())
print(test3.perform_maintenance())

test4 = TechManager('Max', '231', 'dep', 'spec')
print(test4.get_info())
print(test4.skills())
test4.add_employee(test1)
test4.add_employee(test2)
test4.add_employee(test3)
print(test4.get_team_info())