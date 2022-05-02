import getpass

# Input Type
print("Will you encode? or decode.")
print("1. enc")
print("anything number. dec")
try: 
  encordec = int(input("1 or anything: "))
except:
  print("wrong input")
  input()
  exit()
if encordec==1
  print("ENC selected. What's your pin.")
  pin = getpass.getpass("Your Pin: ")
  pinag = getpass.getpass("Your Pin Again: ")
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
        ac += pswd + (pswd + pswd ** i) % 1114112
        c = chr(ac)
        encrypted += c
    print("result: " + str(encrypted))
    input()
    exit()
else:
  print("You Selected Decode.")
  pswd = int(getpass.getpass('The pin You wrote back then: '))
  pswdagain = int(getpass.getpass('The pin You wrote back then Again: '))

  if not pswd==pswdagain:
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
      ac -= pswd + (pswd + pswd ** i) % 1114112
      c = chr(ac)
      decrypted += c
  print("result: " + str(decrypted))
  input()
  exit()
  
