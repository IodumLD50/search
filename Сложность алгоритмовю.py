# поиск максимального элемента в списке

arr = []
n = len(arr)
max_elem = arr[0]

for i in range(n):
    if arr[i] > max_elem:
        max_elem = arr[i]
        
        