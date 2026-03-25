# შექმენით 10x10 მატრიცა შემთხვევითი რიცხვებით [0, 10] შუალედიდან.
# იპოვეთ ყველა ელემენტი, რომელიც მეტია 5-ზე.

import numpy as np

A = np.random.randint(0, 10, (10, 10))

greater_than_5 = A[A > 5]
positions = np.where(A > 5)

print("Matrix: \n", A)
print("Greater than 5: \n", greater_than_5)

print("\nPositions of elements greater than 5:")
for row, col in zip(positions[0], positions[1]):
    print(f"{A[row, col]} at row {row}, column {col}")
