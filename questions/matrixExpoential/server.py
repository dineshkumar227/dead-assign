import scipy.linalg as sla
import numpy as np

#range of allowed values, dont want this to be too big to avoid cubersome problems
nMax = 2
#dimensions of matrix
matrixRows = matrixCols = 3

#generating a random matrix
matrix = np.random.random_integers(-nMax,nMax,(matrixRows,matrixCols))

answer = sla.expm(matrix)

print(answer)



