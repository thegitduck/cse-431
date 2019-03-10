import statistics as stat

# Code from https://www.geeksforgeeks.org/merge-sort/
# Python program for implementation of MergeSort 
def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
    return arr


def middle(L):
    n = len(L)
    m = n - 1
    return (L[int(n/2)] + L[int(m/2)]) / 2.0

def do_median(arr):
    if arr:
        med = round(middle(arr), 1)
        if med == 0:
            print(int(med))
        elif (med < 1) and (med > 0):
            print(med)
        elif int(med) == med:
            print(int(med))
        else:
            print(med)
    else:
        print("Wrong!")

num = int(input())
arr = []
for i in range(num):
    instr = input().split()
    let = instr[0]
    val = int(instr[1])
    
    if let == 'a':
        arr.append(val)
        arr = mergeSort(arr)
        do_median(arr)
    else:
        if val in arr:
            arr.remove(val)
            arr = mergeSort(arr)
            do_median(arr)
        else:
            print("Wrong!")