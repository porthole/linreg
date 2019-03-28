
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

model = LinearRegression(fit_intercept=False)
model.fit(Xtrain, ytrain)
y_model = model.predict(Xtest)

#Note: if error: you may need np.asarray(...,dtype=np.float64)

#3. Test it on test data
#for classificaiton
# from sklearn.metrics import accuracy_score
# accuracy_score(ytest, y_model)
#for regression
mse = mean_squared_error(ytest, y_model)
print("Slope: ", w)
print("MSE: ", mse)

#compare labels
plt.scatter(ytest, y_model)
plt.xlabel("Truth")
plt.ylabel("Predicted")
plt.title("Boston Housing True vs Predicted prices")