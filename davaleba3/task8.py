# ააგეთ 8x8 ზომის ჭადრაკის დაფა. გამოიყენეთ NumPy ბიბლიოთეკა.

import numpy as np

board = np.zeros((8, 8), int)

board[1::2, ::2] = 1
board[::2, 1::2] = 1

print(board)
