# ------------------------------------------------------------
# SIMPLE LINEAR REGRESSION (y = a*x + b)
# From first principles without external libraries
# ------------------------------------------------------------

# Function to compute the mean (average) of a list of numbers
def mean(values):
    s = 0.0
    n = len(values)
    for i in range(n):          # sum all values manually
        s += values[i]
    return s / n                # divide total by number of items


# Function to compute variance: Σ(x - mean_x)^2
def variance(values, m):
    s = 0.0
    n = len(values)
    for i in range(n):
        d = values[i] - m       # deviation from mean
        s += d * d              # square and add up
    return s                    # return total variance sum (not divided by n)


# Function to compute covariance between x and y:
# Σ[(x - mean_x)*(y - mean_y)]
def covariance(x, mx, y, my):
    s = 0.0
    n = len(x)
    for i in range(n):
        s += (x[i] - mx) * (y[i] - my)
    return s


# Function to calculate slope (a) and intercept (b) using least squares formula:
# a = covariance(x,y) / variance(x)
# b = mean(y) - a * mean(x)
def linear_regression_fit(x, y):
    mx = mean(x)                # mean of x values
    my = mean(y)                # mean of y values
    cov = covariance(x, mx, y, my)  # calculate covariance between x and y
    var = variance(x, mx)           # calculate variance of x
    a = cov / var               # slope
    b = my - a * mx             # intercept
    return a, b


# Function to make predictions using the model y = a*x + b
def linear_regression_predict(x, a, b):
    preds = []
    for i in range(len(x)):
        y_pred = a * x[i] + b   # apply the regression equation
        preds.append(y_pred)
    return preds


# main
# Sample dataset (x: independent variable, y: dependent variable)
X = [1, 2, 3, 4, 5]
Y = [2, 4, 5, 4, 5]

# Fit the regression model
a, b = linear_regression_fit(X, Y)

# Display computed coefficients
print("Slope (a):", a)
print("Intercept (b):", b)

# Make predictions for given x values
predictions = linear_regression_predict([1, 2, 3, 6], a, b)

# Show predicted y values
print("Predictions:", predictions)
