pizza = []

with open("./input_files/small.in") as f:
    height, width, L, H = map(int, f.readline().split())
    for line in f.readlines():
        pizza.append([1 if c == 'T' else 0 for c in line.replace('\n', '')])

print(height, width, L, H)
print(pizza)
assert (len(pizza) == height)
assert (len(pizza[0]) == width)


# Precompute the matrix mat such as mat[i][j] is the number of tomatoes
# in the rectangle from top-left corner to cell (i,j) included
def compute_matrix_numbers_tomatoes_top_left(pizza):
    height = len(pizza)
    width = len(pizza[0])
    mat = [width * [0] for _ in range(height)]
    nb_tomatoes = 0
    for i in range(height):
        for j in range(width):
            nb_tomatoes += pizza[i][j]
            if i == 0 and j == 0:
                mat[i][j] = pizza[i][j]
            elif i == 0:
                mat[i][j] = mat[i][j - 1] + pizza[i][j]
            elif j == 0:
                mat[i][j] = mat[i - 1][j] + pizza[i][j]
            else:
                mat[i][j] = mat[i - 1][j] + mat[i][j - 1] - mat[i - 1][j - 1] + pizza[i][j]
    assert (mat[-1][-1] == nb_tomatoes)
    return mat


# compute the number of tomatoes in slice [(i1,j1),(i2,j2)] using the precomputed matrix mat
def compute_number_tomatoes_in_slice(mat, i1, j1, i2, j2):
    assert (i1 <= i2)
    assert (j1 <= j2)
    nb_tom = mat[i2][j2]
    if i1 > 0:
        nb_tom -= mat[i1 - 1][j2]  # x
    if j1 > 0:
        nb_tom -= mat[i2][j1 - 1]  # y
    if i1 > 0 and j1 > 0:
        nb_tom += mat[i1 - 1][j1 - 1]  # w
    return nb_tom


# return 0 if slice is invalid else return the area of the slice
def compute_slice_value(mat, i1, j1, i2, j2, L, H):
    assert (i1 <= i2)
    assert (j1 <= j2)
    height = i2 - i1 + 1
    width = j2 - j1 + 1
    area = height * width
    nb_tomatoes = compute_number_tomatoes_in_slice(mat, i1, j1, i2, j2)
    nb_mushrooms = area - nb_tomatoes
    if nb_tomatoes >= L and nb_mushrooms >= L and area <= H:
        return area
    return 0

mat_numb_top_left = compute_matrix_numbers_tomatoes_top_left(pizza)
print(mat_numb_top_left)
print(compute_slice_value(mat_numb_top_left, 0, 0, len(pizza) - 1, len(pizza[0]) - 1, 1, 100))
