def num_guessing_game():
    print("Welcome to my brain teaser game")
    print("Tell us the name of the country that started with [P] you are thinking of right now....! ")
    print("Remember you have only 5 attempts to guess the NAME  correctly!")
    My_secret_country = "Paris"
    num_of_attempts =5
    while num_of_attempts > 0:
        try:
            your_guess = input("can you enter your ({num_of_attempts}) name here: ")
            num_of_attempts -= 1
            if your_guess != My_secret_country:
                print( "You are wrong sorry!")
            else:
                print("Congratulations you have gussed it right and the name is {My_secret_country} ")
                break
        except ValueError:
            print("Your guess is invalid!!!!11")
num_guessing_game()
        #if not_guessed_correctly:
     






    