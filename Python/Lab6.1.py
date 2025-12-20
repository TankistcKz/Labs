class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    @property
    def password(self):
        pass
    
    @password.setter
    def set_password(self, new_password):
        self.__password = new_password

    def check_password(self, password):
        return self.__password == password



user = UserAccount('TankistcKz', 'gmail.com', '12345')
print(user.check_password('4'))
print(user.check_password('12345'))
user.set_password = '123321'
print(user.check_password('123321'))
print(user.__password)