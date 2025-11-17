toss = int(input("Enter number of coin tosses: "))
dice = int(input("Enter desired dice number (1–6):\n"))

print("--- Coin Toss Results ---")

import random
heads = random.randint(0, toss)
tails = toss - heads

print(f"Head: {heads}, Tail: {tails}")
print(f"Probability of Head: {heads/toss:.2f}")
print(f"Probability of Tail: {tails/toss:.2f}")

print("--- Dice Roll Probability ---")
print(f"The probability of rolling a {dice} is: {1/6:.4f}")
print("Which is also: 1/6")