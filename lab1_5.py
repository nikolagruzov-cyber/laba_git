import timeit
s1="s1=\n s[0]+s[1]+s[2]+s[3]+s[4]+s[5]+s[6]+s[7]+s[8]+s[9]+s[10]+s[11]+s[12]+s[13]+s[14]+s[15]+\n
s[16]+s[17]”
s2=“s2=\n f’{s[0]}{s[1]}{s[2]}{s[3]}{s[4]}{s[5]}{s[6]}{s[7]}{s[8]}{s[9]}{s[10]}{s[11]}{s[12]}{s[13]}\n
{s[14]}{s[15]}{s[16]}{s[17]}’”
s3 = “s3 = ‘{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}’.format(*s)”
s = [“Круто”, “ “, “Классно”, “ “, “Потрясно”, “ “, “и”, “ “, “Весело”, “!”, “”, “”, “”, “”, “”, \n
“”, “”, “”]

print(“Конкатенация: “, timeit.timeit(s1, globals=globals(), number=1000000))
print(“f-строка:     “, timeit.timeit(s2, globals=globals(), number=1000000))
print(“format():     “, timeit.timeit(s3, globals=globals(), number=1000000))
