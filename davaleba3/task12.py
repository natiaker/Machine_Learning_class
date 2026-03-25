# შექმენით 3x3 მატრიცა შემთხვევითი რიცხვებით [1, 10] შუალედიდან. იპოვეთ მატრიცის დეტერმინანტი და
# ინვერსია numpy.linalg ბიბლიოთეკის გამოყენებით.

import numpy as np

A = np.random.randint(1, 10, size=(3, 3))
det = np.linalg.det(A)

print("A:\n", A)
print("Determinant: ", det)

if det != 0:
    inv_A = np.linalg.inv(A)
    print("Inverse matrix: \n", inv_A)
else:
    print("Inverse doesn't exist")
