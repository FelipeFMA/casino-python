import random

play = "y"
bet = 0
money = input("Enter your deposit amount (minimum $100): ").strip()

while not money.isdigit() or float(money) < 100:
    money = input("Invalid amount. Please enter at least $100: ")

money = float(money)

while play.lower() == "y":
    bet = float(input(f"\nHow much would you like to bet? (Available: ${money:.2f}): "))

    x, y, z = random.choices(["🍒", "🍉", "🍌"], k=3)

    print(f"\n {x} {y} {z} | 🎰\n")

    if x == y == z:
        winnings = bet * 2
        money += winnings
        print(f"🎉 Congratulations! You won ${winnings:.2f}! Your new balance: ${money:.2f}")
    else:
        money -= bet
        print(f"😢 You lost ${bet:.2f}. Your remaining balance: ${money:.2f}")

    if money < 1:
        print("💸 You're out of money! Game over.")
        break

    play = input("Do you want to play again? (y/n): ").strip().lower()
