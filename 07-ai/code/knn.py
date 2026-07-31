from collections import Counter
from math import dist


class KNNClassifier:
    def __init__(self, k=3):
        if k < 1:
            raise ValueError("k must be positive")
        self.k = k
        self.x_train = []
        self.y_train = []

    def fit(self, x, y):
        if len(x) != len(y) or not x:
            raise ValueError("x and y must have the same non-zero length")
        if self.k > len(x):
            raise ValueError("k cannot exceed the number of objects")
        self.x_train = list(x)
        self.y_train = list(y)
        return self

    def predict_one(self, x):
        neighbours = sorted(
            zip(self.x_train, self.y_train),
            key=lambda item: dist(x, item[0]),
        )[:self.k]
        votes = Counter(label for _, label in neighbours)
        return min(votes, key=lambda label: (-votes[label], label))

    def predict(self, x):
        return [self.predict_one(point) for point in x]


if __name__ == "__main__":
    x = [(1, 1), (2, 1), (2, 2), (6, 5), (7, 5), (7, 6)]
    y = [0, 0, 0, 1, 1, 1]
    model = KNNClassifier(k=3).fit(x, y)
    print(model.predict([(2, 3), (6, 4)]))
