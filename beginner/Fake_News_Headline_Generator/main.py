import random

subjects = [
    "Tom Cruise",
    "Pat Cummins",
    "Cat",
    "Hive of bees",
    "Elon Musk"
]

actions = [
    "launches popcorns",
    "cancels the deal",
    "dances with strangers",
]

place_or_things = [
    "at Brooklyn Bridge",
    "working from home",
    "at the park",
    "during fifa tournament",
    "at Navy Pier"
]


while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(place_or_things)

    headline = f" BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n" + headline)

    user_input = input("\n Do you want another headline? (yes/no) ".strip().lower())

    if user_input == "no":
        break

print("\n Thanks for using the Fake News Headline Generator")
