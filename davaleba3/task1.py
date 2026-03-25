#1. მოახდინეთ ორი ვექტორის შეკრების მოდელირება. მოიყვანეთ ორი მაგალითი (შემთხვევითი და სტატიკური რიცხვებისთვის).
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print(f"a = {a}")
print(f"b = {b}")
sum_static = a + b
print("Static sum: ", sum_static)


c = np.random.randint(0, 6, 5)
d = np.random.randint(6, 10, 5)
print(f"c = {c}")
print(f"d = {d}")

sum_rand = c + d
print("Random sum: ", sum_rand)

