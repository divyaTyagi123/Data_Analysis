# fetching dataset 
from sklearn.datasets import fetch_openml
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression

mnist = fetch_openml('mnist_784')
#print(mnist)

x , y = mnist['data'],mnist['target']
#print(x.shape , y.shape)

some_digit = x.iloc[3600]           # this returned an array of 784 elements(pixels) which shows an image 
some_digit_image = some_digit.to_numpy().reshape(28,28)     # reshaping it to 28x28 pixels means 2D image
plt.imshow(some_digit_image, cmap=matplotlib.cm.binary, interpolation='nearest')
plt.show()

x_train = x[:6000]
x_text = x[6000:7000]
y_train = y[:6000]
y_test = y[6000:7000]

shuffle_index = np.random.permutation(6000)       # shuffling the training data
x_train,y_train = x_train.iloc[shuffle_index], y_train.iloc[shuffle_index]

#creating a 8 detector to detect digit 8

y_train = y_train.astype(np.int8)
y_test = y_test.astype(np.int8)
y_train_8 = (y_train == 8)
y_test_8 = (y_test == 8)
clf = LogisticRegression(solver = 'lbfgs' ,max_iter=2000,tol=0.1)  # using logistic regression classifier
clf.fit(x_train, y_train_8)

output = clf.predict([x.iloc[3891]])        # works if model was trained on x 
print(output)
print()
# cross validation 
from sklearn.model_selection import cross_val_score

score = cross_val_score(clf , x_train, y_train_8, cv = 3, scoring = 'accuracy')
print(score)
print("Mean accuracy: ", score.mean())