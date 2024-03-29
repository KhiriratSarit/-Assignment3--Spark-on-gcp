import numpy as np 

#import findspark
#findspark.init()

from pyspark import SparkContext
from pyspark.mllib.linalg import Vectors
from pyspark.mllib.linalg.distributed import RowMatrix


# run by using the command to see the result:: 
# D:/spark/spark-2.3.3-bin-hadoop2.7/bin/spark-submit Spark-test-svd-and-pca.py --master local[*]

# load the dataset 
rows = np.loadtxt('testmatrix2200.txt', dtype=float)
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



# Compute the top 4 principal components.
# Principal components are stored in a local dense matrix.
pc = mat.computePrincipalComponents(4)
projected = mat.multiply(pc)


collected = U.rows.collect()
print("\n\n\n\n\nFinish computing U factor:")
#for vector in collected:
#    print(vector)

print("Singular values are: %s" % s)
print("Finish computing V factor\n\n\n\n\n")



collected2 = projected.rows.collect()
print("\n\n\n\n\nFinish Projected Row Matrix of principal component:")
for vector in collected2:
    print(vector)

sc.stop()