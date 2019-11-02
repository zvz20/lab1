alph = ("abcdefghijklmnopqrstuvwsyzabcdefghijklmnopqrstuvwsyz")
num=("1234567890")
encr = input("Enter a massage: ")
encr = encr+" "
key = int(input("Enter a key: "))
encr = encr.lower()
encr2 = ""
a=""
for letter in encr:
    position = alph.find(letter)
    pos = num.find(letter)
    newPosititon2 = pos + key
    newPosititon = position + key
    if letter in alph:
        if a != "":
            a=int(a)
            a=a+key
            a=str(a)
            encr2=encr2+a
            a=""

        encr2 = encr2 + alph[newPosititon]
    elif letter in num:
        a=a+letter
    else:
        if a != "":
            a=int(a)
            a=a+key
            a=str(a)
            encr2=encr2+a
            a=""
        encr2 = encr2 + letter

print("Your cipher is: ", encr2)
