z = int(input('Введите число: '))
if z > 1:
  for x in range(1, z + 1):
    print(x)
else:
  for x in range(1, z - 1, -1):
    print(x)