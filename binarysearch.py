def binary_search(arr, x):
	low = 0
	high = len(arr) - 1
	mid = 0
	while low <= high:
		mid = (high + low) // 2
		if arr[mid] < x:
			low = mid + 1
		elif arr[mid] > x:
			high = mid - 1
		else:
			return mid
	return -1
n = int(input("Enter the value of n: "))
arr = []
print("Enter the array elements: ")
for i in range(n):
    element = int(input())
    arr.append(element)
x=int(input("Enter the search element : "))
arr.sort()
result = binary_search(arr, x)
if result != -1:
	print("Element is present at index -->", result)
else:
	print("Element is not present in array !!")
