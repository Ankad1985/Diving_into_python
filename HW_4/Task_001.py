# Напишите функцию для транспонирования матрицы

def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Создаем новую матрицу с транспонированными размерами
    trans = []
    for _ in range(cols):
        row = []
        for _ in range(rows):
            row.append(0)
        trans.append(row)

    # Копируем элементы из исходной матрицы в транспонированную
    for i in range(rows):
        for j in range(cols):
            trans[j][i] = matrix[i][j]

    return trans


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

trans_matrix = transpose_matrix(matrix)
print(trans_matrix)
