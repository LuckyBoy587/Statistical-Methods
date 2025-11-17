kings = int(input("Enter the number of Kings in the deck: "))
decks = int(input("Enter the total number of cards in the deck: "))
p1 = kings / decks
print()

print(f"Initial Kings in deck: {kings}")
print(f"Initial total cards in deck: {decks}")
print(f"Probability of drawing the first King: {p1:.4f}")

kings -= 1
decks -= 1
p2 = kings / decks
print(f"Kings remaining after first draw: {kings}")
print(f"Total cards remaining after first draw: {decks}")
print(f"Probability of drawing the second King (given first was King and not replaced): {p2:.4f}")
print(f"Probability of drawing two Kings consecutively without replacement: {(p1 * p2):.4f}")