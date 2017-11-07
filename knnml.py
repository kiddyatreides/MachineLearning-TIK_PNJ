from __future__ import division #import library pembagian
import numpy as np
from sklearn import datasets



iris = datasets.load_iris()

count_data = len(iris.data)
persentase = (10/100) * count_data
x = round(persentase,0)

#iris_data = iris.data[:int(x)]
iris_data = iris.data
print iris_data
print ""
print "Menampilkan Iris Data ke 1,2,3"
iris_labels = iris.target
print(iris_data[0], iris_data[1], iris_data[3])
print ""
print "Menampilkan Iris Label pertama, ke 80, dan ke 100"
print(iris_labels[0], iris_labels[79], iris_labels[100])
print""
np.random.seed(10)
indices = np.random.permutation(len(iris_data))
n_training_samples = 12
learnset_data = iris_data[indices[:-n_training_samples]]
learnset_labels = iris_labels[indices[:-n_training_samples]]
testset_data = iris_data[indices[-n_training_samples:]]
testset_labels = iris_labels[indices[-n_training_samples:]]
print "Menampilkan Learnset Data Hingga data ke 10 dan learsnet labels ke 10"
print(learnset_data[:10], learnset_labels[:10])
print ""
print "Menampilkan Test Set Data hingga data ke 10 dan test set labels hingga data ke 10"
print(testset_data[:10], testset_labels[:12])
print ""
# following line is only necessary, if you use ipython notebook!!!
#%matplotlib inline 

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
colours = ("r", "b")
X = []
for iclass in range(3):
	X.append([[], [], []])
	for i in range(len(learnset_data)):
		if learnset_labels[i] == iclass:
			X[iclass][0].append(learnset_data[i][0])
			X[iclass][1].append(learnset_data[i][1])
			X[iclass][2].append(sum(learnset_data[i][2:]))
colours = ("r", "g", "y")
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for iclass in range(3):
	ax.scatter(X[iclass][0], X[iclass][1], X[iclass][2], c=colours[iclass])
#plt.show()
print ""
print "======================"
print ""
def distance(instance1, instance2):
    # just in case, if the instances are lists or tuples:
    instance1 = np.array(instance1) 
    instance2 = np.array(instance2)
    
    return np.linalg.norm(instance1 - instance2)
print "Menampilkan Jarak data ke dari satu titik ke titik lain"
print(distance([3, 5], [1, 1]))
print ""
print "Menampilkan Jarak Dari Learnset data ke 3 ke learnset data ke 10"
print(distance(learnset_data[3], learnset_data[10]))

print "--------------------------------"
print ""
def get_neighbors(training_set, labels, test_instance, k, distance=distance):
	distances = []
	for index in range(len(training_set)):
		dist = distance(test_instance, training_set[index])
		distances.append((training_set[index], dist, labels[index]))
	distances.sort(key=lambda x: x[1])
	neighbors = distances[:k]
	return neighbors

print "Menampilkan Tetangga"

for i in range(3):
	neighbors = get_neighbors(learnset_data, learnset_labels, testset_data[i], 3, distance=distance)
	print(i, testset_data[i], testset_labels[i], neighbors)

plt.show()