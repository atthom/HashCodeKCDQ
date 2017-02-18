import networkx
import math



class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Shape:
    def __init__(self, longeur, largeur):
        self.longeur = longeur
        self.largeur = largeur

    def isValidShape(self, min, max):
        if self.size() < min:
            return False
        if self.size() > max:
            return False
        return True

    def size(self):
        return self.longeur*self.largeur

    def __str__(self):
        return "{ longeur:" + str(self.longeur) + "," + " largeur: " + str(self.largeur) + "}"


class Pizza:
    def __init__(self, matrix, min, max):
        self.matrix = matrix
        self.min_ingredient = min
        self.max_shape_size = max

    def isValidSlice(self, shape, coordinate):
        nb_tomato = 0
        for i in range(coordinate.x, coordinate.x + shape.longeur):
            if matrix[i][coordinate.y] == 'T':
                nb_tomato += 1

        nb_mush = shape.size() - nb_tomato

        if nb_mush> self.min_ingredient and nb_tomato>self.min_ingredient:
            return True
        else:
            return False


f = open("input_files/small.in", "r")

#str = f.read()
matrix = []
for line in f.readlines():
    #print(line)
    matrix.append(line[:-1])
    #for char in line:
        #print(char)
        #matrix.append()


meta_list = matrix[0].split(' ')
del matrix[0]
print(matrix)
print(meta_list)

L = len(matrix)
l = len(matrix[0])
matrix_zero = [L * [_] for _ in range(l)]

print(matrix_zero)

pizza = Pizza(matrix, meta_list[2], meta_list[3])

min_long = math.floor(math.sqrt(float(meta_list[3])))

all_shape = []

min_size = int(meta_list[2])*2
max_size = int(meta_list[3])

for i in range(1, max_size+1):
    for j in range(1, max_size+1):
        current_shape = Shape(i, j)
        if current_shape.isValidShape(min_size, max_size):
            all_shape.append(current_shape)


for shape in all_shape:
    print(shape)
