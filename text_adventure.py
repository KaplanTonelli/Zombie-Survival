"""
Implements the text-base adventure experience:
Zombie Survival
Kaplan Tonelli - September 2026
"""
def exit_door(Item: str, money: str, bullets: str)
def away_from_zombies(item: str) -> None:
    print("""once out on the street you see a couple places to go""")

    response: str=input("""You can either 
    1. Go left and die to zombies
    2. Go right and die to zombies
    Choose a number>""")
    if "1" in response: 
        print("you die to zombies")
    elif "2" in response:
        print("you die to zombies")
    else:
        print("Invalid response")
        away_from_zombies
    
    main
def random_room(item: str) -> None:
    money: str+=600
    bullets: str+=2
    print("""luckily in the random room you find $600, and 2 bullets
    Unluckily the window is all boarded up so you cant exit through the fire escape""")

    response: str=input("""You can either 
    1. NEED AXE: break through the boards with your axe OR
    2. exit through the door again
        Choose a number>""")

    if "1" in response: 
        leave_through_window(item,money,bullets) 
    elif "2" in response:
        exit_door(item,money,bullets)
    else:
        print("Invalid response")
        leave_through_door

def leave_through_window(item: str,money: str,bullets: str) -> None:

    print("You climb out of the window and down the fire escape safely")

    response: str=input("""You are now behind you building would you like
    to 
    1. go to the subway, OR you can 
    2. continue on looking for more things
    Choose a number>""")
def leave_through_door(item: str) -> None:

    print("""You walk out into the hallway and immediately notice some
     zombies across the hall feasting on some random dude
     Choose a number>""")

    response: str=input("""You can now either 
    1. run into a random room OR 
    2. just straight up go in the opposite direction of the zombies
    Choose a number>""")

    if "1" in response: 
        random_room(item) 
    elif "2" in response:
        away_from_zombies(item)
    else:
        print("Invalid response")
        leave_through_door
def choose_first_action(item: str) -> None:

    print(f"""You choose the {item} but quick you need to escape!""")

    response: str=input("""Now you can either
    1. leave through the window down the fire escape OR
    2. out of your door
    Choose a number>""")

    if "1" in response: 
        leave_through_window(item) 
    elif "2" in response:
        leave_through_door(item)
    else:
        print("Invalid response")
        choose_first_action

def main() -> None:
    print("""You wake up tired groggy, you climb out of bed for your morning coffee
    and look out the window, outside on the streets you see lots of zombies,
    eating people and climbing buildings and such, you go to wash your face and
    think about the zombies WAIT ZOMBIES?? Quick get supplies!!""")

    response: str=input("""grab either: 
    1. your rusty old axe, 
    2. bandages, OR 
    3. food and water
    Choose a number>""")

    item: str=""
    if "1" in response:
        item="axe"     
    elif "2" in response:
        item="bandages"     
    elif "3" in response:
        item="FoodAndWater"    
    else:
        print("Invalid response")
        main()

    choose_first_action(item)


if __name__ == "__main__":
    main()