# pcost.py
#
# Exercise 1.27

lines = []
stock_sum = 0

with open('Data/portfolio.csv', 'rt') as f:
    next(f)
    for line in f:
        lines.append(line.split(','))

for line in lines:
    stock_sum += int(line[1]) * float(line[2])

print(stock_sum)