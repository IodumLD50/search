# linear search
# Линейный поиск

import random

n = 40
arr = []  # список из рандомных чисел
for i in range(n):
    number = random.randint(1, 100)
    arr.append(number)
    
to_search = random.randint(1, 100)  #  рандомное число которое мы будем искать
answer = -1 # изночально ответ - 1

##############################################################    



for i in range(n):
    if arr[i] == to_search:
        answer = i
        break
    



##############################################################

print(arr)
print(to_search)
print('_____________________')

if answer != -1:
    print(f'Элемнт в списке был, его индекс: {answer}')
else:
    print('Элемента в списке не было')    