

def is_palindrome(num: str) -> bool:
    return num == num[::-1]

nums = "titit"

print(is_palindrome(nums))