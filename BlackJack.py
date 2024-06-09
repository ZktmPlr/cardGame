import random
#dzien dobry klasa 2 i/p? szukamy 5 dziew... HAHAHAHAHAHAHAHAHA
class Pick:
    def __init__(self, values):
        #gówno ktore trzeba definować
        self.values = values

values = [2, 3, 4, 5, 6, 7, 8, 9, 10,10,10,10, 11]

#calculate total value of cards
def calculate_total(cards):
    total = sum(cards)
    # if value 11 and would give more than 21 total then go with 1
    if 11 in cards and total > 21:
        total -= 10
    return total

# 2 karty na start rozdane
player_cards = [random.choice(values) for _ in range(2)]
dealer_cards = [random.choice(values) for _ in range(2)]

#wydruk
print("Your cards:", player_cards)
print("Dealer's cards:", dealer_cards[0])  #Show only first card
# My turn
while True:
    if calculate_total(player_cards) > 21:
        print("fanum taxed! You lost.")
        break
    action = input("Do you want to hit with a rizz? (type 'h') or stand on rizz party (type 's')? ").lower()
    if action == 'h':
        new_card = random.choice(values)
        player_cards.append(new_card)
        print("You drew:", new_card)
        print("Your cards:", player_cards)
    elif action == 's':
        break

# Dealer's turn
while calculate_total(dealer_cards) < 17:
    new_card = random.choice(values)
    dealer_cards.append(new_card)
    print("Dealer drew:", new_card)
    print("Dealer's cards:", dealer_cards)

# Winner
player_total = calculate_total(player_cards)
dealer_total = calculate_total(dealer_cards)

if player_total > 21:
    print("You skibidi! Dealer mogs you.")
elif dealer_total > 21:
    print("Dealer gooned! You rizzing hard.")
elif player_total > 21 and dealer_total > 21:
    print("Tie!")
elif player_total > dealer_total:
    print("You rizzed real hard!")
elif player_total < dealer_total:
    print("Dealer brutally mogs.")
else:
    print("its not tik tok rizz party. Tie!")