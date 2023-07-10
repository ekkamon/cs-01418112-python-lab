inc = float(input())
ex = float(input())

print("1234567890" * 3)
print("{:13s}{:>8s} bahts".format('Total Income ', f'{inc:+.2f}'))
print("{:13s}{:>8.2f} bahts".format('Expense ', ex))
print("{:13s}{:08.2f} bahts".format('Profit ', inc + ex))