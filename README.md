# Assignment3--Spark-on-gcp
This repository is to test the computations of SVD and PCA on the matrix evaluated by pyspark on google cloud.

## Requirements 

We test the SVD and PCA computations by the script `Spark-test-svd-and-pac.py` on the Windows laptop with the following requirements: 

* Spark 2.3.3 with Hadoop 2.7 
* Anaconda 3 with installed packages `numpy` and `pyspark` 

## Run the code in the personal Windows machine 

Download Spark 2.3.3 with Hadoop 2.7, and run the following command: 

`directory/to/spark-2.3.3-bin-hadoop2.7/bin/spark-submit Spark-test-svd-and-pca.py`

## Numerical Results for GCP

one master - 2 VCPUs
two workers - each of them has 2 VCPUs 

SVD and PCA 

* 2000: 2 min 22 sec for one master and 1 min 45 sec for one master, two workers 
* 2100: 8 min 32 sec for one master and 1 min 54 sec for one master, two workers 
* 2200: out of memory for one master and 2 min for one master, two workers