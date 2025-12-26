x = "madam"
l = 0
r = len(x) - 1
is_palindrome = True

while l < r:
    if x[l] != x[r]:
        is_palindrome = False
        break
    l += 1
    r -= 1

if is_palindrome:
    print("palindrome")
else:
    print("not a palindrome")
