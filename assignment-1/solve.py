import random

arr = []
with open("inupt_quick_sort.txt", "r") as f:
    for line in f:
        arr.append(int(line.strip()))

def quickSort(A, left, right):
    if left < right:
        pivotIdx = random.randint(left, right)
        pivotValue = A[pivotIdx]
        A[left], A[pivotIdx] = pivotValue, A[left]
        lidx, ridx = left+1, right

        while lidx <= ridx:
            while lidx <= ridx and A[lidx] <= pivotValue:
                lidx += 1
            while lidx <= ridx and A[ridx] >= pivotValue:
                ridx -= 1
            if lidx < ridx:
                A[lidx], A[ridx] = A[ridx], A[lidx]
        A[left], A[ridx] = A[ridx], A[left]
        
        quickSort(A, left, ridx-1)
        quickSort(A, ridx+1, right)

quickSort(arr, 0, len(arr)-1)
