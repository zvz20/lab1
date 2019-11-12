alph = ("abcdefghijklmnopqrstuvwsyzabcdefghijklmnopqrstuvwsyz")
alph2 = ("абвгґдеєжзиіїйклмнопрстуфхцчшщьюя")
num=("1234567890")
encr = input("Enter a massage: ")
encr = encr+" "
key = 1
encr = encr.lower()
i = 0
while i < 1:
    i -= 1
    alph = ("abcdefghijklmnopqrstuvwsyzabcdefghijklmnopqrstuvwsyz")
    alph2 = ("абвгґдеєжзиіїйклмнопрстуфхцчшщьюя")
    num=("1234567890")
    encr = input("Enter a massage: ")
    encr = encr+" "
    key = 1
    encr = encr.lower()
    encr2 = ""
    a=""
    for letter in encr:
        position = alph.find(letter)
        pos = num.find(letter)
        pos2 = alph2.find(letter)
        newPosititon3 = pos2 + key
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
        elif letter in alph2:
            if a != "":
                a=int(a)
                a=a+key
                a=str(a)
                encr2=encr2+a
                a=""
    
            encr2 = encr2 + alph2[newPosititon3]
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
