# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True

str1= "nonsense"
str2= "approved"
def find_anagrams(str1, str2):
    # [assignment] Add your code here
    if sorted(str1)==sorted(str2):
     return True
    else:
     return False
print(find_anagrams(str1, str2))

