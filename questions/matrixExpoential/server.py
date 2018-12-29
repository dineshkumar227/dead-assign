import scipy.linalg as sla
import numpy as np

nMax = 2
matrixRows = matrixCols = 3

matrix = np.random.random_integers(-nMax,nMax,(matrixRows,matrixCols))
print (sla.expm(matrix))



