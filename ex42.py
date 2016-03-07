from sys import exit
from random import randint

class Game(object):
    
    def __init__(self, start):
        self.quitps=[
            "You died, fuck your mom.",
            "Hahaha, you're fucked up.",
            "Go died."
        ]
        self.start=start
        
    def play(self):
        next=self.start
        
        while True:
            print "\n------------"
            room = getattr(self, next)
            next=room()
            
    def death(self):
        print self.quitps[randint(0, len(self.quitps)-1)]
        exit(1)

    def central_corridor(self):
        print """
        The Gothons of Planet Percal #25 have invaded your ship and destroyed
        your entire crew. You are the last surviving member and your last
        mission is to get the neutron destruct bomb from the Weapons Armory,
        put it in the bridge, and blow the ship up after getting into an
        escape pod.
        \n
        You're running down the central corridor to the Weapons Armory when
        a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume
        flowing around his hate filled body. He's blocking the door to the
        Armory and about to pull a weapon to blast you.
        """
        
        action=raw_input(">")
        if action == "shoot!":
            print """
            Quick  on  the  draw  you  yank  out  your  blaster  and  fire  it  at  the  Gothon.
            His  clown  costume  is  flowing  and  moving  around  his  body,  which  throws
            off  your  aim.    Your  laser  hits  his  costume  but  misses  him  entirely.    This
            completely  ruins  his  brand  new  costume  his  mother  bought  him,  which
            makes  him  fly  into  an  insane  rage  and  blast  you  repeatedly  in  the  face  until
            you  are  dead.    Then  he  eats  you.
            """
            return 'death'

        elif action == "dodge!":
            print """
            Like  a  world  class  boxer  you  dodge,  weave,  slip  and  slide  right
            as  the  Gothon's  blaster  cranks  a  laser  past  your  head.
            In  the  middle  of  your  artful  dodge  your  foot  slips  and  you
            bang  your  head  on  the  metal  wall  and  pass  out.
             """
            return "death"

        elif action == "tell a joke":
            print "you make it they lmao and you shoot those sob"
            return 'laser_weapon_armory'

        else:
            print "DOES NOT COMPUTE"
            return 'central_corridor'

    def laser_weapon_armory(self):
        print "You are in the weapon Armory"
        print "You saw a panel to control neutron bomb. You need to enter the code"
        print "The code is 3 digits."
        code="%d%d%d" % (randint(1,9),randint(1,9),randint(1,9))
        guess=raw_input("[keypad]>")
        guesses=0
        
        while guess!=code and guesses<10:
            print "BZZZEDD"
            guesses+=1
            guess=raw_input("[keypad]>")
        
        if guess==code:
            print "you got the bomb and you runt to the bridge"
            return 'the_bridge'
        else:
            print "You fucked things up. It blows up and died."
            return 'death'
            
    def the_bridge(self):
        print "All the alliens saw your bomb and scared the shit out. They left and you are safe."
        exit(0)

game=Game("central_corridor")
game.play()
