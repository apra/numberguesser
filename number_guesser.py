correct_no= 47



guess_count= 0
total_guess= 9

while total_guess>0:
    guess=int(input("What is your guess: "))
    guess_count+=1
    total_guess-=1
    if total_guess<=0:
        print("Game over")
    else:
        if guess>correct_no:
            print(f"{guess} is not the right number. You need to guess lower. You have {total_guess} guesses left ")
        elif guess<correct_no:
            print(f"{guess} is not the right number. You need to guess higher. You have {total_guess} guesses left ")
            continue

        elif guess==correct_no:
            print(f"Congratulations it took you {guess_count} guesses. ")
            break
