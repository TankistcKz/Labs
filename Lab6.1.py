class UserAccount():
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def set_password(self, new_password):
        self.password = new_password

    def check_password(self, password):
        if self.password == password:
            return True
        else: return False



user = UserAccount('TankistcKz', 'gmail.com', '12345')
user.set_password('123321')
print(user.check_password('12345'))
print(user.check_password('123321'))