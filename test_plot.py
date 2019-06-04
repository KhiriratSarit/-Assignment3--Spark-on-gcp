import numpy as np
import matplotlib.pyplot as plt


N = 2 
menMeans = (105, 114)
womenMeans = (142, 512)
menStd = (0.1, 0.1)
womenStd = (0.1,0.1)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, menMeans, width, yerr=menStd)
p2 = plt.bar(ind, womenMeans, width,
             bottom=menMeans, yerr=womenStd)

plt.ylabel('Computation time [sec]')
plt.xlabel('matrix size')
plt.title('SVD and PCA computation time for each cluster on GCP')
plt.xticks(ind, ('2000', '2100'))
plt.yticks(np.arange(0, 800, 100))
plt.legend((p1[0], p2[0]), ('one master two workers', 'one master'))

plt.show()