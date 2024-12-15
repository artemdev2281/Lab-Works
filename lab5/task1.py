class Book:
    title = 'Десять негритят'
    author = 'Агата Кристи'
    year = '1939'
    def get_info(self):
        return f'Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}'
z = Book().get_info()
print(z)