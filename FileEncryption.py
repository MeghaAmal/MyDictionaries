
# dictionary with encrypted values for A-Z and a-z
code_encrypt_dictionary = { "A":"2",
                            "B":"-","C":"%","D":"@","E":"3","F":"#","G":"8","H":"g","I":"p","J":"y","K":"7",
                            "L":"`","M":"{","N":"f","O":"+","P":"1","Q":"m","R":"q","S":"^","T":"[","U":"6",
                            "V":";","W":"*","X":"?","Y":"u","Z":"(","a":"o","b":"4","c":"]","d":"r","e":"&",
                            "f":"_","g":"9","h":"k","i":")","j":"5","k":"e","l":"d","m":">","n":"!","o":"}",
                            "p":"|","q":"c","r":"~","s":"w","t":"j","u":"<","v":"z","w":"s","x":"l","y":":",
                            "z":"0"
                         }

#print(code_encrypt_dictionary)
#opening info security file, reads and stores its contents and closes the file
info_security_file = open("info_security.txt","r")
info_file_read = info_security_file.read()    
info_security_file.close()

#create/open a new file to store the encrypted text
info_file_encrpyt = open ("encrypted.txt","w")

#for loop to iterate through all the elements in the text write its encrypted value to encrypted.txt file.

for i in info_file_read:
    if i in code_encrypt_dictionary:
        info_file_encrpyt.write(code_encrypt_dictionary[i])
    elif  i == '.' or i == ',' or i == '!': 
         info_file_encrpyt.write(i)
    else:
        info_file_encrpyt.write(i)

#close the ecrypted file
info_file_encrpyt.close()




