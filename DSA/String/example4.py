# Check if String Contains Substring in Python

# def sub(a,b):
#     c= a.split()
#     for i in range(len(c)):
#         if (c[i]==b):
#             return True
#         else:
#             return False 



if __name__ == '__main__':
    substring= "gee"
    string= "geeks for geeks"
    if substring in string:
        print("Yes")
    else:
        print("No")