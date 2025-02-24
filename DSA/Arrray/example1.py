def largest (arr,n):
    max = arr[0]
    for i in range(1,n):
        if arr[i] > max :
            max= arr[i]
    return max


# Driver code
if __name__ == '__main__':
    arr = [10, 324, 45, 90, 9808]
    n = len(arr)
    print ("Largest in given array ", largest(arr, n))