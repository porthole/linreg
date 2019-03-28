
X= Xtrain
y = ytrain
#train
w = np.dot(np.linalg.pinv(X),y)
print("Slope: ", w)

#predict
y_model = Xtest @ w
print(y_model.shape, Xtest.shape, w.shape)
mse = mean_squared_error(ytest, y_model)
print("*** MSE: ", mse)

#compare labels
plt.scatter(ytest, y_model)
plt.xlabel("Truth")
plt.ylabel("Predicted")
plt.title("Boston Housing True vs Predicted prices")