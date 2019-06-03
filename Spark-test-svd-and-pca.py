import numpy as np 

from pyspark import SparkContext
from pyspark.mllib.linalg import Vectors
from pyspark.mllib.linalg.distributed import RowMatrix


# run by using the command to see the result:: 
# D:/spark/spark-2.3.3-bin-hadoop2.7/bin/spark-submit Spark-test-svd-and-pca.py

# load the dataset 
rows = np.loadtxt('testmatrix.txt', dtype=float)
print('finish loading the data set rows with size')
print(rows.shape)
print('\n')

sc = SparkContext(appName="PythonSVDExample")
rows = sc.parallelize(rows)

#rows = sc.parallelize([Vectors.sparse(5, {1: 1.0, 3: 7.0}), Vectors.dense(2.0, 0.0, 3.0, 4.0, 5.0), Vectors.dense(4.0, 0.0, 0.0, 6.0, 7.0)])

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