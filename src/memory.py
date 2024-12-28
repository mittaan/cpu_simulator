class Memory:
    def __init__(self, size=2**16):
        self.Data = []

        for _ in range(size):
            self.Data.append(0x0)