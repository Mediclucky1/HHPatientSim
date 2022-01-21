game_start = "yes"

while game_start == "yes":

    print("Welcome to 'HellHole' Hospital!")

    name = input("What the fuck is your name?: ")

    xp = 0

    print("Your nurse's name is: Zeb")

    nurses_name = "Zeb"

    xp += 100

    print("100 XP for spelling your name right. ")

    print("XP =", xp)

    print("{Press Enter to Continue}")

    input()

    print("Welcome", name, "to 'HellHole' Hospital. Home of", nurses_name,

          "and the rest of the craziest, most unstable fucking people I've ever had the pleasure of working alongside with. ")

    input()

    print(nurses_name, "walks into the room and starts telling you to 'undress and get in this fucking gown.' ")

    input()

    a = "You don't escape 'HellHole' Hospital", name, "... 'HellHole' Hospital owns your ass!!! Literally. Bend over bitch. 'KBF' is comin in next... "
    b = "You somehow manage to get on the roof, and you jump off the helipad, but your trajectory must've been fucked. You somehow land on some shit that breaks your fall enough to survive, but you paralyzed. "
    c = "You decided to just own your situation and deal with it. Nope. You end up getting violated by 'Greg'. Mmm. Ain't that some shit. "
    d = "You piss all over their face and decide to sit and watch their reaction. They decide to smother you with a pillow because you are a disgusting piece of shit. What the fuck is wrong with you?"
    e = "You decided you wanna wake up and choose violence today. Bold move Cotton... let's see how this plays out..."
    f = "You have chosen the armageddon option...", name,"... umm... Holy fuckballs... UMM... I wasn't expecting this so... here it goes... "


    answer = input("What do you do? (escape, jump, stay, piss or fight or armageddon option...) ")

    if answer == "escape":

        print(a)

        input()

        print(nurses_name, "decides to call 'King Bitch Face' in and then 'KBF' tears you a new one. Collect 500XP.")

        input()

        if answer is True: xp += 500

        kbf = input("What do you wanna do to 'KBF'? (fight, fuck, or feed?) ")

        if kbf == "fight":

            print("You decided to step to God tonight, and you lose. ")

            input()

            xp = 0

            print("You lose all remaining xp. XP =", xp)

            game_start = input("Play again?: ")

            if game_start == ("yes"):

                continue

            else:

                break

        elif kbf == "fuck":

            print("You sick mother fucker... why?? You lose the whole fucking game for that shit... ")

            input()

            xp = 0

            print("XP =", xp)

            game_start = input("Play again?: ")

            if game_start == ("yes"):

                continue

            else:

                break

        elif kbf == "feed":

            print(

                "You serve up the biggest most beautiful steak dinner you've ever seen. ")

            input()

            print("'KBF' eats it all in one bite. 'KBF' rewards you with a Milli XP. ")

            xp = 1000000

            input()

            print("XP =", xp)

            game_start = input("Play again?: ")

            if game_start == ("yes"):

                continue

            else:

                break

    elif answer == "jump":

        print(b)

        input()

        print("You don't collect any XP. Instead, you slowly accumulate negative XP until you die. ")

        input()

        print("Any surviving family starts losing their XP until they die as well... ")

        input()

        xp = 499

        print("XP =", xp)

        game_start = input("Play again?: ")

        if game_start == ("yes"):

            continue

        else:

            break

    elif answer == "stay":

        print(c)

        input()

        print("'Greg' cuddles you after and you lose all remaining XP.")

        input()

        xp = 0

        print("XP =", xp)

        game_start = input("Play again?: ")

        if game_start == ("yes"):

            continue

        else:

            break

    elif answer == "piss":

        print(d)

        input()

        print("You lose all your damn XP.", nurses_name, "deserves to kill your ass. They get 500XP.")

        input()

        xp = 0

        print("Your XP =", xp)

        input()

        print("Zeb's XP = 500")

        game_start = input("Play again?: ")

        if game_start == ("yes"):

            continue

        else:

            break

    elif answer == "fight":

        print(e)

        input()

        print("You are rewarded with 20mg Geodon, and 2mg of Ativan. You sleep like the beautiful bipolar bitch you are... ")

        xp += 220

        print("XP =", xp)

        game_start = input("Play again?: ")

        if game_start == ("yes"):

            continue

        else:

            break

    elif answer == "armageddon":

        print(f)

        input()

        print("You decide to stab Zeb in the eyes with your thumbs as hard as you can.")

        input()

        print("Zeb attempts to fight back but unfortunate for Zeb you have the Gamer Thumbs of a God. You 'Mountain from GOT' his ass and it makes a super gnarly mess on the floor... ")

        input()

        next_choice = input("Roof, Basement, or Across the street? ").lower()

        if next_choice == "roof":

                print("You decide to try to escape to the roof and make it to the doors to the helipad before Security tackles your ass and you end up a committal. ")

                input()

                print("You lose XP slowly as well, but increased rate due to several Psych holds in the ER... You feel yourself die inside each shift change...")

                input()

                print("Time is not real. I miss the Matrix... What year is it??? ")

                xp -= 69

                print("XP =", xp)

                game_start = input("Play again?: ")

                if game_start == ("yes"):

                    continue

                else:

                    break

        elif next_choice == "basement":

                print("You sneak down into the basement but Security spots you going into the Morgue.")

                input()

                print(nurses_name, "sneaks up behind you and cracks you in the skull with a frying pan.")

                input()

                print("How the fuck did he... you know what... I bet I'm dead... ")

                input()

                print("Well fuck we are united now bruh. 4th wall smashed. I am you.")

                xp = "INFINITE"

                print("XP =", xp)

                game_start = input("Play again?: ")

                if game_start == ("yes"):

                    continue

                else:

                    break

        elif next_choice == "across":

            print("You slip across the street into a shitty chicken restaurant.")

            input()

            print("Hey", name, " what's up??? ")

            input()

            print("I NEED A JOB AND A FAKE STACHE... DON'T ASK QUESTIONS!!! ")

            input()

            print("Your chicken friend gives you a uniform and no one suspects a thing. This is your life now. You gain 500 XP for your effort. ")

            xp += 500

            print("XP =", xp)

            game_start = input("Play again?: ")

            if game_start == ("yes"):

                continue

            else:

                break

    else:

        print("escape. jump. stay, piss, or fight... those are the options guy... start over.")

        game_start = input("Play again?: ")

        if game_start == ("yes"):

            continue

        else:

            break
