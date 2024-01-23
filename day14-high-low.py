import day14_high_low_data as day14
import random

def show_ab_data(ig_data, ab):
    ig_name = ig_data["name"]
    ig_followers = ig_data["follower_count"]
    ig_description = ig_data["description"]
    ig_country = ig_data["country"]
    if ab == "A":
        ab_phrase = "Compare A"
    else:
        ab_phrase = "Against B"
    print(f"{ab_phrase}: {ig_name}, a {ig_description}, From {ig_country}")
    return ig_followers

def check_answer(ig_followers_a, ig_followers_b, user_answer, user_score):
    keep_going = True
    if ig_followers_a > ig_followers_b:
        correct_answer = "A"
    else:
        correct_answer = "B"
    if user_answer == correct_answer:
        user_score += 1
        print(f"You're right! Current score: {user_score}")
    else:
        print(f"Sorry, that's wrong. Final score: {user_score}")
        keep_going = False
    return keep_going, user_score

def high_low():
    score = 0
    play = True
    while play:
        followers_a = show_ab_data(random.choice(day14.data), "A")
        followers_b = show_ab_data(random.choice(day14.data), "B")
        answer = input("Who has more followers? Type 'A' or 'B': ")
        play, score = check_answer(followers_a, followers_b, answer, score)

high_low()
