import random

def main():
    """Start a number of element guessing game."""
print("Guess the number of element!")

element = [
        1,
        6,
        8,
        7,
        2,
         ]

x = random.choice(element)
print(x) 
    
guess = True


while guess:
    guess = int(input("What number am I thinking of? "))
    
    if guess == 1:
        print(" Congratulations you got it right! It is hydrogen.")
        
    elif guess != 1:
        print("Unfortunately you got the wrong answer. Please try again!")
        
    elif guess == 6:
        print(" Congratulations you got it right!It is carbon.")
        break
        
    elif guess != 6:
        print(" Unfortunately you got the wrong answer. Please try again!")
    
    elif guess == 2:
        print(" Congratulations you got it right! It is helium.")
        break
        
    elif guess != 2:
        print("Unfortunately you got the wrong answer. Please try again!")
        
    elif guess == 8:
        print(" Congratulations you got it right! It is oxygen.")
        break
        
    elif guess != 8:
        print(" Unfortunately you got the wrong answer. Please try again!")
        
    elif guess == 7:
        print("Congratulations you got it right! It is nitrogen")
        break
        guess = False
    else: 
        print("Unfortunately you got the wrong answer. Please try again!") 
 
else:
    ("Jumpa lagi")
    
main()
 
 
 
    







