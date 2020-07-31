"""
2.2:
Write a Python function which takes a character (i.e. a string of length 1) and returns True if it is
a vowel, False otherwise.
"""

def vowel_check(char):
 if(char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
  return True
 else:
  return False


char = input("Enter character: ");

# If Invalid input, exit
if (char.isalpha() == False):
 exit();

if (vowel_check(char)):
 print(char, "is a vowel.");
else:
 print(char, "is not a vowel."); 