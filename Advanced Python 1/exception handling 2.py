#exception handling
from typing import Type


while(True):
    try:
        a=int(input("Enter a number:  "))
        c=1/a
    except Exception as e:
        print("Exception occured")
        print(f"{e}")
    except ZeroDivisionError as e:
        print("Can't divide by 0")
        # print(f"{e}")
    except TypeError as e:
        print("Can't do it ")
        # print(f"{e}")
print("Thank you for playing")
