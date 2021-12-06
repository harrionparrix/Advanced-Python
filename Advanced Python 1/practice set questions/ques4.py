try:
    a=int(input("Enter 1 number: "))
    b=int(input("Enter 2 number: "))
    c=a/b
    print(c)
except ZeroDivisionError as e:
    print("INFINITE")