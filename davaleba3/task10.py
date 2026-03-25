# შექმენით 10 ელემენტიანი ვექტორი, რომელიც შეიცავს შემთხვევით რიცხვებს [0, 100] შუალედიდან. იპოვეთ მინიმუმი, მაქსიმუმი,
# საშუალო მნიშვნელობა და სტანდარტული გადახრა NumPy
# სტატისტიკური ფუნქციების გამოყენებით.

import numpy as np

vector = np.random.randint(0, 100, 10)
print("vector: ", vector)

min_val = np.min(vector)
max_val = np.max(vector)
mean_val = np.mean(vector)
std_val = np.std(vector)

print("Min: ", min_val)
print("Max: ", max_val)
print("Mean: ", mean_val)
print("Std: ", std_val)
