# შექმენით 5x5 მატრიცა შემთხვევითი რიცხვებით [0, 10] შუალედიდან.
# გამოთვალეთ თითოეული სტრიქონის ჯამი და თითოეული სვეტის ჯამი.

import numpy as np

A = np.random.randint(0, 10, (5, 5))

row_sums = A.sum(axis=1)
col_sums = A.sum(axis=0)

print("Matrix: \n", A)
print("Row sums: ", row_sums)
print("Column sums: ", col_sums)
