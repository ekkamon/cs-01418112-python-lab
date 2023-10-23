import math

def get_bids():
    users = []
    logs = []
    
    while True:
        data = str(input())
        
        if data == 'end':
            break
        
        name, value = data.split(' ')
        
        logs.append([name, float(value)])
        
        if name not in users:
            users.append(name)
            
    return users, logs
        
def get_user_bids(name, logs):
    data = [val[1] for val in logs if name == val[0]]
    
    last_price = max(data)
    count = len(data)
    
    return last_price, count

def print_the_winner(logs):
    winner = {
        'name': '',
        'price': -math.inf
    }
    
    for data in logs:
        name, price = data
        
        if price > winner['price']:
            winner.update({
                'name': name,
                'price': price
            })
        
    print(f'The winner is {winner["name"]}.')

def print_bids(users, logs):
    users.sort()
    
    for name in users:
        last_price, count = get_user_bids(name, logs)
        
        print(f'{name} bid at the price of {last_price:.1f} baht in {count} {"times" if count > 1 else "time"}.')
    
def main():
    users, logs = get_bids()
    print_bids(users, logs)
    print_the_winner(logs)
    
main()