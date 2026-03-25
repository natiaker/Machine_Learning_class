# მოახდინეთ ორი მატრიცის გამრავლების მოდელირება. მოიყვანეთ ორი მაგალითი
# (შემთხვევითი და სტატიკური რიცხვებისთვის).

import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8], [9, 10], [11, 12]])

result1 = np.dot(A, B)
print("static: \n", result1)


C = np.random.randint(0, 10, (2, 3))
D = np.random.randint(0, 10, (3, 2))

result2 = np.dot(C, D)
print("random: \n", result2)
