import time

import random



mazeMap={}

mazeMap['room11']={'e':'room12','w':'','n':'','s':''}

mazeMap['room12']={'e':'','w':'room11','n':'room13','s':''}

mazeMap['room13']={'e':'room14','w':'','n':'','s':'room12'}

mazeMap['room15']={'e':'','w':'room14','n':'','s':''}

mazeMap['room14']={'e':'room15','w':'room13','n':'','s':''}

mazeMap['room16']={'e':'','w':'','n':'room15','s':''}

inventory=['jackknife','rope','matches']

current_position='room11'

game_over=False

justEntered=True

command=''

vspace='\n\n\n\n\n\n\n\n'

print(vspace)

print(" HOLE in the SCHUYLER" )

print('\n\n\n')

print("The awesomest game you will ever play!!")

print(vspace)

print('Loading game... please wait ....')

time.sleep(3)

print(vspace)

print("A 7.3 magnitude earthquake hit Bronx...")

time.sleep(2)

print("as you were walking in a hallway of Fort Shuyler....")

time.sleep(2)

print("ROCKS FALL!!!! You find yourself trapped")

time.sleep(2)

print("... but a hidden door to the ground is found!!!" )

time.sleep(2)

print("You open it and walk down the stairs...")

time.sleep(2)

print("!!!Only to find the hidden door locking itself with a loud thud!!!")

time.sleep(2)

print("You are in a dark room1")

time.sleep(2)





print("type 'help' to bring up available commands")

def movement(command):

    global current_position

    global justEntered

    if command in ['e','east','go east']:

        command='e'

        print('You walk east')

    elif command in ['w','west','go west']:

        command='w'

        print('You walk west')

    elif command in ['s','south','go south']:

        command='s'

        print('You walk south')

    elif command in ['n','north','go north']:

        command='n'

        print('You walk north')

    else:

        return

    if mazeMap[current_position][command]=='':

        print('You cannot go that way!')

    else:

        current_position=mazeMap[current_position][command]

        justEntered=True

    







def room11(): 

    global room_name

    global description

    global justEntered

    if justEntered:

        room_name='a smelly room'

        description=''' The room is dark. You lit a torch. 

        Something smells funny. Did you fart?'''

        print('You are in '+room_name)

    if been_there['room11']==False:

        print(description)

        room_item['room11']=['note']

        been_there['room11']=True

        

    if 'note' in inventory:

        print('''The note reads: "Dear whoever you are. 

        You are basically as good as dead. The only way out will be to

        defeat the evil ____ who resides in the deepest of this cave"''')

        print("The note magically disappears!")

        inventory.remove('note')

        return



    if command=='search':

        print('You find a writing on the wall that says "Clash LOLyale is so lame."')



    justEntered=False

    

def room12(): 

    global room_name

    global description

    global justEntered

    global found_knife

    if justEntered:

        room_name='the smoky room'

        description=''' Smoke is everywhere. You find it hard to see. 

        It looks like someone was just here.'''

        print('You are in '+room_name)

        

    if been_there['room12']==False:        

        print(description)

        room_item['room12']=['firewood']

        found_knife=False

        been_there['room12']=True

        

    if command=='search':

        if found_knife==True:

            print('You did not find anything')

        else:

            print('Among the ashes you found a knife! Use the get command to pick up the knife')

            room_item['room12'].append('knife')

            found_knife=True

    justEntered=False

    

    

def room13(): 

    global room_name

    global description

    global justEntered

    if justEntered:

        room_name='the room with many columns'

        description=''' This looks like a good hiding place for thieves.'''

        print('You are in '+room_name)

        justEntered=False

        

    if been_there['room13']==False:        

        print(description)

        room_item['room13']=[]

        been_there['room13']=True

        

    if ('knife' in inventory) and (not('bag of gold' in inventory)):

        print('A angry looking man appears in front of you. He looks evil.')

        print('"Hey! I was looking for that knife! Gimme that!"')

        print('Do you (f)ight? or (g)ive him his knife back?')

        choice=input('(Choose f or g) >')

        if choice[0]=='f':

            print('''You flash the knife threatening the evil looking man. 

            He screams and runs away, leaving a bag of gold.

            You pick up the bag of gold''')

            inventory.append('bag of gold')

        else:

            print('''You give the man your knife. 

            He then threatens you to get into a pit. 

            There is no way to get out...''')

            game_over=True



    if command=='search':

        print('A frog leaped in front of you. You screamed in fear.')



    justEntered=False



def room14(): 

    global room_name

    global description

    global justEntered

    if justEntered:

        room_name='the spooky room'

        description=''' There is a feint sound of weeping. 

        But you are not sure if it is real.'''

        print('You are in '+room_name)



        

    if been_there['room14']==False:        

        print(description)

        room_item['room14']=[]

        been_there['room14']=True

        

    if ('bag of gold' in inventory) and justEntered:

        print('Someone is heard crying loudly. You are startled by his appearance')

        print('You are relieved to find that he is a little boy.')

        print('Do you (a)sk why he is crying? or (i)gnore him?')

        choice=input('(Choose a or i) >')

        if choice[0]=='a':

            print('''You ask him, "Why are you crying?"

            The boy answers "A thief attacked me and took my bag of gold!"

            Do you (g)ive him the gold or (h)ide the fact that you have it?''')

            choice=input('(Choose g or h) >')

            if choice[0]=='g':

                print(''' The boy takes the bag of gold and is overjoyed!

                He says "Thank you! I will give you a tip. Do not trust any person you meet in this dungeon.

                Some may look normal, but everyone is either a monster or a ghost."

                The boy disappears in a thin air! 

                Then clank, something dropped to the ground''')

                room_item['room14'].append('green key')



    if command=='search':

        print('A frog leaped in front of you. You screamed in fear.')



    justEntered=False





def room15(): 

    global room_name

    global description

    global justEntered

    if justEntered:

        room_name='the nothing room'

        description=''' The room1 look so empty. 

        This looks like a dead end.

        The south wall looks a little funny though. '''

        print('You are in '+room_name)



        

    if been_there['room15']==False:        

        print(description)

        room_item['room15']=[]

        been_there['room15']=True

        

    if command=='search':

        print('You search the room1 and accidently step on some lever.')

        print('An opening in the south wall appears!')

        mazeMap['room15']['s']='room16'



    justEntered=False





def room16(): 

    global room_name

    global description

    global justEntered

    if justEntered:

        room_name='the room with a portal'

        description=''' There is a portal in this room1.

        There are buttons 1 through 5 on the portal control.

        Type "use portal" to use the portal. '''

        print('You are in '+room_name)

        

    if been_there['room16']==False:        

        print(description)

        room_item['room16']=[]

        been_there['room16']=True



    if command=='use portal':

        print('''Unfortunately, this feature is not implemented yet.

        When fully functional, 

        this portal will lead you to different levels of the dungeon.

        However, level 16 will only be accessible if you collect

        five shards and plug it into this portal control.''')



    if command=='search':

        print('A frog leaped in front of you. You screamed in fear.')        





    justEntered=False









been_there={'room11':False,'room12':False,'room13':False,'room14':False,'room15':False,'room16':False}

room_item={}



while True:

    if current_position=='room11':

        room11()

    elif current_position=='room12':

        room12()

    elif current_position=='room13':

        room13()

    elif current_position=='room14':

        room14()

    elif current_position=='room15':

        room15()

    elif current_position=='room16':

        room16()

        

    time.sleep(0.3)

    command=input('>')

    command=command.lower()

    

    if command=='inventory':

        print(inventory)

        continue



    if command[:4]=='drop':

        item=command[5:].rstrip(' ').lstrip(' ')

        if item in inventory:

            print('You drop your '+item)

            inventory.remove(item)

            room_item[current_position].append(item)

        else:

            print("You don't have that item in your inventory")

            continue

    

    if command[:3]=='get':

        item=command[4:].rstrip(' ').lstrip(' ')

        if item in room_item[current_position]:

            print('You pick up '+item)

            room_item[current_position].remove(item)

            inventory.append(item)

        else:

            print("I don't see that item in this room1")

            continue



    if command=='look':

        print('You are in '+room_name)

        print(description)

        print('Items in this room1:' + str(room_item[current_position]))

        continue    

    

    if command=='quit':

        print('Thanks for playing the game!')

        print('Game over')

        break

    

    if command in ['?','help']:

        print('Available commands in any room1:')

        print('search','look','drop','quit','get')

        print('To move, type in "e","w","s" or "n"')

        print('To pick up an item, type "get [item]". The [item] has to be spelled exactly as in the list of items in the room1')

        print('To leave an item in the room1, type "drop [item]". For example "drop rope" will drop the rope you have')

        print('Command "doors" will show available directions you can move.')

    

    if command=='doors':

        print(mazeMap[current_position])



    

    movement(command)

    

    if game_over==True:

        print('Sadly you failed to escape. Your life is over. No more Clash Royale.')

        break