# Reverse Words in a Given String in Python

def reverse(input):
    a= input.split()
    b= a[::-1]
    c=""
    for i in range (0, len(b)):
        c += b[i] + " "  
    return c

if __name__ == '__main__':
    input= "My name is Subhanshu"
    print(reverse(input))