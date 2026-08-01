def dot(u, v):
    return sum(ui * vi for ui, vi in zip(u, v))


class LinearSVM:
    def __init__(self, learning_rate=0.02, regularization=0.01,
                 epochs=1000):
        self.learning_rate = learning_rate
        self.regularization = regularization
        self.epochs = epochs
        self.weights = []
        self.theta = 0.0

    def fit(self, x, y):
        if len(x) != len(y) or not x:
            raise ValueError("x and y must have the same non-zero length")
        dimension = len(x[0])
        if any(len(row) != dimension for row in x):
            raise ValueError("all input vectors must have the same length")
        if any(label not in (0, 1) for label in y):
            raise ValueError("labels must be 0 or 1")

        self.weights = [0.0] * dimension
        self.theta = 0.0
        for _ in range(self.epochs):
            for vector, label in zip(x, y):
                signed_label = 2 * label - 1
                margin = signed_label * (
                    dot(self.weights, vector) + self.theta
                )

                shrink = 1.0 - (
                    self.learning_rate * self.regularization
                )
                self.weights = [shrink * weight for weight in self.weights]
                if margin < 1.0:
                    self.weights = [
                        weight + self.learning_rate * signed_label * value
                        for weight, value in zip(self.weights, vector)
                    ]
                    self.theta += self.learning_rate * signed_label
        return self

    def decision_function(self, x):
        return [dot(self.weights, vector) + self.theta for vector in x]

    def predict(self, x):
        return [int(score >= 0.0) for score in self.decision_function(x)]


if __name__ == "__main__":
    x = [(-2, -1), (-1, -2), (-2, -2), (1, 2), (2, 1), (2, 2)]
    y = [0, 0, 0, 1, 1, 1]
    model = LinearSVM().fit(x, y)
    print("weights:", [round(value, 3) for value in model.weights])
    print("theta:", round(model.theta, 3))
    print("predictions:", model.predict([(-1, 0), (0, 1), (3, 2)]))
