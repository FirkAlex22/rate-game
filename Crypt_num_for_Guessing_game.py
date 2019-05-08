def crypt(x):
    crypt_nom = ""
    keys = {
        "0":")", "1":"!", "2":"@",
        "3":"~","4":"$", "5":"%",
        "6":"_", "7":"^", "8":"&",
        "9":"*", "10":"("
            }
    for i in str(x):
        if i in keys:
            crypt_nom += keys[i]
    return crypt_nom
    
def decrypt(x):
    decrypt_nom = ""
    keys = {
        ")":"0", "!":"1", "@":"2",
        "~":"3", "$":"4", "%":"5",
        "_":"6", "^":"7", "&":"8",
        "*":"9"
            }
    for i in str(x):
        if i in keys:
            decrypt_nom += keys[i]
    return decrypt_nom
