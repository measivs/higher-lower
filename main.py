from art import logo
from art import vs
from game_data import data
import random

print(logo)

right_answer = True
score = 0
previous_winner = None

while right_answer:
    if previous_winner:
        randomly_picked1 = previous_winner
    else:
        randomly_picked1 = random.choice(data)
    
    person_name1 = randomly_picked1['name']
    person_description1 = randomly_picked1['description']
    person_country1 = randomly_picked1['country']
    person_follower_count1 = randomly_picked1['follower_count']
    print(f"compare A: {person_name1}, a {person_description1}, from {person_country1}.")
    print(vs)

    randomly_picked2 = random.choice(data)
    while randomly_picked1 == randomly_picked2:
        randomly_picked2 = random.choice(data)
        
    person_name2 = randomly_picked2['name']
    person_description2 = randomly_picked2['description']
    person_country2 = randomly_picked2['country']
    person_follower_count2 = randomly_picked2['follower_count']
    print(f"against B: {person_name2}, a {person_description2}, from {person_country2}.")
    
    your_answer = input('who has more followers? type "A" or "B": ')
    
    if (your_answer == 'A' and person_follower_count1 > person_follower_count2) or \
            (your_answer == 'B' and person_follower_count1 < person_follower_count2):
        score += 1
        print(f"you're right! current score: {score}.")
        if your_answer == 'A':
            previous_winner = randomly_picked1
        else:
            previous_winner = randomly_picked2
    else:
        print(f"sorry, that\'s wrong. final score: {score}.")
        right_answer = False
