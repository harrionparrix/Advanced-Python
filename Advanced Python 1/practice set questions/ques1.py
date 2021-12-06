for i in range(1,4):
    try:
        a=open(f"{i}.txt","r")
        print(a.read())
    except Exception as e:
        print(f"File {i} is not found")
