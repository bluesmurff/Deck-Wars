import time, random
hp = 30
enemyhp = 30
enemycardhp = 10
guarded_check = False

def enemyhpcheck():
    global enemyhp,enemycardhp
    if enemycardhp <= 0:
        print("Enemy", enemychoice, "Has been slain")
        enemyhp = enemyhp - 5
        print("Enemy loses 5 HP, AI now has", enemyhp, "HP")
        enemycardhp = 10
        enemymove()
        movetype()
    else:
        pass
def playerhpcheck():
    global cardhp, hp
    if cardhp <= 0:
        print("Players", placedcard0, "Has been slain")
        hp = hp - 5
        print("Player loses 5 HP, you now have", hp, "HP")
        movetype()
    else:
        pass
def place_card():
    global choice, placedcard0, placedcard0_check, placedcard1,placedcard1_check
    print("Current hand:", currenthand)
    choice = input("Which card do you want to place?")
    if choice == "0":
        if placedcard0_check == False:
            print("You place down", currenthand[0])
            placedcard0 = currenthand.pop(0)
            placedcard0_check = True
            enemymove()
        if placedcard0_check == True:
            print("You can't place a card on an occupied tile", placedcard0, "is placed here!")
            movetype()
    if choice == "1":
        if placedcard1_check == False:
            print("You place down", currenthand[1])
            placedcard1 = currenthand.pop(1)
            placedcard1_check = True
            enemymove()
        if placedcard1_check == True:
            print("You can't place a card on an occupied tile", placedcard1, "is placed here!")
            movetype()
def movetype():
    global attackdmg
    global selectedcard
    global cardhp
    choice = input("Type your move...")
    if choice == "select 0":
        if placedcard0_check == True:
            print("You have selected", placedcard0)
            selectedcard = placedcard0
            choice = input("Type your move...")
            if choice == "attack 0":
                attack()
        if placedcard0_check == False:
            print("There is no card here!")
            movetype()
        else:
            print("You haven't placed a card here!")
            movetype()
    if choice == "select 1":
        if placedcard1_check == True:
            print("You have selected", placedcard1)
            selectedcard = placedcard1
            choice = input("Type your move...")
            if choice == "attack 0":
                attack()
        else:
            print("There is no card here!")

    if choice == "place":
        place_card()

def attack():
    global enemychoice
    global enemyhp
    global enemycardhp
    global enemycardmg
    global enemycardefense
    global attackdmg
    global cardhp
    enemycardefense = 3
    if placedcard0 == "Holy Knight":
        attackdmg = 4
    if placedcard0 == "Knight":
        attackdmg = 4
    if placedcard0 == "Archer":
        attackdmg = 4
    if placedcard0 == "Healer":
        attackdmg = 4
    if placedcard0 == "Horseman":
        attackdmg = 5
    if enemychoice == "Archer":
        enemycardmg = 4
        enemycardhp = enemycardhp - attackdmg
        print("Your", selectedcard, "hit the enemys", enemychoice, "for", attackdmg, "damage")
        print("The enemy", enemychoice, "has", enemycardhp, " hp left")
        enemyhpcheck()
        enemymove2()
    if enemychoice == "Skeleton Warrior":
        enemycardmg = 4
        enemycardhp = enemycardhp - attackdmg
        print("Your", selectedcard, "hit the enemys", enemychoice, "for", attackdmg, "damage")
        print("The enemy", enemychoice, "has", enemycardhp, "hp left")
        enemyhpcheck()
        enemymove2()
    if enemychoice == "Orc band":
        enemycardmg = 4
        enemycardhp = enemycardhp - attackdmg
        print("Your", selectedcard, "hit the enemys", enemychoice, "for", attackdmg, "damage")
        print("The enemy", enemychoice, "has", enemycardhp, "hp left")
        enemyhpcheck()
        enemymove2()

def endturncard():
    global drawencard
    drawencard = random.choice(deck)
    print("You draw a card...", drawencard, "added to your hand")
    movetype()

def enemymove():
    global enemydeck
    global enemyhand
    global enemychoice
    global enemycardhp, enemycardmg
    enemydeck = ["Archer", "Skeleton Warrior", "Skeleton Warrior", "Orc band"]
    enemyhand = random.choices(enemydeck, k= 3)
    enemychoice = random.choice(enemyhand)
    if enemychoice == "Archer":
        enemycardmg = 4
    if enemychoice == "Skeleton Warrior":
        enemycardmg = 4
    if enemychoice == "Orc band":
        enemycardmg = 4
    print("Opponent places", enemychoice)

def enemymove2():
    global AIchoice, cardhp
    global AIchoice2
    global Defensechoices
    global AIchoiceD
    global enemycardhp
    global AIchoice3
    print("You have completed your turn...Waiting for AI..")
    AIchoice = ["Attack", "Defense"]
    AIchoice2 = random.choice(AIchoice)
    if AIchoice2 == "Attack":
        cardhp = cardhp - enemycardmg
        print("AI selects", enemychoice, "and attacks players", placedcard0)
        print("Your", placedcard0, "takes", enemycardmg, "damage and has", cardhp, "hp left.")
        playerhpcheck()
        print("Turn ending...")
        cardhp = cardhp - enemycardmg
        movetype()
    if AIchoice2 == 'Defense':
        Defensechoices = ["Heal", "Guard"]
        AIchoiceD = random.choice(Defensechoices)
        if AIchoiceD == "Heal":
            if guarded_check == True:
                print("AI selects", enemychoice, "and attacks players", placedcard0)
                print("Your", placedcard0, "takes", enemycardmg, "damage and has", cardhp, "hp left.")
                print("Turn ending...")
                movetype()
            if enemycardhp >= 8:
                print("AI Guards", enemychoice, "This card will take reduced damage while guarded")
                guarded()
                print("Turn ending...")
                movetype()
            else:
                print("AI heals", enemychoice, "for 2 HP")
                enemycardhp = enemycardhp + 2
                print("Turn ending...")
                movetype()
        if AIchoiceD == "Guard":
            if guarded_check == True:
                print("AI selects", enemychoice, "and attacks players", selectedcard)
                print("Your", placedcard0, "takes", enemycardmg, "damage and has", cardhp, "hp left.")
                print("Turn ending...")
                movetype()
            if enemycardhp >= 8:
                print("AI Guards", enemychoice, "This card will take reduced damage while guarded")
                guarded()
                print("Turn ending...")
                movetype()
            else:
                print("AI heals", enemychoice, "for 2 HP")
                enemycardhp = enemycardhp + 2
                print("Turn ending...")
                movetype()


def guarded():
    global guarded_check
    global enemycardefense
    guarded_check = True
    enemycardefense = enemycardefense + 2

deck = ["Holy knight", "Knight", "Healer", "Archer", "Horseman"]
print("█▀▄ █▀▀ █▀▀ █▄▀ █░█░█ ▄▀█ █▀█ █▀")
print("█▄▀ ██▄ █▄▄ █░█ ▀▄▀▄▀ █▀█ █▀▄ ▄█")
print("LOADING GAME FILES...")
time.sleep(2)
print("Loaded all files")

print("Deckwars presented by Bluesmurf...")
time.sleep(1)
print("Before we start the game has a set of rules and a learning curve. If this is your first time playing, consider reading the help text file where you put your deckwars download.")
choice = input("Press type 1 to begin...")
if choice == "1":
    print("Welcome to deckwars..")
    time.sleep(1)
    print("Keep in mind any bugs you find can be helpful so be sure to report them in the discord which can be found in the help.txt :)")
    time.sleep(1)
    print("Welcome to the tutorial battle!")
    time.sleep(1)
    print("HP:", hp)
    currenthand = random.choices(deck, k= 3)
    print("Current Hand:", currenthand)
    choice = input("To play a card type the number of which card you want to place. For example your first card would be 0")
    if choice == "0":
        global attackdmg
        print("You place down", currenthand[0])
        placedcard0 = currenthand.pop(0)
        placedcard0_check = True
        enemymove()
        print("Your opponent has placed down a card, You can now attack. Attacking works the same as picking a card, select the card you'd like to attack with, (Your card is on tile 0) and their current card is on 0")
        print("So if you type select 0 and then type attack 0 and you will attack their card!")
        if placedcard0 == "Holy Knight":
            attackdmg = 4
            cardhp = 12
        if placedcard0 == "Knight":
            attackdmg = 4
            cardhp = 11
        if placedcard0 == "Archer":
            attackdmg = 4
            cardhp = 8
        if placedcard0 == "Healer":
            attackdmg = 4
            cardhp = 7
        if placedcard0 == "Horseman":
            attackdmg = 5
            cardhp = 9
        movetype()
    if choice == "1":
        print("You place down", currenthand[1])
        placedcard0 = currenthand.pop(1)
        placedcard0_check = True
        enemymove()
        print("Your opponent has placed down a card, You can now attack. Attacking works the same as picking a card, select the card you'd like to attack with, (Your card is on tile 0) and their current card is on 0")
        print("So if you type select 0 and then type attack 0 and you will attack their card!")
        if placedcard0 == "Holy Knight":
            attackdmg = 4
            cardhp = 12
        if placedcard0 == "Knight":
            attackdmg = 4
            cardhp = 11
        if placedcard0 == "Archer":
            attackdmg = 4
            cardhp = 8
        if placedcard0 == "Healer":
            attackdmg = 4
            cardhp = 7
        if placedcard0 == "Horseman":
            attackdmg = 5
            cardhp = 9
        movetype()
    if choice == "2":
        print("You place down", currenthand[2])
        placedcard0 = currenthand.pop(2)
        placedcard0_check = True
        enemymove()
        print("Your opponent has placed down a card, You can now attack. Attacking works the same as picking a card, select the card you'd like to attack with, (Your card is on tile 0) and their current card is on 0")
        print("So if you type select 0 and then type attack 0 and you will attack their card!")
        if placedcard0 == "Holy Knight":
            attackdmg = 4
            cardhp = 12
        if placedcard0 == "Knight":
            attackdmg = 4
            cardhp = 11
        if placedcard0 == "Archer":
            attackdmg = 4
            cardhp = 8
        if placedcard0 == "Healer":
            attackdmg = 4
            cardhp = 7
        if placedcard0 == "Horseman":
            attackdmg = 5
            cardhp = 9
        movetype()




