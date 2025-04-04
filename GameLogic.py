def play_game():
    print("Welcome to the Number Guessing Game!")
    random_number = generate_random_number()
    attempts = 0
    while True:
        guess = get_user_guess()
        attempts += 1
        if guess < random_number:
            print("Too low! Try again.")
        elif guess > random_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break