"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.

charge = 0.00
numChars = input("Enter number of characters: ")
woodType = input("Enter wood type (pine or oak): ")
color = input("Enter color (black or gold): ")

# Charge for this sign.
# Number of characters.
# Color of characters.
# Type of wood.
# Write assignment and if statements here as appropriate.

charge = 35.00 + (int(numChars) - 5) * 4

if (color == "gold"):
  charge += 15.00
else:
  charge += 0.00

if (woodType == "oak"):
  charge += 20.00
else:
  charge += 0.00

# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))
