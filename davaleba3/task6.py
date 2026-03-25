# შეავსეთ 10x10 მატრიცა შემთხვევითი რიცხვებით [0, 10] შუალედიდან. წაშალეთ კლავიატურიდან შეტანილი სვეტი.
# გამოიყენეთ NumPy ბიბლიოთეკა.

import numpy as np

A = np.random.randint(0, 10, (10, 10))
print("Random Matrix: \n", A)

column = int(input("Input column to delete: ")) - 1
new_A = np.delete(A, column, axis=1)

print("new matrix: \n", new_A)
