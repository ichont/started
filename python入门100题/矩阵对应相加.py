

x = [[1, 2, 3],
     [3, 2, 3],
     [1, 6, 3]]

y = [[9, 2, 3],
     [3, 8, 3],
     [9, 6, 6]]

z = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

for i in range(3):
    for j in range(3):
        z[i][j] = x[i][j] + y[i][j]

for i in z:
    print(i)