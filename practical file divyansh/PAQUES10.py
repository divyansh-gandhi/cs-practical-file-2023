#ques 01
str1= (input('type the string ;'))
vowel_count=consonants_count=0
vowel={'aeiouAEIOU'}
for alphabet in str1:
  if alphabet in vowel:
    vowel_count=vowel_count +1
  elif alphabet == chr(32):
    consonants_count=consonants_count
  else:
    consonants_count=consonants_count+1
  
print("Number of Vowels in ",str1," is :",vowel_count)
print("Number of Consonants in ",str1," is :",consonants_count)

uppercase_count=0
lowercase_count=0
for elem in str1:
  if elem.isupper():
    uppercase_count += 1
  elif elem.islower():
    lowercase_count += 1
print("Number of UPPER Case in ",str1,"' is :",uppercase_count)
print("Number of lower case in ",str1,"' is :",lowercase_count)
 

 

