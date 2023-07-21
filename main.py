print("Welcome to the Encoder. Please enter a password to be used")
password=input()
print("Thank you!")

dictionary={'a':'abc', 'b':'bcd', 'c':'cde', 'd':'def', 'e':'efg', 'f':'fgh', 'g':'ghi', 'h':'hij', 'i':'ijk', 'j':'jkl', 'k':'klm', 'l':'lmn', 'm':'mno', 'n': 'nop', 'o':'opq', 'p':'pqr', 'q':'qrs', 'r':'rst', 's':'stu', 't':'tuv', 'u':'uvw', 'v':'vwx', 'w':'wxy', 'x': 'xyz', 'y': 'yza', 'z':'zab'}

while True:
  print("would you like to encode or decode a word? e/d")
  answer=input()
  #ENCODING
  if answer=='e':
      print("please enter a word!")
    
      word=input()
      encoded_word=""
    
      for i in range (len(word)):
        if dictionary.get(word[i])!=None:
          encoded_word+=dictionary[word[i]]
        
        else:
          print("Your word contains an invalid character. Please enter a new word")
          break
      print("Encoded: "+encoded_word)

  #DECODING
  if answer=='d':
    print("Please enter your password")
    try_password=input()

    
    if try_password!=password:
      print("incorrect password")


    
    if try_password==password:
      print("Please enter the word you want to decode")
      word=input()
      deencoded_word=""
      if len(word)<3:
        print("your word is too short")

      for i in range(0,len(word)-2, 3):
        if word[i:i+3] not in dictionary.values():
          print("invalid word/character")
          break
        if word[i:i+3] in dictionary.values():
          for key in dictionary.keys():
            if dictionary[key]==word[i:i+3]:
              deencoded_word+=key
      print("your deencoded word is: "+deencoded_word)

  print("Would you like to translate another word? y/n")
  answer=input()

  if answer=="n":
    print("Thank you for using the Encoder!")
    break

#additional: loop that allows you to retry password 3 times