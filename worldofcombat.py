import random
def woc():
    print "Welcome to the World of Combat!"
    start_power = 5
    start_defense = 5
    start_speed = 5
    start_hp = 20
    name = raw_input("Greetings, wanderer. What is your name?")
    print "Hm, I see. Well, %s, let me ask you some questions.(press enter to continue)" % (name)
    raw_input("")
    race = raw_input("What race are you, Dwarf, Elf, or Human?")
    if race == 'dwarf':
        print "Ah, a hearty man of the mountain. Stout but strong"
        raw_input("")
    elif race == 'elf':
        print "The lithe descendants of the woods... lithe and graceful"
        raw_input("")
    elif race == 'human':
        print "The stalwart sentinels of the plains. Strong willed and fiercely ambitious"
        raw_input("")
    else:
        print "Hmm... don't think I've heard of that"
        raw_input("")
    weapon = raw_input("Choose your weapon... Sword, Spear, or Hammer?")
    if weapon == 'sword':
        print "Ahh, the blade... a mighty fine choice"
        power = start_power + random.randint(2,8)
        raw_input("")
    elif weapon == 'spear':
        print "Hmm, a warrior of the spear. Admirable"
        power = start_power + random.randint(1,10)
        raw_input("")
    elif weapon == 'hammer':
        print "A single hammer, not a bad choice, wanderer"
        power = start_power + 5
        raw_input("")
    else:
        print "No valid weapon... interesting"
        power = start_power + 1
        raw_input("")
    armor = raw_input("And now your armor of choice? Wear you a cloak, a leather tunic, or a set of plate?")
    if armor == 'cloak':
        print "A good cloak is always worth carrying on the road"
        defense = start_defense + random.randint(4,5)
        speed = start_speed + random.randint(1,5)
        hp = start_hp + 1
        raw_input("")
    elif armor == 'leather tunic':
        print "Nothing wrong with a hardy tunic on your chest"
        defense = start_defense + random.randint(2,8)
        speed = start_speed + random.randint(1,3)
        hp = start_hp + random.randint(1,3)
        raw_input("")
    elif armor == 'set of plate' :
        print "The strongest defense against goblins and dragons, to be sure"
        defense = start_defense + random.randint(3,12)
        speed = start_speed - 1
        hp = start_hp + random.randint(4,6)
        raw_input("")
    else:
        print "No armor at all? As you wish"
        defense = start_defense + 1
        speed = start_speed + 0
        raw_input("")
    skill = raw_input("What sort of training did you recieve? Striking, Guarding, or Dodging?")
    if skill == 'striking':
        print "A fine warrior you'll make. A deft %s strike is all that matters" % (weapon)
        fin_power = power + random.randint(3,5)
        fin_defense = defense + 0
        fin_speed = speed + random.randint(1,3)
        fin_hp = hp + 0
        raw_input("")
    elif skill == 'guarding':
        print "If we cannot defend, then how can we survive? A strong parry is vital"
        fin_defense = defense + random.randint(3,5)
        fin_power = power + 0
        fin_speed = speed + 0
        fin_hp = hp + random.randint(1,3)
        raw_input("")
    elif skill == 'dodging':
        print "As a wise man once said, not getting hit is the key to victory. A quick dodge can save a life"
        fin_speed = speed + random.randint(3,5)
        fin_power = power + random.randint(1,3)
        fin_defense = defense + 0
        fin_hp = hp + 0
        raw_input("")
    else:
        print "No training... best you stay wary on the road"
        fin_power = power + 1
        fin_speed = speed + 0
        fin_defense = defense + 0
        fin_hp = hp + 1
        raw_input("")
    print "So to sum up, you are a %s called %s, in your hand you carry a %s, you wear a %s, and you recieved training in the art of %s... I wish you the best of luck on your quest through this world. You'll need it on the road ahead" % (race, name, weapon, armor, skill)
    raw_input("")
    print "Your current power is %s" % (fin_power)
    print "Your current defense is %s" % (fin_defense)
    print "Your current speed is %s" % (fin_speed)
    print "You currently have %s health points" % (fin_hp)
    raw_input("")
    adj = random.choice(['dark','long-forgotten','quiet','humid','damp'])
    setting = random.choice(['forest','desert','castle','ruin'])
    print "Your eyes open, and you awake in a %s %s" % (adj,setting)
    raw_input("")
    adje = random.choice(['long', 'dusty', 'dirt covered', 'stone'])
    road = random.choice(['road', 'path', 'bridge', 'pass'])
    print "Further ahead you spot a %s %s... perhaps it could be followed" % (adje, road)
    choice = raw_input("What do you choose to do?")
    if choice == 'follow':
        print "You tread slowly onward, scanning as you go"
        raw_input("")
    else:
        print "You cannot, a stone wall blocks your path back. There is only one choice in the matter"
        raw_input("")
    print "As you walk forward, you hear a rustling nearby... Do you wait, or continue?"
    reply = raw_input("Make the decision")
    if reply == 'continue':
        print "As you move forward, you hear a leaping from behind. You turn, and come face to face with a fearsome creature"
        raw_input("")
    elif reply == 'wait':
        print "You watch intently as a creature moves into sight... You track it with your eyes"
        raw_input("")
    adjec = random.choice(['large', 'small', 'powerful'])
    creature = random.choice(['werewolf', 'hound', 'boar', 'golem'])
    movement = random.choice(['lopes', 'runs', 'bounds', 'lumbers', 'charges'])
    print "Slowly, recognition lights up your eyes, as you realize this beast is a %s" % (creature)
    raw_input("")
    print "Within moments, the %s %s %s towards you, with anger in its eyes" % (adjec, creature, movement)
    raw_input("")
    cpower = 7 + random.randint(1,3)
    cdefense = 7 + random.randint(1,3)
    cspeed = 7 + random.randint(1,3)
    chp = 9 + random.randint(1,3)
    if adjec == 'large':
        crpower = cpower + 2
        crdefense = cdefense + 1
        crspeed = cspeed - 2
        crhp = chp + 3
    elif adjec == 'small':
        crpower = cpower - 2
        crdefense = cdefense - 1
        crspeed = cspeed + 3
        crhp = chp - 1
    elif adjec == 'powerful':
        crpower = cpower + 3
        crdefense = cdefense + 0
        crspeed = cspeed - 1
        crhp = chp + 0
    else:
        print "Creature dies instantly"
    if creature == 'werewolf':
        crepower = crpower + 1
        credefense = crdefense + 1
        crespeed = crspeed + 1
        crehp = crhp + 1
    elif creature == 'hound':
        crepower = crpower - 1
        credefense = crdefense + 0
        crespeed = crspeed + 2
        crehp = crhp - 2
    elif creature == 'boar':
        crepower = crpower + 0
        credefense = crdefense - 1
        crespeed = crspeed + 3
        crehp = crhp - 1
    elif creature == 'golem':
        crepower = crpower + 1 
        credefense = crdefense + 3
        crespeed = crspeed - 3
        crehp = crhp + 3
    print "The %s's power is %s" % (creature, crepower)
    print "The %s's defense is %s" % (creature, credefense)
    print "The %s's speed is %s" % (creature, crespeed)
    print "The %s has %s health points" % (creature, crehp)
    raw_input("")
    act = raw_input("You draw your weapon, will you attack the creature?")
    
        
    
