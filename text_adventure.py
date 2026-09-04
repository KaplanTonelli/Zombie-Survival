"""
Implements the text-base adventure experience:
Zombie Survival
Kaplan Tonelli - September 2026
"""
def killed_janitor(item: str, money : str, bullets : str, gun : str,been_closet:bool=False) -> None:
    print("""You look inside the closet and find 2 ammo, and another $350""")
    money+=350
    bullets+=2

    response: str=input("""Now you can:
    1.Go back to the surface OR
    2.Continue down the tunnel
    Choose a number>""")

    if "1" in response: 
        leave_through_window(item,money,bullets,gun,been_closet)
    elif "2" in response:
        continue_on(item,money,bullets,gun)
    else:
        print("Invalid response")
        killed_janitor(item,money,bullets,gun,been_closet)

def janitors_closet(item: str, money : str, bullets : str, gun : str,been_closet:bool=False) -> None:
    print("""You open up the janitors closet, and before you can react, a zombie jumps out at you""")

    response: str=input("""
        You try to 
        1. kick it off,
        2. you try to use your axe 
        3.shoot it with your pistol OR
        4.shoot it with your shotgun
        Choose a number>""")

    if "1" in response:
        print("""Its useless the zombie overpowers you and eats you DEATH
        
        """)
        main()

    elif "2" in response:
        print("""You swing your axe but its too slow! The zombie eats your face DEATH
        
        """)
        main()

    elif "3" in response:
        if gun == "pistol" and bullets>=1:
            bullets-=1
            print("Nice! You shoot it in the head with your pistol WHUMP")
            killed_janitor(item,money,bullets,gun,been_closet)
        else:
            print("You dont have that!")
            janitors_closet(item,money,bullets,gun,been_closet)
    elif "4" in response:
        if gun == "shotgun" and bullets>=1:
            bullets-=1
            print("You blow its head off with your shotgun")
            killed_janitor(item,money,bullets,gun,been_closet)
        else:
            print("You dont have that!")
            janitors_closet(item,money,bullets,gun,been_closet)
    else:
        print("Invalid response")
        janitors_closet(item,money,bullets,gun,been_closet)


def gun_store(item: str, money : str, bullets : str, gun : str) -> None:
    print("""You go into the gun store, inside you see a counter, where an old man is chilling, 
    you see some dead zombies behind him, and you see a rack of guns behind him, 
    You ask him how much the guns are, he tells you that the shotgun is $700,
    the pistol is $200 and that a bullet is $50 each because of a shortage""")
    if money is None:
        print("The old man shoos you away, you dont have any money!")
        leave_through_window(item,money,bullets,gun)
    response: str=input("""What would you like to buy?
    1.Buy a pistol ($200),
    2.buy a shotgun (700), 
    3.buy ammo, ($50)
    4.Leave
    Choose a number>""")
        
    if "1" in response:
        if money >= 200:
            money-=200
            gun="pistol"
            print(f"""YOU BOUGHT PISTOL, MONEY =${money}
            """)
            gun_store(item,money,bullets,gun)
        else:
            print(f"Not enough money! MONEY =${money}")
            gun_store(item,money,bullets,gun)
    elif "2" in response:
        if money >= 700:
            money-=700
            gun="shotgun"
            print(f"""YOU BOUGHT SHOTGUN, MONEY =${money}
            """)
            gun_store(item,money,bullets,gun)
        else:
            print(f"Not enough money! MONEY =${money}")
            gun_store(item,money,bullets,gun)
    elif "3" in response:
        if money >= 50:
            money-=50
            bullets+=1
            gun_store(item,money,bullets,gun)
            print(f"""YOU BOUGHT BULLET, MONEY =${money}
            """)
        else:
            print(f"Not enough money! MONEY =${money}")
            gun_store(item,money,bullets,gun)
    elif "4" in response:
        leave_through_window(item,money,bullets,gun)
    else:
        print("Invalid response")
        gun_store(item,money,bullets,gun)
def continue_down_street(item: str, money : str, bullets : str, gun : str) -> None:
    print("""You continue down the street eventually coming upon a gun store""")

    response: str=input("""You can:
    1. go back
    2. go in the store, OR
    3. keep going down the street
    Choose a number>""")
    
    if "1" in response: 
        leave_through_window(item,money,bullets,gun)
    elif "2" in response:
        gun_store(item,money,bullets,gun)    
    elif "3" in response:
        print("""You continue down the street until a zombie jumps on your head from above legitimately sliming you DEATH
        
        """)
        main()
    else:
        print("Invalid response")
        continue_down_street(item,money,bullets,gun)
def fight_them(item: str, money : str, bullets : str, gun : str) -> None:
    print("""What do you attack them with?""")

    response: str=input("""Choose one: 
    1. Fight them with hands, OR
    2. Fight them with axe OR
    3. Fight them with pistol
    4. Fight them with shotgun and less than 3 ammo
    5. Fight them with shotgun and more than 3 ammo
    Choose a number>""")

    if "1" in response:
        print("""not even close but nice try DEATH
        
        """)
        main()
    elif "2" in response:
        if item=="axe":
            print("""You whip out your old axe and they shoot you DEATH
            
            """)
            main()
        else:
            print("You dont have that!")
            fight_them(item,money,bullets,gun)
    elif "3" in response:
        if gun=="pistol":
            print("""You fire your pistol and get one of them, but theres too many and they overwhelm you DEATH
            
            """)
            main()
        else:
                    print("You dont have that!")
                    fight_them(item,money,bullets,gun)
    elif "4" in response:
        if gun=="shotgun" and bullets<3:
            print("""you take out of couple but run out of ammo and they slime you, so close :C DEATH
            
            """)
            main()
        else:
            print("You dont have that!")
            fight_them(item,money,bullets,gun)
    elif "5" in response:
        if gun=="shotgun" and bullets>3:
            print("""You attack them with your shotgun, and 3 bullets is enough to take the mall out, you take their car and leave YOU WIN
            
            """)
            main()
        else:
            print("You dont have that!")
            fight_them(item,money,bullets,gun)
    else:
        print("Invalid response")
        fight_them(item,money,bullets,gun)
def light_tunnel(item: str, money : str, bullets : str, gun : str) -> None:
    print("""Down the lighter tunnel you eventually come to a large checkpoint that it looks like some refuges are running, 
    They tell you, that you have to give them $800 give you a car to escape""")

    response: str=input("""You can either:
    1. You can fight them and take the car, OR 
    2. you can pay them the money, OR 
    3. refuse
    Choose a number>""")
    
    if "1" in response: 
        fight_them(item,money,bullets,gun)
    elif "2" in response:
        print("""you give them them the money, and they shoot you DEATH
        
        """)
        main()
    elif "3" in response:
        print("""You refuse, and they shoot you DEATH
        
        """)
        main()
    else:
        print("Invalid response")
        light_tunnel(item,money,bullets,gun)
def continue_on(item: str, money : str, bullets : str, gun : str) -> None:
    print("""You continue down the tunnel and eventually see a fork, one fork has light up ahead the other looks dark""")

    response: str=input("""You can either:
    1. Go down the dark tunnel OR
    2. go down the light tunnel
    Choose a number>""")
    
    if "1" in response: 
        print("""you cant see the dark pit, so you fall into it and die DEATH
        
        """)
        main()
    elif "2" in response:
        light_tunnel(item,money,bullets,gun)          
    else:
        print("Invalid response")
        continue_on
def go_subway(item: str, money : str, bullets : str, gun : str,been_closet: bool = False) -> None:
    print("""You go down into the subway, after a while of going down the stairs, you descend down into the subway,"
    "in front of you, you see a train tunnel and what looks like a janitors closet""")

    response: str=input("""You can either:
    1. You can check the janitors closet, OR
    2. you can just go down the tunnel
        Choose a number>""")

    if "1" in response:
        if not been_closet:
            janitors_closet(item,money,bullets,gun,been_closet=True)
        else:
            print("You've already been there")
            go_subway(item,money,bullets,gun,been_closet=True)
    elif "2" in response:
        continue_on(item,money,bullets,gun)
    else:
        print("Invalid response")
        go_subway(item,money,bullets,gun,been_closet)

def exit_door(Item: str, money: str, bullets: str, gun : str):
    print("""You forget to silently close the door, and BANG, a group of zombies across the hall turn towards you and pounce, you dont stand a chance DEATH
    
    """)
    main()
def away_from_zombies(item: str) -> None:
    print("""once out on the street you see a couple places to go""")

    response: str=input("""You can either:
    1. Go left and die to zombies
    2. Go right and die to zombies
    Choose a number>""")
    if "1" in response: 
        print("you die to zombies")
        main()
    elif "2" in response:
        print("you die to zombies")
        main()
    else:
        print("Invalid response")
        away_from_zombies
    
    main()
def random_room(item: str) -> None:
    money: int = 600
    bullets: int = 2
    print("""luckily in the random room you find $600, and 2 bullets
    Unluckily the window is all boarded up so you cant exit through the fire escape""")

    response: str=input("""You can either:
    1. NEED AXE: break through the boards with your axe OR
    2. exit through the door again
    Choose a number>""")

    if "1" in response: 
        if item=="axe":
            leave_through_window(item,money,bullets,None)
        else:
            print("you dont have an axe!")
            random_room() 
    elif "2" in response:
        exit_door(item,money,bullets)
    else:
        print("Invalid response")
        random_room

def leave_through_window(item: str,money: str,bullets: str, gun : str,been_closet:bool=False) -> None:

    print("You are now safely out on the street")

    response: str=input("""You are now behind the building would you like
    to:
    1. go to the subway, OR you can 
    2. continue on looking for more things
    Choose a number>""")

    if "1" in response: 
        go_subway(item,money,bullets,gun,been_closet)
    elif "2" in response:
        continue_down_street(item,money,bullets,gun)
    else:
        print("Invalid response")
        continue_down_street(item,money,bullets,gun,been_closet)

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
def choose_first_action(item: str,money: str,bullets:str,gun:str) -> None:

    print(f"""You choose the {item} but quick you need to escape!""")

    response: str=input("""Now you can either
    1. leave through the window down the fire escape OR
    2. out of your door
    Choose a number>""")

    if "1" in response: 
        leave_through_window(item,money,bullets,gun) 
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

    choose_first_action(item,None,None,None)


if __name__ == "__main__":
    main()