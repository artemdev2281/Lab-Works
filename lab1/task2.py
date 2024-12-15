z = int(input('Введите число: '))
while z <= 1:
  z = int(input('Введите другое число, большее 1: '))
else:
  for x in range(1, z + 1):
    print(x)