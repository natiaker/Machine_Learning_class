# შეავსეთ 10x10 მატრიცა შემთხვევითი რიცხვებით [0, 10] შუალედიდან. შეცვალეთ ყველა 0-ის მნიშვნელობა 1-ით.
# გამოიყენეთ NumPy ბიბლიოთეკა.

import numpy as np

A = np.random.randint(0, 10, (10, 10))
print("Random Matrix: \n", A)

A[A == 0] = 1
print("new matrix: \n", A)
