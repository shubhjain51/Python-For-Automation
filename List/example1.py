# Python program to interchange first and last elements in a list

def interchange(arr):
    temp= arr[0]
    n=len(arr)
    arr[0]= arr[n-1]
    arr[n-1]=temp
    return arr

if __name__ == '__main__' :
    arr= [1,2,3,4,5]
    print("The number after interchanges",  interchange(arr))
