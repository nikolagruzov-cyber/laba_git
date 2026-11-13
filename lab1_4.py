import sys
 
num = [-100, -2, 0, 6, 600, 10**4, 10**10]
size_num = [sys.getsizeof(x) for x in num]
print(*num, sep='\t')
print(*size_num, sep='\t')

string = ['', ' ', 'b', 'b'*5, 'b' * 50]
size_str = [sys.getsizeof(x) for x in string]
print(*string, sep='\t')
print(*size_str, sep='\t')
