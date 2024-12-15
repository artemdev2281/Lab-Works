try:
    f = open('not_example.txt', 'r', encoding='utf-8')
    print(f.read())
except FileNotFoundError:
    print('Такого файла не существует')

