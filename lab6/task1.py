class UserAccount:
  def __init__(self, username : str, email : str, password : str):
    self.username = username
    self.email = email
    self.__password = password
  def get_password(self):
    return self.__password
  def set_password(self):
    check = 0
    while check != self.__password:
      check = input('Введите текущий пароль: ')
      if check != self.__password:
        print('Введен неверный пароль')
    else:
      new_password = input('Введите новый пароль: ')
      self.__password = str(new_password)
  def check_password(self, password):
    if password == self.__password:
      return True
    else:
      return False
user = UserAccount('Artem', 'jgs@gmail.com', '12345678')
print(user.get_password())
user.set_password()
print(user.get_password())
print(user.check_password('1228'))
print(user.check_password('1234'))