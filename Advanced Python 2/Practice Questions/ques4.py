def div(num):
    if(num%5==0):
        return True
    else:
        return False

l=[1,2,5,9,80,12,15]
a=list(filter(div,l))
print(a)