import string   # to use the inbuilt string.punctuation method

#open sometext.txt in read mode
myfile = open("sometext.txt","r")

#store the contents of file in a var called text
text = myfile.read()
myfile.close()

#  remove the punctuactions from the text
for punctuactions in string.punctuation:
    text= text.replace(punctuactions,'')
#print(text)

#initialize an empty dictionary to store  contents of  text file in key value pair format
#initialize a variable count to 0 to store  count of  word's occurrances
word_dict ={}
count=0

#split the words in text using split() method.
indv_keys=text.split()

#using for loop to iterate through each words
for word  in indv_keys:

    #using if loop to add each word to dictionary as well as to track  number of occurances of each word through count variable.

    if word not in word_dict:
        word_dict[word]= count+1
    else:
        word_dict[word]+=1
print("Dictionary is /n" )
#print (word_dict)
# print(word_dict["Co"])
# print(type(word_dict))

#Co.
#twenty-six
#printing dictionary in readable format
for key,value in word_dict.items():
    print(key,":",value)



