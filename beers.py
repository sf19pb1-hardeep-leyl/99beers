"""
Output the lyrics to 99 Bottles of Beer using a function
"""

import sys

line1 = "bottles of beer"
line2 = "on the wall"

def chorus(counter):
    print(f"{counter} bottles of beer on the wall, {counter} bottles of beer.")
    print(f"Take one down and pass it around, {counter-1} bottles of beer on the wall")
    return

for i in range (99,0,-1):
    chorus(i)

print("No more bottles of beer on the wall, no more bottles of beer.")
print("Go to the store and buy some more, 99 bottles of beer on the wall.")
