from math import exp


def sigmoid(z):
    if z >= 0:
        return 1.0 / (1.0 + exp(-z))
    value = exp(z)
    return value / (1.0 + value)


class LogisticRegression:
    def __init__(self, learning_rate=0.1, iterations=2000):
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.a = 0.0
        self.b = 0.0

    def fit(self, x, y):
        if len(x) != len(y) or not x:
            raise ValueError("x and y must have the same non-zero length")

        n = len(x)
        for _ in range(self.iterations):
            probabilities = [
                sigmoid(self.a * xi + self.b)
                for xi in x
            ]
            gradient_a = sum(
                (probability - yi) * xi
                for xi, yi, probability in zip(x, y, probabilities)
            ) / n
            gradient_b = sum(
                probability - yi
                for yi, probability in zip(y, probabilities)
            ) / n
            self.a -= self.learning_rate * gradient_a
            self.b -= self.learning_rate * gradient_b
        return self

    def predict_proba(self, x):
        return [sigmoid(self.a * xi + self.b) for xi in x]

    def predict(self, x, threshold=0.5):
        return [
            int(probability >= threshold)
            for probability in self.predict_proba(x)
        ]


if __name__ == "__main__":
    x = [-3, -2, -1, 1, 2, 3]
    y = [0, 0, 0, 1, 1, 1]
    model = LogisticRegression().fit(x, y)
    print(model.predict_proba([-1.5, 0, 1.5]))
    print(model.predict([-1.5, 0, 1.5]))
