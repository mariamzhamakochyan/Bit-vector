class BitVector:
    def __init__(self, size):
        self.size = size
        self.vector = [0] * (size // 64 + 1)
        
    def set(self, index):
        self.vector[index // 64] |= 1 << (index % 64)
    
    def reset(self, index):
        self.vector[index // 64] &= ~ (1 << (index % 64))

    
    def show(self, index):
        return (self.vector[index // 64] >> (index % 64)) & 1


b = BitVector(989)
b.set(7)
print(b.show(7))
b.set(357)
b.reset(7)
print(b.show(7))
print(b.show(357))


