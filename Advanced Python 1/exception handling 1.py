#exception handling
while(True):
    print("Press q to exit")
    a=input("Enter a number:  ")
    if a == "q":
        break
    try:
        a=int(a)
        if a>5:
            print("the number is greater than 5")
    except Exception as e:
        print(f"The error was: {e}")
    
print("Thank you for playing")
