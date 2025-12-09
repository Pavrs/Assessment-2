A=[1,2,3,4,5,6,7,8,9]
n=len(A)
print(A)
target=int(input('What is your target'))


def binary(A, target):                  #done
    low=0
    high=n-1
    while low<=high:
        mid=((low+high)//2)
        if A[mid]==target:
            return mid
        elif A[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1

result=binary(A, target)
if result != -1:
    print('your target was found at index', result)
else:
    print('target not found')


def linear(A, target):                  #done
    for i in range(0,n-1):
        if target == A[i]:
            print('Target found at index', i)
            break
        else:
            print('target not found')

linear(A, target)

def insertion(A):                       #???? does not order only shifts 2 to the left making negatives
    for i in range(0,n-1):
        key=i+1
        for j in range(0,n-1-i):
            if j>=A[j+1] and j+1<key:
                A[j]=A[j+1]
                j-=1
            A[j+1]=key
    return A

l=insertion(A)
print(l)

def bubble(A):                          #???? too many j j+1 and A
    for i in range(0,n-1):
        swapped = True
        for j in range(0,n-1-i):
            if A[i]<A[j+1]:
                temp = A[j]
                A[j],A[j+1]=A[j+1], temp
            return A
s=bubble(A)
print(s)











