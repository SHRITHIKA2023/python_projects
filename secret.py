import random
word=input("Enter a code word: \n")
for i in word:
  #first slicing of word is happening then first letter of the word is add to last of the word
  n=word[1:]+word[0]
  #adding random letters in the beginning and end of the word
  random_letters=random.choice("abcdefghijklmnopqrstuvwxyz")+n+random.choice("abcdefghijklmnopqrstuvwxyz")
  #printing the final word
  
print(random_letters[:8])
  

  
if len(word) < 3:
  print(word[::-1])

marks=[1,2,34,98,78]
for mark in marks:
  print(mark)

   