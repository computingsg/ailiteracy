# Provide appropriate comments for this program
# Linear regression y = a*x + b using least squares

def mean(values):
    s = 0.0
    n = len(values)
    for i in range(n):
        s += values[i]
    return s / n

def variance(values, m):
    s = 0.0
    n = len(values)
    for i in range(n):
        d = values[i] - m
        s += d * d
    return s

def covariance(x, mx, y, my):
    s = 0.0
    n = len(x)
    for i in range(n):
        s += (x[i] - mx) * (y[i] - my)
    return s

def linear_regression_fit(x, y):
    mx = mean(x)
    my = mean(y)
    cov = covariance(x, mx, y, my)
    var = variance(x, mx)
    a = cov / var          # slope
    b = my - a * mx        # intercept
    return a, b

def linear_regression_predict(x, a, b):
    preds = []
    for i in range(len(x)):
        preds.append(a * x[i] + b)
    return preds

# main
X = [1, 2, 3, 4, 5]
Y = [2, 4, 5, 4, 5]
a, b = linear_regression_fit(X, Y)
print("Slope (a):", a)
print("Intercept (b):", b)
print("Predictions:", linear_regression_predict([1, 2, 3, 6], a, b))

# Suggested solution at https://github.com/computingsg/ailiteracy/blob/main/linear_regression_comments.py
