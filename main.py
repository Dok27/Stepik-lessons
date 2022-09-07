num = 0
arr2 = []
N = 0
r, c = [int(i) for i in input().split()]
arr = [[0]*c for _ in range(r)]
# rep = int(r / 2)
# x = r - rep
# y = c - rep

#Создает массив чисел строка*столбец
#и разворачивает его
for i in range(r):
    for j in range(c):
        num += 1
        arr2.append(num)
arr2.reverse()

# for i in range(r):
#     for j in range(c):
#         arr[i][j] = f'{i}{j}'
#
# for i in range(r):
#     for j in range(c):
#         print(str(arr[i][j]).ljust(3), end=' ')
#     print()
# print()


#Отрисовывает матрицу

#Для четных и равных сторон
# if (r == c) and (r % 2 == 0):
#     while arr2:
#         for _ in range(rep):
#             for i in range(6):
#                 if i == 1:
#                     y -= 1
#                     arr[x][y] = arr2.pop(0)
#                 if i == 2:
#                     for _ in range(N):
#                         x += 1
#                         arr[x][y] = arr2.pop(0)
#                 if i == 3:
#                     for _ in range(N + 1):
#                         y += 1
#                         arr[x][y] = arr2.pop(0)
#                 if i == 4:
#                     for _ in range(N + 1):
#                         x -= 1
#                         arr[x][y] = arr2.pop(0)
#                 if i == 5:
#                     for _ in range(N + 1):
#                         y -= 1
#                         arr[x][y] = arr2.pop(0)
#             N += 2


#Для нечетных и равных сторон
# if (r == c) and (r % 2 == 1):
#     N += 1
#     x -= 1
#     y -= 1
#     while arr2:
#         arr[x][y] = arr2.pop(0)
#         for _ in range(rep):
#             for i in range(6):
#                 if i == 1:
#                     y -= 1
#                     arr[x][y] = arr2.pop(0)
#                 if i == 2:
#                     for _ in range(N):
#                         x += 1
#                         arr[x][y] = arr2.pop(0)
#                 if i == 3:
#                     for _ in range(N + 1):
#                         y += 1
#                         arr[x][y] = arr2.pop(0)
#                 if i == 4:
#                     for _ in range(N + 1):
#                         x -= 1
#                         arr[x][y] = arr2.pop(0)
#                 if i == 5:
#                     for _ in range(N + 1):
#                         y -= 1
#                         arr[x][y] = arr2.pop(0)
#             N += 2

#Заполняет матрицу по спирали
for j in range(len(arr2)):
    s = 1 + j * 2
    for i in range(c - s):
        if len(arr2) > 0:
            arr[j][i + j] = arr2.pop(-1)
    for i in range(r - s):
        if len(arr2) > 0:
            arr[i + j][c - 1 - j] = arr2.pop(-1)
    for i in range(c - s):
        if len(arr2) > 0:
            arr[r - 1 - j][c - 1 - i - j] = arr2.pop(-1)
    for i in range(r - s):
        if len(arr2) > 0:
            arr[r - 1 - i - j][j] = arr2.pop(-1)
if (r == c) and (r % 2 == 1):
    arr[int(r / 2)][int(c / 2)] = arr2.pop(0)

#Вывод
for i in range(r):
    for j in range(c):
        print(str(arr[i][j]).ljust(3), end=' ')
    print()


