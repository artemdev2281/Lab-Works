class Vehicle:
  def __init__(self, make, model):
    self.make = make
    self.model = model

  def get_info(self):
    return f'Make: {self.make}, Model: {self.model}'

class Car(Vehicle):
  def __init__(self, make, model, fuel_type):
    super().__init__(make, model) #вызов конструктора родительского класса
    self.fuel_type = fuel_type

  def get_info(self):
    res = super().get_info()
    return res + f", Fuel type: {self.fuel_type}"

Lada1 = Vehicle('Lada', '2107')
print(Lada1.get_info())
Lada2 = Car('Lada', '2109', 'petrol')
print(Lada2.get_info())