# Python program to print even length words in a string

input= "This is a python language aaaa"

a= input.split()

for i in range(0,len(a)):
    if (len(a[i]) %  2 == 0):
        print(a[i])

