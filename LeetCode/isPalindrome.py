''' write a function to check if a number is a palindrome number
    e.g 57275 --> true
    e.g 259 --> false
'''

def isPalindrome(x):
    div=1
    # x=52725, div=10000
    while x/div>=10:
        div*=10
    while x!=0:
        # right=the rightmost digit, left=the leftmost digit
        right=x%10
        left=x/div
        if left!=right:
            return False
        # strips off the rightmost digit and the leftmost digit
        x=(x%div)/10
        div/=100
    return True
        
if __name__ == '__main__':
    print isPalindrome(52725)
