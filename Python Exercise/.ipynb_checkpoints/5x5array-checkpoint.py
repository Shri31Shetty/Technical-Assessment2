#4.Create a 5x5 array with random integers between 1 and 100.
import numpy as np

array_5x5 = np.random.randint(1, 101, size=(5,5))
print("\n5x5 Random Array:\n", array_5x5)