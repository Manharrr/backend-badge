# lst=[2,6,3,1,6,7,89,67,3,4,17]
# p=lst[1]=9
# print(lst)

# # print(lst)

# # lst.append(29)
# # print(lst)
# # lst.extend([99,999,999,88])
# # print(lst)
# # lst.insert(0,99)
# # lst.remove(17)
# # lst.pop(1)
# # lst.clear()
# # lst.sort()
# # a=lst[::-1]
# # print(a)
# a=lst.copy()
# print(lst)

# a=(2,6,3,1,6,7,89,67,3,4,17)
# print(type(a))


# sq=[i *i for i in range(0,10) if i%2 ==0]
# print(sq)
# t=(1,2,3,)
# lst= list(t)
# lst.extend([1,77,8])
# ans=tuple(lst)
# print(ans)

# stud={
#     "name":"manhar",
#     "age":22
    
#     }
# print(stud.get("age"))
# a=stud["place"]="tirur"
# print(stud)




students = {
    "s1": {
        "name": "Manhar", 
        "age": 21,
        "marks": {
            "python": 85,
            "sql": 78,
            "ml": 90
        }
    },
    "s2": {
        "name": "Akhil",
        "age": 22,
        "marks": {
            "python": 88,
            "sql": 82,
            "ml": 75
        }
    }
}
# print(students["s2"]["marks"].get("sql"))

# def decor (func):
#     def wrapper():
#         return func().replace("i","*")
#     return wrapper

# @decor
# def one ():
#     return("This code defines a class Employee with a class variable raise_amount")
    
# print(one())



# def decor(func):
#     def wrapper():
#         a=func().capitalize()
#         return a
        
#     return wrapper



# @decor
# def one():
#     return "hi my name is manhar i love mashook"
# print(one())

# class employee:
#     def one(self):
#         print("hyyyy")
    
# a=employee()
# a.one()

# class Students:
#     def __init__(self ,name, age):
#         self.name=name
#         self.age=age
        
#     def intro(self):
#         return f"your name is {self.name},and {self.age}year old"

# stud1=Students("manhar",21)
# stud2=Students("masook",23)
# print(stud1.intro())
# print(stud2.intro())






# class parent:
#     def first(self):
#         print('iam parent')
# class child(parent):
#     def second(self):
#         print("iam child")
        
        
    
# a=child()
# a.second()
# a.first()

# class gparent:
#     def house(self):
#         print("gp house")
        
# class parent(gparent):
#     def car(self):
#         print("carrr")
# class child(parent):
#     def bike (self):
#         print("bikeeeee")
        
# c=child()
# c.house()
# c.car()

# class animal:
#     def sound(self):
#         print("animal make sound")
# class dog(animal):
#     def sound(self):
#         print("bwwwww")
# class cat(animal):
#     def sound(self):
#         print("meowww")
# a=animal()
# b=dog()
# c=cat()
# a.sound()
# b.sound()
# c.sound()

# from abc import ABC,abstractmethod

# class parent(ABC):
#     @abstractmethod
#     def one(self):
#         pass

# class  child(parent):
#     def one(self):
#         print("hyy")
# c=child()
# c.one()\

# lst=[1,2,3,4]
# it=iter(lst)
# print(next(it))
# print(next(it))

# def gen():
#     yield 1
#     yield 2
# g=gen()
# print(next(g))
# print(next(g))
# print(next(g))

# def gen ():
#     yield 1
#     yield 6
# g=gen()
# print(next(g))
# print(next(g))
    
# num=[12,4,3,2,6,8]
# even=filter(lambda x: x%2==0,num)
# print(list(even))

# mp=map(lambda x :x +1,num)
# print(list(mp))

# names = ["manhar", "akhil", "anu"]

# res=map(str.upper, names)
# print(list(res))

# from functools import reduce
# sum= reduce(lambda x,y : x+y,num)
# print(sum)

# text = "hello world python"

# words = text.split()
# print(words)


text = "hello world python"

words=text.split()
final=[]

for  i in words:
    rev=""
    for alph in i:
        
        rev=alph +rev
    final.append(rev)
result= " ".join(final)
print(result)
        
        
    
    
    
 
    



    







































    