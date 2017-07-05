import matplotlib.pyplt as plt
import numpy as np
from sklearn.metrics import r2_score
np.random.seed(2)

pageSpeeds = np.random.normal(3.0,1.0,100)
purchaseAmount = np.random.normal(50.0, 30.0, 100)/ pageSpeeds

plt.scatter(pageSpeeds,purchaseAmount)

trainX = pageSpeeds[:80]
testX = pageSpeeds[80:]
trainY = purchaseAmount[:80]
testY = purchaseAmount[80:]

x = np.array(trainX)
y = np.array(trainY)
p4 = np.poly1d(np.polyfit(x,y,8))

r2 = r2_score(testY, p4(testX))