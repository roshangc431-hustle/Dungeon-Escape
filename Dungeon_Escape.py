print("Welcome to Dungeon Escape!")
player_name = input("What is your name? ")

escaped = False
got_key = False
lives = 3

print("\nAlright " + player_name + ", you're stuck in a dark dungeon.")
print("Find a way out before you run out of lives. You've got " + str(lives) + " of them.")

def go_north():
    global lives, got_key
    print("\nYou head north into a cold room with a heavy iron gate.")
    print("There's a riddle written on the wall:")
    print("'I have keys, but no locks. I have space, but no room. You can enter, but you can't go outside. What am I?'")
    answer = input("Your answer (one word): ").strip().lower()

    if answer == "keyboard":
        print("\nNice! The gate unlocks and you grab a shiny golden key.")
        got_key = True
    else:
        print("\nNope, that's not it. Poison darts shoot out and hit you!")
        lives -= 1

    print("You head back to the main room.")

def go_south():
    global lives, got_key, escaped
    print("\nYou walk south and spot a huge wooden door.")

    if got_key:
        print("You put the golden key in the lock... it turns!")
        print("You push the door open and escape into the fresh air. You win, " + player_name + "!")
        escaped = True
    else:
        print("It's locked tight and you don't have a key.")
        print("A trapdoor opens under your feet and you fall onto some spikes. Ouch!")
        lives -= 1
        print("You pull yourself up and go back to the main room.")

def go_east():
    global lives
    print("\nYou go east into an old storage room.")
    drink = input("There's a weird glowing bottle on a shelf. Drink it? (y/n): ").strip().lower()

    if drink == "y" or drink == "yes":
        print("\nWhoa, that actually healed you! You gain 1 life.")
        lives += 1
    else:
        print("\nSmart move, better not risk it. Back to the main room.")

def go_west():
    global lives
    print("\nYou head west and a giant spider drops right in front of you!")
    move = input("Do you run or fight? (run/fight): ").strip().lower()

    if move == "run":
        print("\nYou bolt back to the main room without getting touched.")
    else:
        print("\nYou try to fight it, but it bites you first!")
        lives -= 1
        print("You limp back to the main room.")

while lives > 0 and not escaped:
    print("\n--- Lives left: " + str(lives) + " ---")
    direction = input("Go north, south, east, or west? ").strip().lower()

    if direction == "north" or direction == "n":
        go_north()
    elif direction == "south" or direction == "s":
        go_south()
    elif direction == "east" or direction == "e":
        go_east()
    elif direction == "west" or direction == "w":
        go_west()
    else:
        print("That is not a valid direction. Try north, south, east, or west.")

if not escaped:
    print("\nGame over, " + player_name + ". You ran out of lives down there.")
