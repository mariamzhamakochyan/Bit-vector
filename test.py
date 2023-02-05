from bitvector import BitVector

b = BitVector(989)
b.set(7)
print(b.show(7))
b.set(357)
b.reset(7)
print(b.show(7))
print(b.show(357))
