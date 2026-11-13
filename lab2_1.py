list=[1,2,3,4,5,6]
tuple=(1,2,3,4,5,6)
print("Начальные данные")
print(id(list))
print(type(list))
print(id(tuple))
print(type(tuple))

list[5]=7
tuple=(1,2,3,4,5,7)
print("Измененные данные")
print(id(list))
print(id(tuple))
