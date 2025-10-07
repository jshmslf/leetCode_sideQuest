# class Solution:
#     def is_palindrome(num: str) -> bool:
#         return print(num == num[::-1])


# Solution.is_palindrome('EllE')

def willReversed(string: str):
    return string[::-1].lower() # reversed and lowered

print("Every word will be reversed!")
while(True):
    user_input = input(">>: ")
    if user_input == '/quit':
        break
    
    print(willReversed(user_input))
        
    
