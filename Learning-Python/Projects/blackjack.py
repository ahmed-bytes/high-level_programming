"""BlackJack Simultation."""
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    """Distribute Cards Randomnly."""
    from random import choice

    return choice(cards)


def calculate_score(cards_list):
    """Sum of all the Cards in a list."""
    if sum(cards_list) == 21 and len(cards_list) == 2:
        return 0
    elif sum(cards_list) > 21 and 11 in cards_list:
        cards_list.remove(11)
        cards_list.append(1)

    return sum(cards_list)


def compare(user, computer):
    """Compare the total score of user and computer."""
    if user == computer:
        return "Draw :|"
    elif computer == 0:
        return "Lost, Opponent has BlackJack :("
    elif user == 0:
        return "You won with a BlackJack :)"
    elif user > 21:
        return "You Lost, You went over :("
    elif computer > 21:
        return "You Won, Opponent Went Over :)"
    elif user > computer:
        return "You won :)"
    else:
        return "You Lost :("


def game_on():
    """Start Game."""
    computer_cards = []
    user_cards = []
    iS_GAMEOVER = False
    user_score = 0
    computer_score = 0

    for i in range(0, 2):
        computer_cards.append(deal_card())
        user_cards.append(deal_card())

    while not iS_GAMEOVER:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Cards: {user_cards}\t Score: {user_score}\n")
        print(f"Computer First Card: {computer_cards[0]}\n")

        if user_score == 0 or user_score > 21 or computer_score == 0:
            iS_GAMEOVER = True
        else:
            user_continue_prompt = input(
                "Type 'y' to get another card or type 'n' to pass: "
            )
            if user_continue_prompt == "y":
                user_cards.append(deal_card())
            else:
                iS_GAMEOVER = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Cards: {user_cards}\t Score: {user_score}\n")
    print(f"Computer Cards: {computer_cards}\t Computer Score: {computer_score}\n")
    print(compare(user_score, computer_score))


play_again = "y"

while play_again == "y":
    game_on()
    play_again = input("Type 'y' to play again or 'n' to end: ").lower()
