# Author: Connor Clark
#
# Program to compute Garth's Formula.
# 2/22/2022

# Variables used by all functions.
importance = -1  # 1-10 how important the event is.
sleep = -1  # Hours of sleep attained the night before.
coffee = -1  # Cups of coffee/stimulants consumed.
prep_needed = -1  # Hours of prep needed.
prep_done = -1  # Hours of prep done.
difficulty = -1  # 1-10 difficulty of event.
nervous = -1  # 1-10 How nervous the user is.


def main():
    """Our main function."""
    print("ARE YOU PREPARED (TO GIVE A PRESENTATION, TAKE A TEST, ETC)?" + "\n")
    getuserinput()
    checkdata()
    result = calculate()
    # Give the user their answer.
    print("\n" + "If your level of Preparedness is greater than 1, you will be just fine.")
    print("\n" + "Your level Preparedness is  " + str(result))


def getuserinput():
    """Gets the input needed to calculate the formula
    from the user! If the user input is invalid, it tells the user
    and asks them to enter the data again"""
    global importance
    while not ((importance >= 1) and (importance <= 10)):
        importance = eval(input("Enter the importance of the event (1 - 10 with 10 being \"singing the national "
                                "anthem at the Super Bowl\"): "))
        print(importance)
        if not ((importance >= 1) and (importance <= 10)):
            print("INVALID INPUT")
    global sleep
    while not (0 <= sleep <= 23):
        sleep = eval(input("Enter the hours of sleep you had last night: "))
        print(sleep)
        if not (0 <= sleep <= 23):
            print("INVALID INPUT")
    global coffee
    while not (coffee >= 0):
        coffee = eval(input("Enter the shots of espresso or other stimulants consumed: "))
        print(coffee)
        if not (coffee >= 0):
            print("INVALID INPUT")
    global prep_needed
    while not (prep_needed >= 1):
        prep_needed = eval(input("Enter the hours of preparation needed to excel: "))
        print(prep_needed)
        if not (prep_needed >= 1):
            print("INVALID INPUT")
    global prep_done
    while not (prep_done >= 0):
        prep_done = eval(input("Enter the hours you actually spent preparing: "))
        print(prep_done)
        if not (prep_done >= 0):
            print("INVALID INPUT")
    global difficulty
    while not ((difficulty >= 1) and (difficulty <= 10)):
        difficulty = eval(input("Enter the difficulty of the subject matter (1 - 10 with 10 being \"theoretical "
                                "particle physics\"): "))
        print(difficulty)
        if not ((difficulty >= 1) and (difficulty <= 10)):
            print("INVALID INPUT")
    global nervous
    while not ((nervous >= 1) and (nervous <= 10)):
        nervous = eval(input("Enter the level of nervousness (1 - 10 with 10 being \"tightrope across the Grand "
                             "Canyon on a windy day\"): "))
        print(nervous)
        if not ((nervous >= 1) and (nervous <= 10)):
            print("INVALID INPUT")


def checkdata():
    """Checks the data to ensure no errors will be
    created when calculating."""
    # Check for divide by zero errors
    if (difficulty + nervous + importance) == 0:
        raise Exception("Current numbers for difficulty, nervousness, and importance will"
                        "create a divide by zero error")


def calculate():
    """Runs the calculation."""
    calc = ((8 * prep_done)*(sleep + coffee)) / ((3 * prep_needed)*(difficulty + nervous + importance))
    return calc


main()
