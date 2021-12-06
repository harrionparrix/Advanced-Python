def greater_than_5(num):
    if num>5:
        return True
    else:
        return False

l=[1,3,4,5,6,7,86,53,12]
print(list(filter(greater_than_5,l)))

#Syntax: list(filter(function,list))