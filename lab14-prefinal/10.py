values = {
    'A': 1,
    'J': 10.01,
    'Q': 10.02,
    'K': 10.03,
}

def backjack(cards):
    max_value = 0
    max_card = ''
    total = 0
    count = 0
    
    for card in cards:
        val = int(card) if card.isdigit() else values[card]
        
        if total > 16 or count >= 5:
            break
        
        total += int(val)
        count += 1
        
        if val > max_value:
            max_value = val
            max_card = card
        
    print(max_card)
    print('busted' if total > 21 else total)

def main():
    cards = str(input()).split(' ')
    backjack(cards)
    
main() 