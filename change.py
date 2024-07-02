# Author: James Dubei
# GitHub username: James-code-creator
# Date: 07/01/2024
# Description: This program breaks down a certain integer between 0-99 into the fewest number of coins

print("Please enter an amount in cents less than a dollar.")
cents = int(input())
Q = (cents // 25)
D = ((cents - Q * 25) // 10)
N = ((cents - Q * 25 - D * 10) // 5)
P = ((cents - Q * 25 - D * 10 - N * 5) // 1)
print("Your change will be:")
print( "Q:", Q)
print("D:", D)
print("N:", N)
print("P:", P)