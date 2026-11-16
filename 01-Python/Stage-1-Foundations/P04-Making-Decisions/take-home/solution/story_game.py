print("You wake up in a dark forest. A path splits LEFT and RIGHT.")
health = 3
has_key = False

choice = input("Which way? (left/right) ").lower().strip()
if choice == "left":
    print("You find a rusty key half-buried in the mud.")
    has_key = True
    choice = input("Pick it up and keep walking, or climb a tree to look around? (walk/climb) ").lower().strip()
    if choice == "climb":
        print("A branch snaps! You fall and hurt your ankle.")
        health -= 2
    print("You reach an old stone door.")
    choice = input("Try to open it? (yes/no) ").lower().strip()
    if choice == "yes" and has_key and health > 1:
        print("The key turns... behind the door is a treasure room. YOU WIN! 🏆")
    elif choice == "yes" and has_key:
        print("You open the door but are too injured to carry the treasure. So close!")
    else:
        print("You sit by the door until nightfall. A wolf howls... THE END.")
elif choice == "right":
    print("You hear a river ahead and a strange humming to your left.")
    choice = input("Follow the river or the humming? (river/humming) ").lower().strip()
    if choice == "river":
        print("The river leads to a village. You're safe and they give you dinner. GOOD ENDING.")
    elif choice == "humming":
        print("The humming is a swarm of bees! You run until you're lost forever. BAD ENDING.")
    else:
        print("You can't decide and fall asleep. You wake up at home – was it a dream?")
else:
    print("You stand still so long that moss grows on you. THE END.")
