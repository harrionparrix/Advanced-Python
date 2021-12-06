n=int(input("Enter number: "))
b=[n*i for i in range(1,11)]
a=str(b)
z=open("ques5file.txt","w")
z.write(a)
z.close()