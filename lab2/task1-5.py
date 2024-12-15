def greet(name):
  return f'Привет, {name}!'
print(greet('Артем'))

def square(number):
  return number**2
print(square(13))

def max_of_two(x, y):
  if x > y:
    return x
  elif x < y:
    return y
  else:
    return 'Числа равны'
print(max_of_two(1,1), max_of_two(1,2), max_of_two(2,1))

def describe_person(name, age=30):
  s = f'Имя:{name}. Возраст:{age}'
  return s
print(describe_person('Василий', 69))

def is_prime(number):
  for x in range(2, int(number**0.5) + 1):
    if number % x == 0:
      return False
    return True
print(is_prime(17))