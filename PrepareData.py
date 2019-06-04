# prepare the data set 
import numpy as np 

rows = 1000
cols = 2500
A = np.random.randn(rows,cols)
output_matrix = np.dot(np.transpose(A),A) 


np.savetxt('testmatrix2500.txt', output_matrix, fmt='%d')