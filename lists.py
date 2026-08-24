fruits=[]
print(type(fruits))

fruits=["apple","banana","mango","grapes"]
print(fruits[0]) 
print(fruits[:3])
print(fruits[::-1])
# 
# for a in range(len(fruits)):
    # print(fruits[a])

[print(fruit) for fruit in fruits]
a=[fruit for fruit in fruits]
print(a)

#Swapping the elements in the list
a=["ross","monica","chandler","joey","phoebe","rachel"]
a[0],a[3]=a[3],a[0]
print(a)

a.insert(2,"robert")
print(a)

a.pop(2)
print(a)

num=[34,3453,4,2,42,4,24,324,324]
print(max(num))

num.sort(reverse=True)