import random

money = float(input("Enter your deposit money :"))
bet = float(input("How much you bet to double it: "))

x = random.randint(1, 3)
y = random.randint(1, 3)
z = random.randint(1, 3)

if x == 1:
    x = "🍒"
if y == 1:
    y = "🍒"
if z == 1:
    z = "🍒"

if x == 2:
    x = "🍉"
if y == 2:
    y = "🍉"
if z == 2:
    z = "🍉"

if x == 3:
    x = "🍌"
if y == 3:
    y = "🍌"
if z == 3:
    z = "🍌"

print("\n", x, y, z, "\n")

if x == y == z:
    bet *= 2
    money += bet
    print("You Won! you have ", money, "You earned ", bet)
else:
    money -= bet
    print("Better luck next time, you loss ", bet ," Do you have ", money)
    play= input(" play again? (y/n)")
