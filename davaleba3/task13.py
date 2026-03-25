#შექმენით 10 ელემენტიანი ვექტორი შემთხვევითი რიცხვებით.
# დაალაგეთ ვექტორი ზრდადობით და კლებადობით.

import numpy as np

v = np.random.randint(1, 100, 10)
sorted_asc = np.sort(v)
sorted_desc = np.sort(v)[::-1]

print("Vector: ", v)
print("Sorted ascending: ", sorted_asc)
print("Sorted descending: ", sorted_desc)
