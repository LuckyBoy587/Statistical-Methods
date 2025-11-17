heads = 0

import random
for _ in range(100):
    heads += random.randint(0, 1)
    
print(f"Number of heads in 100 flips: {heads}")
