
class AccountLockedError(Exception):
    pass


class LoginSystem:

    def __init__(self):
     self._password = "python@123"
   self._attempts = 3

    def login(self, password):
     try:
    if self._attempts =
    raise AccountLockedError("Account Locked!")

  if password == self._password:
  
     print("Login Successful!!")

   else:
     self._attempts -= 1
   print("Wrong Password")
    print("Remaining Attempts:", self._attempts)

   if self._attempts == 0:
    raise AccountLockedError("Account Locked!")

    except AccountLockedError as e:
     print(e)

   finally:
     print("Login Process Finished\n")


obj = LoginSystem()

obj.login("abc")
obj.login("123")
obj.login("test")
obj.login("python@123")