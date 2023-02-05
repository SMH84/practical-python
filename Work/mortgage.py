# mortgage.py
#
# Exercise 1.7

# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 1
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000


while principal > 0:
    if month in range(extra_payment_start_month, extra_payment_end_month + 1):
        payment = payment + extra_payment
    principal = principal * (1+rate/12) - payment
    if principal < 0:
        print("You overpaid by", abs(principal))
        principal = 0
    total_paid = total_paid + payment
    if month in range(extra_payment_start_month, extra_payment_end_month + 1):
        payment = payment - extra_payment
    print(month, total_paid, principal)
    month = month + 1


print('Total paid', total_paid)
print('Total months', month - 1)
