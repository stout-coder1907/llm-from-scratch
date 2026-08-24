a="hello","my","name","is","Sudhanshu"
print(a)

Employee={"Name":"Sudhanshu","Age":20,"Salary":20000}
print(Employee["Name"])

for x in Employee:
    print(Employee[x])

for x,y in Employee.items():
    print(x,y)

a = Employee.items()
print(a)
# 
a={"a":1,"b":2,"c":3}
a = sorted(a.values())
print(a)

a={}
for i in range(1,6):
    a[i]=i*i
print(a)

a = {2,3,4,4,5,3,3}
print(a)

for x in a:
    print(x)

s = ["apple","banana","mango","grapes"]
b =["guava","kiwi","orange","banana"]
c=['date','fig','grapes','kiwi','banana','mango']

d = set(s).intersection(set(b))
e= d.intersection(set(c))
print(e)

print(d.difference(e))