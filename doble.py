a = list(input("Enter a sth: "))
len_a = len (a)
b = " "
for i in a:
    if i is not " ":
        b = b + i + i
    else:
        b = b + i
print(b)