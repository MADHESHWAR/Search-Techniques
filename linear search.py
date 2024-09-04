def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i 
    return -1

n = int(input("Enter the value of n: "))
arr = []
print("Enter the array elements: ")
for i in range(n):
    element = int(input())
    arr.append(element)
target = int(input("Enter the number you want to search for: "))
result = linear_search(arr, target)
if result != -1:
    print(f"Element found at index : {result}")
else:
    print("Element not found in the array !")
