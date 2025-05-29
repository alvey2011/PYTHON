word = str(input("Enter a word : "))
n = ''
for w in word : 
    n = w + n 
    
if n == word :
    print("The word is a palindrome.")
else:
    print("the word is not a plaindrome")
    