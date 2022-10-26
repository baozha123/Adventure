name = input("Type your name: ")
print(name,", welcome to this adventure. Always Type one action per turn.")

answer = input("You woke up finding yourself in a mystery world, where you have become a character."
               "Choose your class between a wizard or a warrior: ").lower()
if answer == "wizard":
    answer = input("Leveled up! You are now Lv 1. Your mission is to get to level 10 and defeat Baron."
        "You can equip weapon and armour to boost your gear score."
        "You can also kill mobs to gain exp in order to level up. What is your next move? ").lower()
elif answer == "warrior":
    answer = input("Leveled up! You are now Lv 1. Your mission is to get to level 10 and defeat Baron."
          "you can equip weapon and armour to boost your gear score. "
          "You can also kill mobs to gain exp in order to level up. What is your next move? ").lower()

string = "equip weapon and armour"
if answer in string:
    answer = input("You have equipped weapon and armour, what's your next move? ").lower()
else:
    answer = input("You killed 10 mobs and leveled to level 10. What is your next move? ").lower()
string = "defeat baron"
if answer in string:
    print("Congratulations! You have defeated the Baron. Mission Complete!")
    quit()
else:
    answer = input("You have leveled to level 10. What is your next move? ")
string = "defeat baron"
if answer in string:
    print("Congratulations! You have defeated the Baron. Mission Complete!")
    quit()






