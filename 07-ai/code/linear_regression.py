class LinearRegression:
    def __init__(self):
        self.a = 0.0
        self.b = 0.0

    def fit(self, x, y):
        if len(x) != len(y) or not x:
            raise ValueError("x and y must have the same non-zero length")

        mean_x = sum(x) / len(x)
        mean_y = sum(y) / len(y)
        variance_x = sum((value - mean_x) ** 2 for value in x) / len(x)
        if variance_x == 0:
            raise ValueError("all x values are equal")

        covariance = sum(
            (xi - mean_x) * (yi - mean_y)
            for xi, yi in zip(x, y)
        ) / len(x)
        self.a = covariance / variance_x
        self.b = mean_y - self.a * mean_x
        return self

    def predict(self, x):
        return [self.a * value + self.b for value in x]

    def mse(self, x, y):
        predictions = self.predict(x)
        return sum(
            (yi - prediction) ** 2
            for yi, prediction in zip(y, predictions)
        ) / len(y)


if __name__ == "__main__":
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 4, 6]
    model = LinearRegression().fit(x, y)
    print(f"f(x) = {model.a:.2f}x + {model.b:.2f}")
    print(f"MSE = {model.mse(x, y):.2f}")
