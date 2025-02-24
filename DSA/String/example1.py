# Python Program to Check if a String is Palindrome or Not

def palindrome(input):
    n= len(input)
    for i in range(0, int(n/2)):
        if (input[i]==input[n-i-1]):
            return True
        else:
            return False

if __name__ == '__main__':
    input= "malayalam"
    s=(palindrome(input))
    if (s):
        print("Yes")
    else:
        print("No")