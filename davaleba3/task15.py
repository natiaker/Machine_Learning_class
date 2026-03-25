# . შექმენით 10 ელემენტიანი ვექტორი, სადაც პირველი და ბოლო
# ელემენტი არის 1, ხოლო დანარჩენი ელემენტები არის 0.

import numpy as np

vector = np.zeros(10, dtype=int)

vector[0] = 1
vector[-1] = 1

print(vector)

