class Union:
    def __init__(self):
        self.ids = [i for i in range(0, 169)]
        self.sizes = [1 for i in range(0, 169)]

    def root(self, x):
        curr = x
        while self.ids[curr] != curr:
            self.ids[curr] = self.ids[self.ids[curr]]
            curr = self.ids[curr]
        return curr

    def union(self, x, y):
        rootx = self.root(x)
        rooty = self.root(y)
        if self.sizes[rootx] > self.sizes[rooty]:
            self.ids[rooty] = rootx
            self.sizes[rootx] += self.sizes[rooty]
        else:
            self.ids[rootx] = rooty
            self.sizes[rooty] += self.sizes[rootx]

    def find(self, x, y):
        return self.root(x) == self.root(y)

