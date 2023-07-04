import random
print("hello developer")

username = input(" what is your name? : ")

print(f"Hello {username} how are you")

names = ["eshan", "hablu", "tutul"]
Locattion = ["dhaka",  "rajshahi", "bogura"]
story = ["doggy & Cat Fighing", "Hablu & Gablu Fighing", "Cow 7 Goat fighing "]
role  = ["Farmar", "Fire fighter ", "King"]

randomName = random.choice(names)
randomLocation = random.choice(Locattion)
randomStory = random.choice(story)
randomRole = random.choice(role)

RealStory = f"once apon a time there was a {randomRole} called {randomName}.  "
print(RealStory)
