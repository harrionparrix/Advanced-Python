try:
    i=int(input("Enter a number: "))
    c=1/i
except Exception as e:
    print(e)
    exit()
finally:
    print("We are done")  #will print regardless of what is in except

print("Thanks again") #wont print if exit() in except