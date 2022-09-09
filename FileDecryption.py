# dictionary with decrypted values for A-Z and a-z
code_decrypted_dictionary = { "2":"A","-":"B","%":"C","@":"D","3":"E","#":"F","8":"G","g":"H","p":"I", "y":"J",
                              "7":"K","`":"L","{":"M","f":"N","+":"O","1":"P","m":"Q","q":"R","^":"S",
                            "[":"T","6":"U",";":"V","*":"W","?":"X","u":"Y","(":"Z","o":"a","4":"b","]":"c",
                            "r":"d","&":"e","_":"f","9":"g","k":"h",")":"i","5":"j","e":"k","d":"l",">":"m",
                            "!":"n","}":"o","|":"p","c":"q","~":"r","w":"s","j":"t","<":"u","z":"v","s":"w",
                            "l":"x",":":"y","0":"z"
                            }

#opening info encrypted file, reads and stores its contents and closes the file
encrypted_file = open("encrypted.txt","r")
encrypted_file_read = encrypted_file.read()    
encrypted_file.close()


#create/open a new file to store the decrypted text
info_file_decrypt = open ("decrypted.txt","w")

#for loop to iterate through all the elements in the text write its decrypted value to decrypted.txt file.

for i in encrypted_file_read:
    if i in code_decrypted_dictionary:
        info_file_decrypt.write(code_decrypted_dictionary[i])
    else:
        info_file_decrypt.write(i)

#close the decrypted file
info_file_decrypt.close()
 #print the decrypted file in sceen
decrypted_file = open("decrypted.txt","r")
decrypted_text=decrypted_file.read()
print(decrypted_text)




    


