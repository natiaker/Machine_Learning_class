# შეავსეთ 10x10 მატრიცა შემთხვევითი რიცხვებით [0, 10] შუალედიდან.
# წაშალეთ კლავიატურიდან შეტანილი სტრიქონი. გამოიყენეთ NumPy ბიბლიოთეკა.

import numpy as np

A = np.random.randint(0, 10, (10, 10))
print("Random Matrix: \n", A)

row = int(input("Input row to delete: ")) - 1
new_A = np.delete(A, row, axis=0)

print("new matrix: \n", new_A)
