# Assignment3--Spark-on-gcp
This repository is to test the computations of SVD and PCA on the matrix evaluated by pyspark on google cloud.

## Requirements

This section introduces the requirements so that pyspark can be run on your personal local machine as shown below: 

* Java JDK
* Scala
* Spark 2.3.3 with Hadoop 2.7 
* Anaconda 3 with installed packages `numpy` and `pyspark` 

In addition, you have to export SPARK_HOME (for your current spark directory), PYSPARK_PYTHON (for your current python directory), and HADOOP_HOME (for your current hadoop directory). 

## Run the code in the personal Windows machine 

After all the installations, we can run the SVD and PCA computations by the python scipt `Spark-test-svd-and-pca.py` on your personal machine with spark 2.3.3 and hadoop 2.7 by using the following command:

`directory/to/spark-2.3.3-bin-hadoop2.7/bin/spark-submit Spark-test-svd-and-pca.py`


## Run the code on GCP

This section introduces how to test the SVD and PCA computations by the script `Spark-test-svd-and-pca.py` on GCP. 

## Numerical Results for GCP

one master - 2 VCPUs
two workers - each of them has 2 VCPUs 

SVD and PCA 

* 2000: 2 min 22 sec for one master and 1 min 45 sec for one master, two workers 
* 2100: 8 min 32 sec for one master and 1 min 54 sec for one master, two workers 
* 2200: out of memory for one master and 2 min for one master, two workers