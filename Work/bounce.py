# bounce.py
#
# Exercise 1.5

ball_height = 100

for drop in range(1,11):
    ball_height = ball_height * (3/5)
    print(drop, round(ball_height, 4))