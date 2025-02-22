def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]


word = input("Enter a word: ")
if is_palindrome(word):
    print("It's a palindrome!")
else:
    print("Not a palindrome.")
