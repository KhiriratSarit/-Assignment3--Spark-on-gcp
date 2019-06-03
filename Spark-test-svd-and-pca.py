import numpy as np 

from pyspark import SparkContext
from pyspark.mllib.linalg import Vectors
from pyspark.mllib.linalg.distributed import RowMatrix


# load the dataset 
rows = np.loadtxt('testmatrix.txt', dtype=float)
print('finish loading the data set rows with size')
print(rows.shape)
print('\n')

sc = SparkContext(appName="PythonSVDExample")

rows = sc.parallelize(rows)
mat = RowMatrix(rows)

# compute SVD 
svd = mat.computeSVD(5, computeU=True)
U = svd.U       # The U factor is a RowMatrix.
s = svd.s       # The singular values are stored in a local dense vector.
V = svd.V       # The V factor is a local dense matrix.
# $example off$
collected = U.rows.collect()
print("U factor is:")
for vector in collected:
    print(vector)

print("Singular values are: %s" % s)
print("V factor is:\n%s" % V)


# Compute the top 4 principal components.
# Principal components are stored in a local dense matrix.
pc = mat.computePrincipalComponents(4)
projected = mat.multiply(pc)

collected = projected.rows.collect()
print("\n\nProjected Row Matrix of principal component:")
for vector in collected:
    print(vector)

sc.stop()