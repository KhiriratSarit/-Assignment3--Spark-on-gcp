# prepare the data set 
import numpy as np 

rows = 500 
cols = 1000
A = np.random.randn(rows,cols)
output_matrix = np.dot(np.transpose(A),A) 


np.savetxt('testmatrix.txt', output_matrix, fmt='%d')