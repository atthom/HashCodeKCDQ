import networkx

f = open("input_files/small.in", "r")

#str = f.read()
matrix = []
for line in f.readlines():
    #print(line)
    matrix.append(line[:-1])
    #for char in line:
        #print(char)
        #matrix.append()


meta = matrix[0]
del matrix[0]

print(matrix)

meta_list = meta.split(' ')

print(meta_list)

L = len(matrix)
l = len(matrix[0])
matrix_zero = [L * [0] for _ in range(l)]

print(matrix_zero)

#for line in matrix:
#    for char in line:
#        if char == 'T':
#            before =



