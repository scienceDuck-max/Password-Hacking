#find the password

def findPassword(password):

    for i in range(10):
        if(password.count(i)>0):
            for k in range(0,8):
                if(i==password[k]):
                   print(str(i)+" is "+str(k)+ "th password!")

    #print(password.count(chr(97))) #find 'a'


    for i in range(97,123,1):
        if(password.count(chr(i))>0):
            #print(chr(i)+" is in password!")
            for k in range(0,8):
                if(chr(i)==password[k]):
                   print(chr(i)+" is "+str(k)+"th password")

pw1 = ['m','a','x',4,'s','e','n','a']#example
pw2 = ['i','l','o','v',3,'u',2,2]

print("Hacking pw1...")
findPassword(pw1)

print("Hacking pw2...")
findPassword(pw2)


