count = int(input())
cash = [int(input()) for _ in range(count)]
balance = int(input())

cash.sort(reverse=True)

for val in cash:
    print(f'{val}: {balance // val}')
    balance %= val