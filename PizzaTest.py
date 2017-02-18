import networkx
import math
import numpy



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
    def __init__(self, matrix, list):
        self.matrix = matrix
        self.min_ingredient = int(list[2])
        self.max_shape_size = int(list[3])
        self.long = int(list[1])
        self.width = int(list[0])
        L = len(matrix)
        l = len(matrix[0])
        self.matrix_tomato = [L * [0] for _ in range(l)] # numpy.zeros((L, l))
        self.generate_array_tomato()

    def generate_array_tomato(self):
        #L = len(matrix)
       # l = len(matrix[0])
       # self.matrix_tomato = numpy.zeros((L, l)) #  [L * [_] for _ in range(l)]

        nb_tomato = 0
        for i in range(0, self.long):
            for j in range(0, self.width):
                if matrix[j][i] == 'T':
                    nb_tomato += 1
                    self.matrix_tomato[i][j] = nb_tomato

        print("\nNb tomato :")
        print(self.matrix_tomato)



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

matrix = []
for line in f.readlines():
    matrix.append(line[:-1])


meta_list = matrix[0].split(' ')
del matrix[0]
print("\nPizzaaa :")
print(matrix)

print("\nMeta data :")
print(meta_list)

pizza = Pizza(matrix, meta_list)

min_long = math.floor(math.sqrt(float(meta_list[3])))

all_shape = []

min_size = int(meta_list[2])*2
max_size = int(meta_list[3])

for i in range(1, max_size+1):
    for j in range(1, max_size+1):
        current_shape = Shape(i, j)
        if current_shape.isValidShape(min_size, max_size):
            all_shape.append(current_shape)

print("\nShapes acceptables :")
for shape in all_shape:
    print(shape)


