a=[3,2,5,7,8,3,12,8,4,2,34,1343,77]


# b=[]
# for item in a:
#     if item%2==0:
#         b.append(item)
# print(b)

print([i for i in a if i%2==0])

t=[1,1,1,1,1,1,2,4,7,5,9,10]
s={i for i in t}
print(s)