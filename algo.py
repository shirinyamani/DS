#Bubble Sort  #O(n2)
from torch import R


def BubbleSort(arr):
    for _ in range(len(arr)):
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1] = arr[i+1], arr[i]
    return arr

#Merge Sort #O(logn)
def _merge(arr1, arr2):
    res= []
    for i in range(len(arr1)+len(arr2)):
        #print(i,arr1,arr2)
        if arr1[0] <= arr2[0]:
            res.append(arr1[0])
            del arr1[0]
        else:
            res.append(arr2[0])
            del arr2[0]
        if len(arr1)==0:
            res.extend(arr2)
            break
        elif len(arr2)==0:
            res.extend(arr1)
            break

    return res


def MergeSort(arr):
    if len(arr) ==1:
        return arr
    else:
        arr1 = MergeSort(arr[:len(arr)//2])
        arr2 = MergeSort(arr[len(arr)//2:])
        return _merge(arr1, arr2)

#Insertion Sort O(N2)
def swap(arr,i,j):
    t =arr[i]
    arr[i]=arr[j]
    arr[j]=t
    return arr

def InsertionSort(arr):
    for indx in range(1,len(arr)):
        for i in range(indx, 0, -1):
            if arr[i] < arr[i-1]:
                swap(arr,i,i-1)
            else: break

    return arr


def binarysearch(arr,elm):
    if len(arr)==0:
        return None
    elif len(arr)==1:
        return 0 if arr[0] == elm else None
    mid = len(arr)//2
    left= arr[:mid]
    right=arr[mid:]
    if elm == left[-1]:
        return mid - 1
    elif elm > left[-1]:
        return binarysearch(right,elm)
    else:
        return binarysearch(left,elm)




































if __name__ == "__main__":
    #print(_merge([3,5,67],[6,9,20]))
    #print(MergeSort([39,12,18,85,72]))
    print(binarysearch(list(sorted([30,4,6,1,20,88])),30))
