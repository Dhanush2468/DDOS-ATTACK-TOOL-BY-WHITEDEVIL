
from random import choice



def protect(message, salt):
   
    eData = ''
    salt = list(salt)
    saltChars = []

  
    for char in message:
        if not char in saltChars:
            saltChars.append(char)

    
    for index, secretChar in enumerate(message):
        for _ in range(int(salt[index])):
            eData += choice(saltChars)
        eData += secretChar

    return eData



def unprotect(message, salt):
  
    p = 0
    dData = ''

    
    for secretSalt in salt:
        message = message[int(secretSalt) + p:]
        
        if not message:
            break

        dData += message[0]
        p = 1

    return dData
