import random

print("Welcome to Rock, Paper, Scissors!")
print("Developed by Seth Christmus.")
print("ASCII art source: https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe")

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

if user_choice == 0:
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)
elif user_choice == 1:
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)
else:
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)

print("\n")
print("Computer chose:\n")

if computer_choice == 0:
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)
elif computer_choice == 1:
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)
else:
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)

if user_choice == 0 and computer_choice == 2:
    print("You win!!!")
elif user_choice == 1 and computer_choice == 0:
    print("You win!!!")
elif user_choice == 2 and computer_choice == 1:
    print("You win!!!")
elif user_choice == computer_choice:
    print("Draw!")
else:
    print("You lose.")

