def sum(arr,n):
    sum=0
    for i in range(0,n):
        sum+=arr[i]
    return sum
# Driver Code
if __name__== '__main__':
    arr = [1,2,3,4,5]
    n= len(arr)
    print("The sum of the Array is " , sum(arr,n))
