# დააგენერირეთ 1000 შემთხვევითი რიცხვი ნორმალური განაწილებიდან (Normal Distribution). იპოვეთ მათი საშუალო მნიშვნელობა
# და სტანდარტული გადახრა NumPy ფუნქციების გამოყენებით.

import numpy as np

data = np.random.randn(1000)

mean_val = np.mean(data)
std_val = np.std(data)

print("First 10 elements: \n", data[:10])
print("Mean = ", mean_val)
print("Standard Deviation: ", std_val)

