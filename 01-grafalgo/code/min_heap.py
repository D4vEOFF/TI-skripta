"""Minimova binarni halda ulozena v poli indexovanem od nuly."""


class MinHeap:
    def __init__(self, values=()):
        self.data = []
        for value in values:
            self.insert(value)

    def _parent(self, index):
        return (index - 1) // 2

    def _left(self, index):
        return 2 * index + 1

    def bubble_up(self, index):
        while index > 0:
            parent = self._parent(index)
            if self.data[parent] <= self.data[index]:
                break
            self.data[parent], self.data[index] = (
                self.data[index], self.data[parent]
            )
            index = parent

    def bubble_down(self, index):
        size = len(self.data)
        while self._left(index) < size:
            left = self._left(index)
            right = left + 1
            smaller = left
            if right < size and self.data[right] < self.data[left]:
                smaller = right
            if self.data[index] <= self.data[smaller]:
                break
            self.data[index], self.data[smaller] = (
                self.data[smaller], self.data[index]
            )
            index = smaller

    def insert(self, value):
        self.data.append(value)
        self.bubble_up(len(self.data) - 1)

    def minimum(self):
        if not self.data:
            raise IndexError("Halda je prazdna.")
        return self.data[0]

    def extract_min(self):
        if not self.data:
            raise IndexError("Halda je prazdna.")
        result = self.data[0]
        last = self.data.pop()
        if self.data:
            self.data[0] = last
            self.bubble_down(0)
        return result

    def increase(self, index, new_value):
        if new_value < self.data[index]:
            raise ValueError("Nova hodnota musi byt alespon puvodni.")
        self.data[index] = new_value
        self.bubble_down(index)

    def decrease(self, index, new_value):
        if new_value > self.data[index]:
            raise ValueError("Nova hodnota musi byt nejvyse puvodni.")
        self.data[index] = new_value
        self.bubble_up(index)


if __name__ == "__main__":
    heap = MinHeap([1, 4, 3, 7, 8, 6, 5])
    print("Halda:", heap.data)
    heap.increase(1, 9)
    print("Po increase:", heap.data)
    heap.decrease(5, 2)
    print("Po decrease:", heap.data)
    print("Odebrane minimum:", heap.extract_min())
    print("Vysledna halda:", heap.data)
