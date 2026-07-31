from math import exp
from random import Random


def sigmoid(z):
    return 1.0 / (1.0 + exp(-z))


class NeuralNetwork:
    def __init__(self, input_size, hidden_size, seed=0):
        random = Random(seed)
        self.hidden_weights = [
            [random.uniform(-1.0, 1.0) for _ in range(input_size)]
            for _ in range(hidden_size)
        ]
        self.hidden_biases = [0.0] * hidden_size
        self.output_weights = [
            random.uniform(-1.0, 1.0) for _ in range(hidden_size)
        ]
        self.output_bias = 0.0

    def forward(self, inputs):
        hidden = [
            sigmoid(sum(w * x for w, x in zip(weights, inputs)) + bias)
            for weights, bias in zip(
                self.hidden_weights, self.hidden_biases
            )
        ]
        output = sigmoid(
            sum(w * a for w, a in zip(self.output_weights, hidden))
            + self.output_bias
        )
        return hidden, output

    def fit(self, inputs, targets, learning_rate=0.8, epochs=10000):
        for _ in range(epochs):
            for sample, target in zip(inputs, targets):
                hidden, output = self.forward(sample)

                # For sigmoid and binary cross-entropy:
                output_delta = output - target
                old_output_weights = self.output_weights[:]

                for j, activation in enumerate(hidden):
                    self.output_weights[j] -= (
                        learning_rate * output_delta * activation
                    )
                self.output_bias -= learning_rate * output_delta

                for j, activation in enumerate(hidden):
                    hidden_delta = (
                        output_delta
                        * old_output_weights[j]
                        * activation
                        * (1.0 - activation)
                    )
                    for k, value in enumerate(sample):
                        self.hidden_weights[j][k] -= (
                            learning_rate * hidden_delta * value
                        )
                    self.hidden_biases[j] -= learning_rate * hidden_delta

    def predict(self, inputs):
        return [self.forward(sample)[1] for sample in inputs]


xor_inputs = [(0.0, 0.0), (0.0, 1.0), (1.0, 0.0), (1.0, 1.0)]
xor_targets = [0.0, 1.0, 1.0, 0.0]

network = NeuralNetwork(input_size=2, hidden_size=3)
network.fit(xor_inputs, xor_targets)

for sample, output in zip(xor_inputs, network.predict(xor_inputs)):
    print(sample, round(output, 3), int(output >= 0.5))

