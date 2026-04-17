import random

random_choice = random.randint(0, 1000)   # 40
atempt = 1
print("--------Number Guessing Game--------")
user_choice = int(input("Guess the number : "))  # 10

while random_choice != user_choice and atempt <= 10:
    if user_choice  < random_choice:
        print(f"Guess a lettle higher! atempt {atempt}")
    else:
        print(f"Guess a leetle lower!  atempt {atempt}")

    user_choice = int(input("Guess the number : "))
    atempt += 1


if atempt == 11:
    print("program ended, maximum atempt reached")
else:
    print(f"congrats you found the nubmer! in {atempt} atempts")