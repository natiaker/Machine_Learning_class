# შექმენით ორი 5x5 მატრიცა შემთხვევითი რიცხვებით [0,10] შუალედიდან. გამოთვალეთ მატრიცების ნამრავლი,
# მატრიცების ტრანსპონირებული ვარიანტი და ელემენტური გამრავლება.

import numpy as np

A = np.random.randint(0, 10, (5, 5))
B = np.random.randint(0, 10, (5, 5))

print("A:\n", A)
print("B:\n", B)

matrix_product = np.dot(A, B)
print("Matrix product (A x B): \n", matrix_product)

A_transpose = A.T
B_transpose = B.T
print("Transpose of A: \n", A_transpose)
print("Transpose of B: \n", B_transpose)


elementwise_product = A * B
print("Element-wise product (A * B): \n", elementwise_product)



