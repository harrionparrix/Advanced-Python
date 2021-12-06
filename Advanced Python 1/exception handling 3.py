def increment(num):
    try:
        return int(num)+1
    except:
        raise ValueError("Error has occured")
    
a=increment("000asd")
print(a)