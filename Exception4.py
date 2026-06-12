
class UnderAgeError(Exception):
    pass

class InvalidAgeError(Exception):
    pass


class AgeVerification:

    def set_age(self, age):
  try:
    if age < 0:
   raise ValueError("Age cannot be negative")

    elif age < 18:
   raise UnderAgeError("Under Age")

    elif age > 100:
  raise InvalidAgeError("Invalid Age")

   else:
    print("Valid age!")

 except ValueError as e:
    print("ValueError:", e)

except UnderAgeError as e:
    print("UnderAgeError:", e)

  except InvalidAgeError as e:
     print("InvalidAgeError:", e)

   finally:
   print("Age verification completed")


a = AgeVerification()

a.set_age(-5)
a.set_age(15)
a.set_age(120)
a.set_age(25)