
X = xl
y = yl

xm = np.mean(X)
ym = np.mean(y)

w = np.sum((X - xm)*(y-ym))/np.sum((X-xm)**2)
b = ym - w*xm

print("Slope: ",w,b)

from matplotlib.colors import ListedColormap

plt.figure(figsize=(20,10))
# Plot also the training points
plt.scatter(X, y, edgecolor='k', s=80)

Xt = np.arange(np.min(X), np.max(X), 1)
yt = (w * Xt) + b
plt.plot(Xt, yt, c='r')

plt.xlabel("xl")
plt.ylabel("yl")
plt.title("Data and linear fit")