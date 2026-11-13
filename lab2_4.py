import sys
my_list=[1,2,3,4,5]
my_tuple=(1,2,3,4,5)
my_set={1,2,3,4,5}
my_dict={1:"one",2:"two",3:"three",4:"four",5:"five"}
print(sys.getsizeof(my_list))
print(sys.getsizeof(my_tuple))
print(sys.getsizeof(my_set))
print(sys.getsizeof(my_dict))
