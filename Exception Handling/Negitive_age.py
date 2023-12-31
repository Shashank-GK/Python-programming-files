# This program will raise an exception if the user enters a negative number for age.
# The program will also raise an exception if the user enters a number greater than 150 for age.


class NegativeAgeException(Exception):
    pass


def stage(age):
    if age < 0:
        raise NegativeAgeException("Age should not be Negative")
    elif age >= 0 and age < 13:
        print("Kid")
    elif age >= 13 and age < 20:
        print("Teen")
    elif age >= 20 and age <= 50:
        print("Young")
    else:
        print("Old")


age = int(input("Enter Your Age"))

try:
    stage(age)
except NegativeAgeException as e:
    print(e)
