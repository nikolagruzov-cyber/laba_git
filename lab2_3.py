import timeit
list=[1,20,300,2000]
my_set=set(list)
print("Тест 1")
print(timeit.timeit("300 in list",number=1000000,globals=globals()))
print(timeit.timeit("300 in my_set",number=1000000,globals=globals()))
print(timeit.timeit("3 in list",number=1000000,globals=globals()))
print(timeit.timeit("3 in my_set",number=1000000,globals=globals()))

list1=[1,20,300,4,10,100,111,11432,2930,2000]
my_set1=set(list1)
print("Тест 2")
print(timeit.timeit("300 in list1",number=1000000,globals=globals()))
print(timeit.timeit("300 in my_set1",number=1000000,globals=globals()))
print(timeit.timeit("3 in list1",number=1000000,globals=globals()))
print(timeit.timeit("3 in my_set1",number=1000000,globals=globals()))

list2=[1,20,300,4,10,100,111,11432,2930,2000,10000,10023,100000,120023034]
my_set2=set(list1)
print("Тест 3")
print(timeit.timeit("300 in list2",number=1000000,globals=globals()))
print(timeit.timeit("300 in my_set2",number=1000000,globals=globals()))
print(timeit.timeit("3 in list2",number=1000000,globals=globals()))
print(timeit.timeit("3 in my_set2",number=1000000,globals=globals()))
