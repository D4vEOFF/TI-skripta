from math import dist


def mean(points):
    dimension = len(points[0])
    return tuple(
        sum(point[j] for point in points) / len(points)
        for j in range(dimension)
    )


def assign(points, centers):
    return [
        min(range(len(centers)), key=lambda j: dist(point, centers[j]))
        for point in points
    ]


def update(points, labels, centers):
    new_centers = []
    for j, old_center in enumerate(centers):
        cluster = [
            point for point, label in zip(points, labels)
            if label == j
        ]
        new_centers.append(mean(cluster) if cluster else old_center)
    return new_centers


def kmeans(points, k, max_iterations=100, tolerance=1e-6):
    if not 1 <= k <= len(points):
        raise ValueError("k must be between 1 and the number of points")

    centers = list(points[:k])
    for _ in range(max_iterations):
        labels = assign(points, centers)
        new_centers = update(points, labels, centers)
        movement = max(
            dist(old, new)
            for old, new in zip(centers, new_centers)
        )
        centers = new_centers
        if movement <= tolerance:
            break

    return labels, centers


if __name__ == "__main__":
    data = [(1, 1), (1, 2), (2, 1), (8, 8), (8, 9), (9, 8)]
    labels, centers = kmeans(data, k=2)
    print("labels:", labels)
    print("centers:", centers)
