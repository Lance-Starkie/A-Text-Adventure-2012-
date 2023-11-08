x = (0);
y = (0);
win = (0);
potato = (1);
axe = (0);
hunger = (0);
print ("instructions:")
print ("pick 'n', 'e', 's', 'w', according to what you want to do");
print ("if it asks a question, answer 'y' or 'n' according to what you want to do");
print ("");
print ("Welcome to potato land");
tree = (0);
thirst = (0);
wood = (0);
day = (0);
time = (0);
chair = (0);
house = (0);
shack = (0);
wings = (0);
bridge = (0);
while (win == 0):
        time = (time)+(1);
        if time > (3):
                time = (0);
                day = (day)+(1);
        if time > (1):
                print ("It's night time.");
        else:
                print ("It's day time.");
        tree = (tree)+(1);
        if tree > (3):
                tree = (3);
        print('You have survived ', end="")
        print(day, end="")
        print("days.")
        hunger = (hunger)+(1);
        thirst = (thirst)+(1);  
        print('x=', end="")
        print(x, end="")
        print(' y=', end="")
        print (y);
        print ("north(n)");
        print ("east(e)");
        print ("south(s)");
        print ("west(w)");
        lulz = input("");
        if lulz == ("n"):
                y = (y)+(1);
        elif lulz == ("e"):
                x = (x)+(1);
        elif lulz == ("s"):
                y = (y)-(1);
        elif lulz == ("w"):
                x = (x)-(1);
        if x == (0):
                print ("");
                if y == (0):
                        print ("this is were you started");
                        if house == (1):
                                print ("You have a house");
                                print ("Do you want to sleep in it??? (y/n)");
                                lulz = input("");
                                if lulz == ("y"):
                                        print ("You were eaten in your sleep");
                                        win = (1);
                        elif wood > (15):
                                print ("do you want to build a house? (y/n)");
                                lulz = input("");
                                if lulz == ("y"):
                                        print ("there!")
                                        house = (1);
                                        wood = (wood)-(16);
                        if shack == (1):
                                print ("You have a shack");
                        elif wood > (8):
                                print ("Do you want to build a shack? (y/n)");
                                lulz = input("");
                                if lulz == ("y"):
                                        print ("Hehe, shacks are usless, but okay!");
                                        shack = (1);
                        if chair == (1):
                                print ("You have a creeky, breaking, unlucky, chair")
                                print ("do you want to sit in it? (y/n)")
                                lulz = input("");
                                if lulz == ("y"):
                                        print ("You transend god.");
                                        print ("You win");
                                        win = (1);
                        elif wood > (110):
                                print ("do you want to build a, wait, what??? how di...");
                                lulz = input("");
                                if lulz == ("y"):
                                        print ("okay...");
                                        chair = (1);
                        elif wood > (2):
                                print ("do you want to build a chair? haha!!! just kidding, you need 112 wood for that!");
                elif y == (1):
                        if potato == (1):
                                print ("A potato sits at your feet, do you eat it?(y/n)");
                                lulz = input("")
                                if lulz == ("y"):
                                        print ("you sprout wings, you fly");
                                        wings = (1);
                                        hunger = (hunger)-(6);
                                        if hunger < (0):
                                                hunger = (0)
                                elif lulz == ("n"):
                                        print ("the potato eats you");
                                        win = (1)
                                else:
                                        print("the potato hates rule breakers, so he leaves through an underground tunnel");
                                potato = (0);
                        else:
                                print ("the potato once sat here");
                                print ("");
                                print (nn);
                                print (ee);
                                print (ss);
                                print (ww);
                                lulz = input("");
                                if lulz == ("n"):
                                        y = (1);
                elif y == (-1):
                        print ("Oops, that was a cliff, well, BYE!!!!")
                        win = (1)
                else:
                        print ("thats a cliff tooo!!!!!!");
                        win = (1)

        elif x == (1):
                print ("")
                if y == (0):
                        print ("A dead man sits at your feet");
                        print ("He has an axe through his chest");
                        print ("do you take the axe through his chest?(y/n)");
                        lulz = input("")
                        if lulz == ("y"):
                                print ("you take the axe");
                                axe = (1);
                        elif lulz == ("n"):
                                print ("he comes to life and eats you");
                                win = (1);
                        else:
                                print ("That answer is invalid, so screw you.");
                elif y == (-1):
                        print ("Oops, that was a cliff, well, BYE!!!!")
                        win = (1)
                elif y == (-1):
                        if wings == (1):
                                print ("Do you want to fly over them");
                                lulz = input("");
                                if lulz == ("y"):
                                        print ("Ok, you won't fall in");
                                else:
                                        print ("You slowly fly into HELL!!");
                                        print ("It is the Devil");
                                        print ("Do you you...");
                                        print ("A: Fight him.");
                                        print ("B: Steal his bike.");
                                        print ("C: Ask him for a hamburger.");
                                        print ("D: well... um....");
                                        print ("(a/b/c/d)");
                                        lulz = input("");
                                        if lulz == ("a"):
                                                print ("you die Bit**");
                                                win = (1)
                                        elif lulz == ("b"):
                                                print ("YES, YOU HAVE IT!!!!, YOU HAVE DULAHAN!");
                                                print ("YOU FLY OUT OF HELL, BIKE IT HAND!!!!");
                                                print ("INFACT! YOU TRANSEND GOD!!!!!!!!!!!!!!!!!!!!!");
                                                win = (1)
                                        elif lulz == ("c"):
                                                print ("He gives you one and it turns out he has 11 stars out of 10 for COSTOMER SERVICE!!!!");
                                                hunger = (-1000);
                                        elif lulz == ("d"):
                                                print ("Why, why in the hell....");
                                                print ("You test possitive for pregnancey");
                                                print ("You have a child");
                                                print ("Name him.");
                                                name = input ("");
                                                print(name, end="")
                                                print(", lives with his father for the rest of his life");
                                        elif lulz == ("e"):
                                                print("E? U WOT M8")
                                        else:
                                                print("You die");
                                                win = (1)
                        else:
                                print ("Oops, that was a ravine in the earth leading to HELL!!!!!, well, BYE!!!!")
                                win = (1)
                elif y == (-2):
                        if bridge == (0):
                                print ("this area seems suitable for building a bridge.");
                                if wood>(5):
                                        print ("Do you want to build one?(y/n)");
                                        lulz = input ("");
                                        if lulz == (y):
                                                print ("OK!!!!");
                                                bridge = (1);
                                        elif lulz == (n):
                                                print ("WELL FINE");
                                                thirst = (13);
                                else:
                                        print ("but you would need at least 5 wood");
                        else:
                                print ("There is a bridge to the west.");
                elif y == (-3):
                        if bridge == (1):
                                print("You are on a bridge")
                        else:
                                print("There wasn't a bridge.... So yeah... BYE!!!!");
                                win = (1)
                elif y == (-4):
                        print ("That's a cliff!!! :D yay, I don't need to deal with you anymore! BYE!!!!");
                else:
                        print ("thats a cliff tooo!!!!!!");
                        win = (1)
        elif x == (-1):
                print ("")
                if y == (0):
                        print ("OH NO, theres a hungery lion staring right at you!!!");
                        print ("This seems to be a lion hot spot");
                        if axe == (1):
                                print ("Consume Lion?(y/n)");
                                lulz = input("")
                                if lulz == ("y"):
                                        print("You consumed the lion.");
                                        hunger = (hunger)-(3);
                                        if hunger < (0):
                                                hunger = (0)
                                else:
                                        print("it ate you");
                        else:
                                print ("Well your screwed");
                                print ("BYE!!");
                                win = (1);
                elif y == (1):
                        print ("Oh, there is a river");
                        print ("Do you drink from it???(y/n)");
                        lulz = input("");
                        if lulz == ("y"):
                                print ("The water is delicious");
                                thirst = (thirst)-(5);
                                if thirst < (0):
                                        thirst = (0)
                elif y == (-1):
                        if tree == (0):
                                print ("There isn't anything here");
                        elif tree == (1):
                                print ("There is a small sapling here. You could get a bit of wood out of it,");
                                if axe == (1):
                                        print ("do you want to?(y/n)");
                                        lulz = input("")
                                        if lulz == ("y"):
                                                print ("You chop up the sapling.");
                                                wood = (wood)+(2)
                                                tree = (0)
                                        else:
                                                print ("ok :(");
                                else:
                                        print ("but you don't have an axe or anything.");

                        elif tree == (2):
                                print ("There is a small tree here. You could get some wood out of it,");
                                if axe == (1):
                                        print ("do you want to?(y/n)");
                                        lulz = input("");
                                        if lulz == ("y"):
                                                print ("You chop down the small tree");
                                                wood = (wood)+(5);
                                                tree = (0);
                                        elif lulz == ("potate"):
                                                wood = (wood)+(1000);
                                        else:
                                                print ("ok :(");
                                else:
                                        print ("but you don't have an axe or anything.");
                        elif tree == (3):
                                print ("There is a large tree here. You could get a lot of wood out of it,");
                                if axe == (1):
                                        print ("do you want to?(y/n)");
                                        lulz = input("")
                                        if lulz == ("y"):
                                                print ("You chop down the tree");
                                                wood = (wood)+(11)
                                                tree = (0)
                                        else:
                                                print ("ok :(");
                                else:
                                        print ("but you don't have an axe or anything.");
                else:
                        print ("thats a cliff tooo!!!!!!");
                        win = (1)
        else:
                print ("thats a cliff tooo!!!!!!");
                win = (1)
        print('Your hunger is ', end="")
        print(hunger);
        if hunger > (10):
                print ("You have starved");
                win = (1);
        elif hunger > (5):
                print ("you getting hungery");
        print('Your thirst is ', end="")
        print(thirst);
        if thirst > (15):
                print ("You have died of dehydration.");
                win = (1);
        elif thirst > (7):
                print ("your getting dehydrated.");
        print('You have is ', end="")
        print(wood);
print ("The game is over");
input();
