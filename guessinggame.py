import random

num = random.randint(0, 10)
answer = -1
score = 10
while int(answer) != int(num):
        answer = input("Enter in your number: ")
        answer = int(answer)
        score -= 1

print("Score: " + str(score))
