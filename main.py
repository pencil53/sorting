#Optimized Python program for implementation of bubble sort

"""def bubblesort(arr):
    n = len(arr)

    #Traverse through all array elements
    for i in range(n):
        swapped = False
        
        #Last i elements are already in place
        for j in range(0, n-i-1):

            #traverse the array from 0 to n-i-1
            #swap if the element found is greater
            #than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] =  arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break



#Driver code to test above
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]

    bubblesort(arr)

    print("sorted array:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")



#python program for implementation of inseration sort

#function to do insertion sort
def insertionsort(arr):

    #traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        #move elements of arr[0..i-1], that are
        #greater than key, to one position ahead
        #of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key


# Driver code to test above
arr = [12, 11, 13, 5, 6]
insertionsort(arr)
for i in range(len(arr)):
    print ("% d" % arr[i])"""

"""def bubblesort(arr):
    n = len(arr)

    #Traverse through all array elements
    for i in range(n):
        swapped = False
        
        #Last i elements are already in place
        for j in range(0, n-i-1):

            #traverse the array from 0 to n-i-1
            #swap if the element found is greater
            #than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] =  arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break

arr2 = [98, 64, 83, 75, 89, 73, 100, 54, 53, 0]

#Driver code to test above
if __name__ == "__main__":
    arr = [98, 64, 83, 75, 89, 73, 100, 54, 53, 0]

    bubblesort(arr)

    print("sorted Grades:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")
    
    print("original grades:")
    print(arr2)"""




"""def insertionsort(arr):

    #traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        #move elements of arr[0..i-1], that are
        #greater than key, to one position ahead
        #of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key


# Driver code to test above
arr = [94, 93, 65, 67, 84, 65, 100, 73, 61]
arr2 = [94, 93, 65, 67, 84, 65, 100, 73, 61]
insertionsort(arr)
print("Sorted grades")
for i in range(len(arr)):
    print ("% d" % arr[i])

print("Original grades")
print(arr2)"""

mylist = [3,1,2,5,4]
mylist.sort(reverse = True)
print(mylist)
print(mylist.sort(reverse = False))

#bubble sort
#time complexity - O(n^2)

mylist = [12,34,2,5,7]

for i in range(0, len(mylist)):
    for j in range(i, len(mylist)):
        if mylist[i] < mylist[j]:
            mylist[i],mylist[j] = mylist[j], mylist[i]

print(mylist)