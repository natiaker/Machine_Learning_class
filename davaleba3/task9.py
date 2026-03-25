# შეავსეთ ორი 10x10 მატრიცა შემთხვევითი რიცხვებით [0, 10] შუალედიდან. გააერთიანეთ ორივე მატრიცის ელემენტები და
# გადაიყვანეთ ერთ სიად. გამოიყენეთ NumPy ბიბლიოთეკა.

import numpy as np

A = np.random.randint(0, 10, (10, 10))
B = np.random.randint(0, 10, (10, 10))

combined_matrix = A + B
flattened_list = combined_matrix.flatten()

print("A = \n", A)
print("B= \n", B)
print("combined matrix = \n", combined_matrix)
print("flattened list = \n", flattened_list)


