import random

def draw_card():
    return random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11])

def hand_total(hand):
    total = sum(hand)
    aces = hand.count(11)
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

def player_turn():
    hand = [draw_card(), draw_card()]
    while hand_total(hand) < 21:
        print(f"Your hand: {hand} = {hand_total(hand)}")
        if input("(h)it or (s)tand? ").lower() != "h":
            break
        hand.append(draw_card())
    print(f"You finish on {hand_total(hand)}")
    return hand

def dealer_turn():
    hand = [draw_card(), draw_card()]
    while hand_total(hand) < 17:
        hand.append(draw_card())
    print(f"Dealer has {hand} = {hand_total(hand)}")
    return hand

def winner(player, dealer):
    p, d = hand_total(player), hand_total(dealer)
    if p > 21:
        return "dealer", "Bust! Dealer wins."
    if d > 21 or p > d:
        return "player", "You win!"
    if p == d:
        return "draw", "Push – it's a draw."
    return "dealer", "Dealer wins."

def main():
    chips = 100
    while chips > 0:
        bet = int(input(f"You have {chips} chips. Bet: ") or 10)
        bet = max(1, min(bet, chips))
        player = player_turn()
        dealer = dealer_turn() if hand_total(player) <= 21 else []
        who, msg = winner(player, dealer)
        print(msg)
        if who == "player":
            chips += bet
        elif who == "dealer":
            chips -= bet
        if input("Play again? (y/n) ").lower() != "y":
            break
    print(f"You leave with {chips} chips.")

if __name__ == "__main__":
    main()
