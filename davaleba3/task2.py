# . მოახდინეთ ორი ვექტორის გამრავლების მოდელირება. მოიყვანეთ ორი მაგალითი
# (შემთხვევითი და სტატიკური რიცხვებისთვის).
# სასურველია აჩვენოთ ელემენტური გამრავლება და სკალარული ნამრავლი (dot product).

import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print(f"a = {a}")
print(f"b = {b}")

elementwise = a * b
dot_product = np.dot(a, b)

print("elementwise: ", elementwise)
print("dot product(scalar): ", dot_product)


c = np.random.randint(0, 6, 5)
d = np.random.randint(6, 10, 5)
print(f"c = {c}")
print(f"d = {d}")

elementwise_r = c * d
dot_product_r = np.dot(c, d)

print("elementwise: ", elementwise_r)
print("dot product(scalar): ", dot_product_r)
