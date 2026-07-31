class HopfieldNetwork:
    def __init__(self, size):
        self.size = size
        self.weights = [[0.0] * size for _ in range(size)]

    def fit(self, patterns):
        for i in range(self.size):
            for j in range(self.size):
                if i != j:
                    self.weights[i][j] = sum(
                        pattern[i] * pattern[j] for pattern in patterns
                    ) / self.size

    def recall(self, damaged_pattern, max_sweeps=20):
        state = damaged_pattern[:]
        for _ in range(max_sweeps):
            changed = False
            for i in range(self.size):
                field = sum(
                    self.weights[i][j] * state[j]
                    for j in range(self.size)
                )
                new_value = 1 if field > 0 else -1 if field < 0 else state[i]
                if new_value != state[i]:
                    state[i] = new_value
                    changed = True
            if not changed:
                break
        return state


patterns = [
    [1, 1, 1, -1, -1, -1, 1, 1, 1],
    [1, -1, 1, 1, -1, 1, 1, -1, 1],
]

network = HopfieldNetwork(size=9)
network.fit(patterns)

damaged = [1, 1, -1, -1, -1, -1, 1, 1, 1]
print(network.recall(damaged))

