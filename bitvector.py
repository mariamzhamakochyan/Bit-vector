class BitVector:
    def __init__(self, size):
        self.size = size
        self.vector = [0] * (size // 64 + 1)
        
    def set(self, index):
        idx = index // 64
        self.vector[idx] |= 1 << (index % 64)

    def reset(self, index):
        idx = index // 64
        self.vector[idx // 64] &= 0 << (index % 64)

    
    def show(self, index):
        idx = index // 64
        return (self.vector[idx] >> (index % 64))


