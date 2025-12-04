def find_number(arr, target):
        for i in range(len(arr)):
            if arr[i] == target:
                return i


print(find_number([1,2,5,4,67,7,65,32], 32))