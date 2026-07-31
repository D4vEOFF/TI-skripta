import random


WIDTH, HEIGHT = 4, 3
START = (0, 0)
GOAL = (3, 2)
TRAP = (3, 0)
WALL = (1, 1)
ACTIONS = ("up", "right", "down", "left")
MOVE = {
    "up": (0, 1),
    "right": (1, 0),
    "down": (0, -1),
    "left": (-1, 0),
}


def step(state, action):
    dx, dy = MOVE[action]
    candidate = (state[0] + dx, state[1] + dy)
    x, y = candidate
    if not (0 <= x < WIDTH and 0 <= y < HEIGHT) or candidate == WALL:
        candidate = state
    if candidate == GOAL:
        return candidate, 10, True
    if candidate == TRAP:
        return candidate, -10, True
    return candidate, -1, False


def train(episodes=3000, alpha=0.2, gamma=0.9, epsilon=0.1):
    states = [
        (x, y)
        for x in range(WIDTH)
        for y in range(HEIGHT)
        if (x, y) != WALL
    ]
    q = {(state, action): 0.0 for state in states for action in ACTIONS}

    for _ in range(episodes):
        state = START
        done = False
        while not done:
            if random.random() < epsilon:
                action = random.choice(ACTIONS)
            else:
                action = max(ACTIONS, key=lambda a: q[state, a])

            new_state, reward, done = step(state, action)
            continuation = 0.0 if done else max(
                q[new_state, a] for a in ACTIONS
            )
            q[state, action] += alpha * (
                reward + gamma * continuation - q[state, action]
            )
            state = new_state

    return q


if __name__ == "__main__":
    q = train()
    policy = {
        state: max(ACTIONS, key=lambda action: q[state, action])
        for state in {state for state, _ in q}
        if state not in (GOAL, TRAP)
    }
    print(policy)
