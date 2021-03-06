import getpass

# Input Type
print("Will you encode? or decode.")
print("1. enc")
print("anything number. dec")
encordec = int(input("1 or anything int: "))
if encordec==1:
    print("ENC selected. What's your pin.")
    pin = int(getpass.getpass("Your Pin: "))
    pinag = int(getpass.getpass("Your Pin Again: "))

    if not pin==pinag:
        print("pin, pinagain isn't same.")
        input()
        exit()

    enctext = input("enc text: ")
    print(f"{enctext} encoding..." )
    c = ''
    ac = 0
    encrypted = ''
    for i in range(len(enctext)) :
        c = enctext[i]
        ac = ord(c)
        ac += pin + (pin + pin ** i) % 1114112
        c = chr(ac)
        encrypted += c
    print("result: " + str(encrypted))
    input()
    exit()
else:
    print("You Selected Decode.")
    pin = int(getpass.getpass('The pin You wrote back then: '))
    pinagain = int(getpass.getpass('The pin You wrote back then Again: '))

    if not pin==pinagain:
        print("pin, pinagain isn't same.")
        input()
        exit()
    dtext = input("decode text: ")
    print(f"I will decode \"{dtext}\" ")
    decrypted = ""
    c = ""
    for i in range(len(dtext)) :
        c = dtext[i]
        ac = ord(c)
        ac -= pin + (pin + pin ** i) % 1114112
        c = chr(ac)
        decrypted += c
    print("result: " + str(decrypted))
    input()
    exit()
