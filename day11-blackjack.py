import random

face_values = {
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
}

def prepare_cards():
    cards = []
    for i in range(4):
        for face in face_values:
            cards.append(face)
    random.shuffle(cards)
    return cards

def draw_card(source, target, count, index):
    for _ in range(count):
        target.append(source[index])
        index += 1
    return target, index

def calc_score(source, is_first):
    score = 0
    for face in source:
        score += face_values[face]
    if is_first:
        if "A" in source and score == 11:
            score = "Blackjack"
    else:
        if score > 21:
            score = "Bust"
        elif source.count("A") > 0 and score == 11:
            score = 21
    return score

def find_blackjack(user_target, com_target):
    results = {
        0: "No blackjack yet.",
        1: "User blackjack. User wins.",
        2: "Com blackjack. Com wins.",
        3: "Both user and com blackjack. Draw."
    }
    user_blackjack = calc_score(user_target, True) == "Blackjack"
    com_blackjack = calc_score(com_target, True) == "Blackjack"
    key = 0
    if user_blackjack:
        key += 1
    if com_blackjack:
        key += 2
    return results[key]    

def hit(source, target, index):
    return draw_card(source, target, 1, index)

def split(source, target, index):
    first_card, second_card = target[0]
    target = [[], []]
    target[0].append(first_card)
    target[1].append(second_card)
    target[0], index = hit(source, target[0], index)
    target[1], index = hit(source, target[1], index)
    return target, index

def user_turn(source, target, index):
    is_user_turn = True
    is_first = True
    option = {
        "t": hit
    }
    menu = {
        "t": "Type 't' (hit) to take a card.",
        "e": "Type 'e' (stand) to end your turn."
    }
    while is_user_turn:
        print(f"User cards: {target}")
        if is_first:
            first_card, second_card = target[0]
            if face_values[first_card] == face_values[second_card]:
                option["s"] = split
                menu["s"] = "Type 's' (split) to split into two."
        for line in menu.values():
            print(line)
        choice = input("Pick a choice: ")
        while not choice in option and choice != "e":
            choice = input("Pick a choice: ")
        if choice == "e":
            is_user_turn = False
        elif choice == "s":
            op = option[choice]
            target, index = op(source, target, index)
            if choice == "s":
                del option["s"]
                del menu["s"]
        else:
            deck_option = []
            for i in range(len(target)):
                if len(target[i]) > 0:
                    score = calc_score(target[i], False)
                    if score != 21 and score != "Bust":
                        deck_option.append(i+1)
            while len(deck_option) > 0:
                for deck_index in deck_option:
                    print(f"{deck_index}: {target[deck_index-1]}")
                deck_choice = int(input("Pick a choice: "))
                while not deck_choice in deck_option:
                    deck_choice = int(input("Pick a choice: "))
                target[deck_choice-1], index = hit(cards, target[deck_choice-1], index)
                new_score = calc_score(target[deck_choice-1], False)
                if new_score == 21 or new_score == "Bust":
                    deck_option.remove(deck_choice)
                    if len(deck_option) == 0:
                        is_user_turn = False
                else:
                    for deck_index in deck_option:
                        print(f"{deck_index}: {target[deck_index-1]}")
                    end_deck = input("Type 'e' if you want to end current deck or enter to continue: ")
                    if end_deck == "e" and len(option) > 0:
                        deck_option.remove(deck_choice)
            is_user_turn = False
        is_first = False
    return target, index

def com_turn(source, target, index):
    score = calc_score(target, False)
    while score != 21 and score != "Bust" and score < 17:
        target, index = draw_card(source, target, 1, index)
        score = calc_score(target, False)
    return target

def compare(user_source, com_source):
    com_score = calc_score(com_source, False)
    for deck in user_source:
        if deck:
            user_score = calc_score(deck, False)
            if user_score == "Bust":
                print(f"User: {deck} (Bust) vs Com: {com_source} ({com_score}) => User loses.")
            elif com_score == "Bust":
                print(f"User: {deck} ({user_score}) vs Com: {com_source} (Bust) => User wins.")
            elif user_score > com_score:
                print(f"User: {deck} ({user_score}) vs Com: {com_source} ({com_score}) => User wins.")
            elif user_score == com_score:
                print(f"User: {deck} ({user_score}) vs Com: {com_source} ({com_score}) => Draw.")
            else:
                print(f"User: {deck} ({user_score}) vs Com: {com_source} ({com_score}) => User loses.")
            
cards = prepare_cards()
user_cards = [[], []]
com_cards = []
index = 0

user_cards[0], index = draw_card(cards, user_cards[0], 2, index)
com_cards, index = draw_card(cards, com_cards, 2, index)

print(f"User cards: {user_cards}")
print(f"Com cards: {[com_cards[0], "*"]}")
blackjack_found = find_blackjack(user_cards[0], com_cards)

if blackjack_found != "No blackjack yet.":
    print(blackjack_found)
else:
    user_cards, index = user_turn(cards, user_cards, index)
    com_cards = com_turn(cards, com_cards, index)
    compare(user_cards, com_cards)
