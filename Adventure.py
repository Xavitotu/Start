def name(na):
    print(nam)
    
left = "left"
right = "right"
down = "down"
up = "up"
yes = "yes"
no = "no"
cont = "continue"
sleep = "sleep"
ign = "ignore"
listen = "listen"
follow = "follow"
other = "other way"

nam = input("What is your name? ")
print("")
print("You wake up in the middle of the forest, you don't remember anything, all you have is a flash light with little")
print("to no battery and an empty water bottle. The sun seems like it will set soon. You see what ressembled to be two")
a = input("roads, one going left and one going right, which one do you choose? ")

if a == left:
    print("")
    b = input("You walk for for what seems like an hour and the sun is barley vissible, you see a worn down house to your left,\nbut the road you were on still goes forward into a forest. Do you check the house? ")

elif a == right:
    print("")
    b = input("You walk for a very long time, so long that the sun has just set and the road is barely visible. \nThe road you are on goes into a forest. You fear that you might get lose the road by lack of brightness, do you \nturn on the flashlight? ")

if a == left and b == yes:
    print("")
    c = input("You check the front door of the house, closed. You break open the door and go inside. There isn't much inside, \nsome broken cloth, two snacks that you devoured instantly [you glutton], an old tv with the remote ontop, and\nsome shotgun shells in the floor.There was also a pond in the back of the house which you used to fill your \nwaterbottle. The sun just set and it's night time. You get a feeling of dread when looking at the bed. Do you \nstay in the house and sleep or do you continue on the road? ")

elif a == left and b == no:
    print("")
    c = input("You ignore the house and continue ahead. It's almost night, you continue onwards through the road on the forest \nuntil all of the sudden you hear faint wispers, ''Come close, follow me'', the wispers get stronger on you \nears, do you ignore them or do you listen? ")

elif a == right and b == yes:
    print("")
    c = input("You turn on the flash light and istantly see better. You find the road again and continue along. You hear \nmovement on you right and decided to check what it was, it was just a deer that ran away when you saw it.\nAfter a long walk you flash light battery runs out but you hear the sound of running water you don't know what it \nis but you guess it's a very big river, do you follow the water or do you go the other way? ")

elif a == right and b == no:
    print("")
    c = input("Probably for the better, you don't have alot of battery after all. You continue slowly, feeling the road before you walk on it. All of the sudden you hear movement behind you in the bushes, it starts off distant but it quickly\ngets louder behind you. whatever it is it's rushing towards you in an alarming rate. Do you run? ")

if a == left and b == yes and c == sleep:
    print("")
    print(f"You lay on the bed and fall asleep in a minute. You get woken up by a loud grunt coming from the main door.\nYou hear a mixture of loud steps and heavy breathing coming your direction. You start to hyperventalate in panic\n''YOU!!'' A big man with jeans, no shirt [awesome 8-pack btw] and a shotgun comes to you. ''I'm not going to let you get away with what you did {nam}! Time to pay the price.'' You don't know what is happening and you try to \nspeak for reason and to question, but before you can, your hear a loud explosion. You first feel shock, then you \nfeel pain, then you feel like your in the air, then you feel like your flying in the air, then you feel nothing.")
    print("")
    print("")
    print("Shot ending")
    print("ending 1/8")

elif a == left and b == yes and c == cont:
    print("")
    print(f"You leave the house and continue on the road. The sun has just set and you can't see anything. You use the\nflashlight to see and continue through the woods. You hear the sound of an engine closing in on you and decided \nto scream for them. Thankfully they hear you and a fourtrack comes towards tour direction. ''Woah buddy, you seem\nlost, need help?'', you get a feeling of relief after hearing this. ''Names'Bob, and hes Gary'' he points to the \nman that is driving,'' What's yours... {nam} huh, well nice to meet you, what happened?'', He pauses for a second,\n''Oh wait a second''. He turns around to see Gary who was distracted with the handle of the vehical, ''Hey Gary,\nnwhat was the name of the guy in that crazy plane story you told me, the one that they didn't find?''. Gary \nstares of in the distance for a moment ''If I remember correctly, I think it was {nam}.")
    print("")
    print("")
    print("Fourtrack ending")
    print("ending 2/8")

elif a == left and b == no and c == listen:
    print("")
    print(f"You decide to listen and start following the whispers, ''Yes, come. This way. Follow me.'' You start halusinating\nand you know because all of the sudden you see a deer standing in its two. ''Folow me.'' you continue following,\nyou start to feel numb, you can't feel your legs anymore, you can't even think straight anymore, but no matter\nwhat, you continue following the whispers. ''Yes, your almost ther, {nam}.''")
    print("")
    print("")
    print("Lost ending")
    print("ending 3/8")

elif a == left and b == no and c == ign:
    print("")
    print(f"You try your best to ignore the whispers. They get louder but you do a good job to hear istead of listening to the\nwords. They get loud to the point it hurts so much you scream in pain. Finally they disapear after your scream.\nYou then find a light source, you dicide to investigate. You find a village that seems abandoned. The light source\n comes from a small lamp in a news board in the center of the village. Theres one newsppaper in the whole\nboard, ''Missing persons after disaster''. You look at the names that the poster higlited. One name caught your eye,\n''{nam}''")
    print("")
    print("")
    print("Missing ending")
    print("ending 4/8")

elif a == right and b == yes and c == follow:
    print("")
    print("You follow the noise. It seems it's farther than expected, so you start joging. You don't seem to be getting closer\nso you start to run. You get a big carless while running and you trpi with a branch on the floor. You fall and \nstart rolling down a clif. You hit every rock and tree in the way until you finally stop in a river. The river is a\nvery rapid one and you drown due to lack of energy and with pain because of the trip.")
    print("")
    print("")
    print("Tripped ending")
    print("ending 5/8")

elif a == right and b == yes and c == other:
    print("")
    print("You decide to go the other way incase that sound was because of a waterfall. You walk for miles again in the dark\nuntil you hear a helicopter over you. You try to signal the helicopter but there is no way to because of how dark\nit is, maybe if you still had battery on your flashlight you could have. The heli is now gone, your only chance to\nbe saved now in ashes. You scream out of frustration and you start to throw a fit. You start kicking and\npunching anything you see and you eventually pass out. You wake up in the middle of the day without remembering\nanything. you try to remember last night but you get startled by something coming through the bushes. You go to\ncheck what it is until a pack of wolves start huddling around you.")
    print("")
    print("")
    print("Surrounded ending")
    print("ending 6/8")

elif a == right and b == no and c == yes:
    print("")
    print("You run as fast as you can from the sound. You don't know if it is still following but you still run just incase.\nYou then suddenly trip with a branch on the floor ans start rolling down a clif, hitting evry rock and tree along\nthe way. You finnaly reach a flat surface all bruised and bleeding and you are meet with a big angry bear standing\nbeside you")
    print("")
    print("")
    print("Chased ending")
    print("ending 7/8")

elif a == right and b == no and c == no:
    print("")
    print("You stand your ground against the rushing object. It is about to hit you but your braveness knows no bounds.\nFinally through the bushes you find a deer that running extremly fast and it just passes you by. You decide to continue\nthrough the road until you hear a helicopter passing by. You try to scream at it to get it's attention until you\nremember your flashlight. You use the flaslight upwards to signal them you are there. They see the beam of\nlight and turn towards your direction")
    print("")
    print("")
    print("Escaped ending")
    print("ending 8/8")